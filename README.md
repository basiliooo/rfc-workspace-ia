# rfc-workspace-ia

Skill que entrevista você e escreve **um contrato único de como seus agentes de IA devem trabalhar**. A skill funciona com qualquer agente (Hermes, Claude Code, Codex, Cursor).

O contrato cobre:
- formato das respostas;
- quando agir ou perguntar;
- aprovações;
- divisão de trabalho entre bots;
- rotinas e notificações;
- notas;
- publicações, mensagens a clientes e dinheiro;
- como cada correção sua vira regra.

O objetivo é parar de corrigir os bots várias vezes pela mesma coisa.

## Como funciona

1. **Minera o seu histórico.** `scripts/minerar_correcoes.py` lê conversas antigas em SQLite, JSONL, JSON ou MD e acha as frases em que você corrigiu o bot (“eu já te pedi”, “cadê”, “não era isso”…) e as vezes em que ele pediu desculpas. Assim você não precisa repetir o que já disse.
2. **Faz um rascunho** com o que já dá para deduzir.
3. **Faz a entrevista em rodadas** de até 5 perguntas. Cada pergunta vem com opções e uma recomendação, então você responde clicando. O banco tem mais de 80 perguntas em 14 áreas.
4. **Consolida a RFC.** Cada resposta vira uma regra com ID, e a RFC também traz o Decision Log, os riscos aceitos e os critérios de aceite.
5. **Aplica, depois que você aprovar.** Um núcleo comum de regras vai em todos os agentes, e são feitas a limpeza das memórias e o ajuste das rotinas.

## Instalação

**Hermes Agent**
```bash
git clone <url-deste-repo> ~/.hermes/skills/rfc-workspace-ia
```
Depois, numa sessão nova: *“quero criar o RFC do meu workspace de IA”*.

**Claude Code**
```bash
git clone <url-deste-repo> ~/.claude/skills/rfc-workspace-ia
```

**Outros agentes:** aponte o agente para o `SKILL.md` e peça para ele seguir o procedimento.

## Estrutura

```
SKILL.md                         procedimento (fases 0–5) e checklist
templates/RFC-workspace.md       esqueleto da RFC com as 17 áreas de regras
references/banco-de-perguntas.md perguntas com opções e recomendação
references/mineracao.md          onde achar o histórico e como virar C-xx
scripts/minerar_correcoes.py     minerador, só com biblioteca padrão do Python 3.9+
```

## Uso do minerador sozinho

```bash
python3 scripts/minerar_correcoes.py ~/.hermes/state.db ~/.claude/projects --out correcoes.md
```

## Origem

Esta skill foi extraída de um caso real. A RFC original saiu de 97 perguntas e virou cerca de 160 regras, que resolveram 12 correções recorrentes: “já era pra ter feito”, “cadê o áudio”, “disse que funcionava e não funcionava”, logs duplicados e outras. O conteúdo da RFC original é pessoal e não está aqui; só o método.

Licença MIT.
