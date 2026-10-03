# Mineração de correções

Objetivo: achar as frases em que o usuário **corrigiu**, cobrou ou repetiu um pedido, e as frases em que o agente **pediu desculpas**. Isso vira a tabela C-xx da RFC e evita perguntar o que ele já disse.

## Onde procurar o histórico

| Agente | Fonte típica |
|---|---|
| Hermes Agent | `~/.hermes/state.db` e `~/.hermes/profiles/*/state.db` (SQLite, tabela `messages`, colunas `role`, `content`, `timestamp`) |
| Claude Code | `~/.claude/projects/**/*.jsonl` |
| Codex CLI | `~/.codex/sessions/**/*.jsonl` |
| Outros | exports `.json`/`.jsonl`/`.md`/`.txt` de conversas, logs de bots (Telegram/WhatsApp) |

Se não houver histórico, peça ao usuário que cole de 5 a 10 correções de que se lembra e siga em frente.

## Como rodar

```
terminal(command="python3 scripts/minerar_correcoes.py ~/.hermes/state.db ~/.claude/projects --out rfc-ws/correcoes.md")
```

- Aceita arquivos e pastas (busca recursiva por `.db`, `.sqlite`, `.jsonl`, `.json`, `.md`, `.txt`).
- `--extra-regex` adiciona padrões próprios, por exemplo gírias do usuário.
- `--max 400` limita o número de trechos.
- A saída é um markdown com fonte, data quando houver, papel e trecho.

## Como transformar em C-xx

1. Leia `correcoes.md` inteiro.
2. Agrupe as frases que reclamam da mesma coisa, por exemplo “cadê o áudio?” e “não chegou o áudio”.
3. Para cada grupo: frase mais representativa (literal), data/canal e **causa-raiz**. A causa-raiz é a regra que faltava, não o sintoma.
4. Priorize os grupos com 2 ou mais ocorrências: são as correções recorrentes que a RFC precisa matar primeiro.
5. Cada C-xx deve gerar pelo menos uma regra e um critério de aceite.

## Causas-raiz comuns (para reconhecer rápido)

- Status em vez de ação → falta a regra de autonomia (R-AUT).
- “Não entendi o que você fez” → relatório sem objetivo/porquê (R-COM).
- “Disse que funcionava e não funcionava” → falta a regra de evidência (R-DOD).
- Rotina “ok” sem entrega → “executou” tratado como “entregou” (R-DOD/R-ROT).
- Preferência que só um bot respeita → regra na memória de um agente só (R-GOV).
- Pedido repetido em vários dias → contexto não retomado (R-CTX).
- Arquivos duplicados/conflitos → vários escritores sem dono (R-MB).
