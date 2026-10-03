#!/usr/bin/env python3
"""Minera correções do usuário e desculpas do agente em históricos de conversa.

Uso:
    python3 minerar_correcoes.py <arquivo|pasta> [...] [--out correcoes.md]
                                 [--extra-regex PADRAO] [--max 400]

Fontes suportadas: SQLite (tabela com colunas role/content), .jsonl, .json, .md, .txt.
Só usa a biblioteca padrão.
"""
from __future__ import annotations

import argparse
import json
import re
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

USER_PATTERNS = [
    # PT-BR
    r"j[aá] era pra", r"eu (j[aá] )?(te )?(pedi|falei|disse)", r"de novo", r"outra vez",
    r"n[aã]o (era|foi) (isso|o que)", r"cad[eê]", r"por que (voc[eê] )?(n[aã]o|parou)",
    r"n[aã]o entendi", r"errado", r"para de", r"pare de", r"n[aã]o quero", r"nunca mais",
    r"sempre (que|faça|fa[cç]a)", r"aff", r"oxe", r"p[oô]rra", r"caralho", r"t[aá] errado",
    r"n[aã]o funcionou", r"n[aã]o chegou", r"esqueceu", r"de novo isso", r"quantas vezes",
    r"n[aã]o aguento", r"te corrigir",
    # EN
    r"i (already )?(told|asked) you", r"again\b", r"that'?s not what", r"why (did|didn'?t) you",
    r"stop (doing|asking)", r"\bwrong\b", r"never do", r"always do", r"didn'?t work",
    r"where (is|are) the", r"how many times",
]
AGENT_PATTERNS = [
    r"tem raz[aã]o", r"desculp", r"erro meu", r"foi mal", r"falha minha", r"me equivoquei",
    r"you'?re right", r"my (mistake|bad)", r"i apologi[sz]e", r"sorry",
]
ROLE_USER = {"user", "human"}
ROLE_AGENT = {"assistant", "ai", "model"}
EXTS = {".db", ".sqlite", ".sqlite3", ".jsonl", ".json", ".md", ".txt"}


def _ts(value) -> str:
    try:
        v = float(value)
        if v > 1e12:
            v /= 1000
        return datetime.fromtimestamp(v, tz=timezone.utc).strftime("%Y-%m-%d %H:%M")
    except (TypeError, ValueError, OSError):
        return str(value or "")[:16]


def _text(content) -> str:
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        parts = [c.get("text", "") if isinstance(c, dict) else str(c) for c in content]
        return " ".join(p for p in parts if p)
    if isinstance(content, dict):
        return _text(content.get("text") or content.get("content") or "")
    return ""


def from_sqlite(path: Path):
    con = sqlite3.connect(f"file:{path}?mode=ro", uri=True)
    tables = [r[0] for r in con.execute("select name from sqlite_master where type='table'")]
    for t in tables:
        cols = [r[1] for r in con.execute(f"pragma table_info('{t}')")]
        if "role" in cols and "content" in cols:
            tcol = "timestamp" if "timestamp" in cols else "NULL"
            for role, content, ts in con.execute(f"select role, content, {tcol} from '{t}'"):
                yield role, content or "", _ts(ts)
    con.close()


def _walk_json(obj):
    if isinstance(obj, dict):
        role = obj.get("role") or obj.get("type") or (obj.get("message") or {}).get("role")
        content = obj.get("content", (obj.get("message") or {}).get("content"))
        if role and content is not None:
            yield str(role), _text(content), _ts(obj.get("timestamp") or obj.get("created_at"))
        for v in obj.values():
            if isinstance(v, (dict, list)):
                yield from _walk_json(v)
    elif isinstance(obj, list):
        for v in obj:
            yield from _walk_json(v)


def from_json(path: Path):
    text = path.read_text(encoding="utf-8", errors="ignore")
    if path.suffix == ".jsonl":
        for line in text.splitlines():
            try:
                yield from _walk_json(json.loads(line))
            except json.JSONDecodeError:
                continue
    else:
        try:
            yield from _walk_json(json.loads(text))
        except json.JSONDecodeError:
            return


def from_text(path: Path):
    for para in re.split(r"\n\s*\n", path.read_text(encoding="utf-8", errors="ignore")):
        yield "unknown", para, ""


def iter_files(targets):
    for t in targets:
        p = Path(t).expanduser()
        if p.is_file():
            yield p
        elif p.is_dir():
            yield from (f for f in p.rglob("*") if f.is_file() and f.suffix.lower() in EXTS)


def messages(path: Path):
    suf = path.suffix.lower()
    try:
        if suf in {".db", ".sqlite", ".sqlite3"}:
            yield from from_sqlite(path)
        elif suf in {".jsonl", ".json"}:
            yield from from_json(path)
        else:
            yield from from_text(path)
    except (sqlite3.Error, OSError) as exc:
        print(f"aviso: {path}: {exc}")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("targets", nargs="+")
    ap.add_argument("--out", default="correcoes.md")
    ap.add_argument("--extra-regex", action="append", default=[])
    ap.add_argument("--max", type=int, default=400)
    ap.add_argument("--chars", type=int, default=500, help="tamanho máximo do trecho")
    args = ap.parse_args()

    user_re = re.compile("|".join(USER_PATTERNS + args.extra_regex), re.I)
    agent_re = re.compile("|".join(AGENT_PATTERNS), re.I)
    hits, seen = [], set()
    for f in iter_files(args.targets):
        for role, content, ts in messages(f):
            role = (role or "").lower()
            text = " ".join(content.split())
            if not text or len(text) > 4000:  # ignora dumps de ferramenta
                continue
            if role in ROLE_USER or role == "unknown":
                m = user_re.search(text)
                kind = "usuário"
            elif role in ROLE_AGENT:
                m = agent_re.search(text)
                kind = "agente"
            else:
                continue
            if not m:
                continue
            key = text[:120]
            if key in seen:
                continue
            seen.add(key)
            hits.append((ts, kind, f.name, m.group(0), text[: args.chars]))
            if len(hits) >= args.max:
                break
        if len(hits) >= args.max:
            break

    hits.sort(key=lambda h: h[0])
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    lines = [f"# Correções mineradas ({len(hits)} trechos)\n"]
    for ts, kind, src, gatilho, text in hits:
        lines.append(f"- **{ts or 's/ data'}** · {kind} · `{src}` · gatilho «{gatilho}»\n  > {text}\n")
    out.write_text("\n".join(lines), encoding="utf-8")
    users = sum(1 for h in hits if h[1] == "usuário")
    print(f"{len(hits)} trechos ({users} do usuário, {len(hits) - users} do agente) -> {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
