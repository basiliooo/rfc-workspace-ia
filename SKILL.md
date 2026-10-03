---
name: rfc-workspace-ia
description: "Use when the user wants an operating contract for AI agents."
version: 1.0.0
author: Nicolas, Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [rfc, governance, agents, workflow, prompts, pt-br]
    related_skills: []
---

# RFC do Workspace de IA — contrato operacional dos seus bots

Esta skill entrevista o usuário e escreve **uma RFC única** que define como os agentes dele devem trabalhar:
- formato das respostas;
- quando agir sozinho e quando perguntar;
- aprovações;
- divisão de trabalho entre bots;
- rotinas e notificações;
- notas e memória;
- ações externas (publicar, enviar, cobrar);
- como cada correção do usuário vira regra.

O objetivo é parar de corrigir o mesmo comportamento várias vezes. Cada preferência vira uma regra com ID, numa fonte única que tem precedência sobre memória, prompts soltos e hábito.

A skill não implementa nada. Ela termina com a RFC aprovada e um backlog de aplicação. Funciona com qualquer agente (Hermes, Claude Code, Codex, Cursor), porque só precisa ler e escrever arquivos e fazer perguntas.

## When to Use

Use quando o usuário:
- diz que vive corrigindo os bots, quer “regras do meu workspace”, “contrato dos agentes”, “como meus bots devem funcionar” ou “padronizar os agentes”;
- tem 2 ou mais agentes, perfis ou rotinas agendadas com comportamentos que se contradizem;
- quer documentar preferências de output, autonomia e aprovação antes de dar mais autonomia aos bots.

**Don't use for:**
- RFC de uma feature ou produto (use uma skill de RFC de projeto);
- uma preferência isolada (grave direto na memória ou no arquivo de regras);
- configurar uma ferramenta específica.

## Princípios (não negociáveis)

1. **Evidência antes de perguntas.** Primeiro levante as correções reais que o usuário já fez (Fase 1). Pergunte só o que o histórico não responde.
2. **Toda pergunta tem opções e uma recomendação.** O usuário deve conseguir responder clicando. Coloque a opção recomendada primeiro e explique o porquê em 1 linha.
3. **Toda resposta vira uma regra com ID**, rastreável até a pergunta (`Q-xx`) ou correção (`C-xx`) que a originou.
4. **Toda tabela de regras tem a linha `default`.** O caso não coberto é a origem mais comum de “o bot fez besteira”.
5. **Discorde quando houver motivo.** Se o usuário pedir algo arriscado (enganar terceiros, violar regra de plataforma, apagar sem backup), argumente e ofereça alternativas. Se ele mantiver a decisão e ela for legal e ética, registre-a como **risco aceito**. Nunca escreva uma regra que mande o bot enganar ou prejudicar terceiros.
6. **Não perca respostas.** Grave cada rodada num arquivo de trabalho logo que ela chegar, antes de fazer a próxima pergunta.

## Procedure

### Fase 0 — Preparação
- Pergunte, ou descubra lendo os arquivos:
  - onde ficam as notas (Obsidian, Notion, pasta);
  - quais agentes e perfis existem;
  - quais canais são usados (Telegram, WhatsApp, Desktop, terminal);
  - quais rotinas agendadas existem;
  - idioma e fuso horário.
- Crie a pasta de trabalho `rfc-ws/` com `respostas.md` (vazio) e copie [templates/RFC-workspace.md](templates/RFC-workspace.md).
- **Pronto quando:** o inventário de agentes, canais, rotinas e locais de notas estiver escrito no topo de `respostas.md`.

### Fase 1 — Mineração de correções (evidência)
- Rode `scripts/minerar_correcoes.py` sobre o histórico disponível: banco SQLite de sessões, exports `.jsonl`/`.json`/`.md` ou logs. Veja [references/mineracao.md](references/mineracao.md).
- Leia os trechos encontrados e agrupe em **correções recorrentes** `C-01..C-NN`, com: frase do usuário, data/canal e causa-raiz.
- Leia também os arquivos de regras atuais (prompts de sistema, AGENTS.md, CLAUDE.md, memórias, configs de rotinas) e liste **contradições** entre eles.
- **Pronto quando:** existir uma tabela C-xx com pelo menos 1 evidência por linha (ou a nota “sem histórico disponível”) e a lista de contradições.

### Fase 2 — Rascunho v0.1
- Preencha o template com o que já é inferível: contexto (C-xx), glossário, papéis dos agentes e regras óbvias tiradas das correções.
- Tudo o que for incerto vira pergunta aberta na §11. Nada é inventado.
- **Pronto quando:** a RFC v0.1 estiver salva com estado `em-revisao` e a lista de perguntas abertas pronta.

### Fase 3 — Entrevista em rodadas (Grill Me)
- Use [references/banco-de-perguntas.md](references/banco-de-perguntas.md). Ele cobre 14 áreas e mais de 80 perguntas com opções.
- Pule o que a Fase 1 já respondeu e adapte as opções à realidade do usuário.
- Faça **rodadas de até 5 perguntas independentes** (ferramenta de perguntas com opções, ou lista numerada no chat).
- Ordem das rodadas: autonomia/aprovação → comunicação → orquestração → notificações → rotinas → notas → código → ações externas → dinheiro → crescimento.
- Depois de cada rodada:
  1. anexe as respostas a `respostas.md` no formato `Q-xx <resposta curta>`;
  2. se uma resposta abriu dúvida, crie a pergunta derivada `Q-xxb`;
  3. a cada ~4 rodadas, pergunte “mais uma rodada ou consolidar?”.
- Se o formulário expirar, **não assuma que o usuário desistiu**: reenvie as mesmas perguntas e ofereça a opção de responder pelo chat.
- **Pronto quando:** o usuário pedir para consolidar, ou quando todas as áreas do banco de perguntas tiverem pelo menos uma decisão.

### Fase 4 — Consolidação v0.2
- Releia `respostas.md` **inteiro**; ele é a fonte autoritativa. Não confie em respostas truncadas no transcript.
- Para cada resposta, escreva ou ajuste a regra na tabela da área, com a coluna `Q`.
- Respostas que substituem regras antigas devem dizer isso na própria regra (“substitui a regra X”).
- Preencha:
  - **Decision Log:** uma linha por Q;
  - **Riscos:** inclua os riscos aceitos pelo usuário;
  - **Critérios de aceite:** Given/When/Then, no mínimo 1 por área, priorizando as correções C-xx;
  - **Apêndice A** (onde aplicar cada grupo de regras);
  - **Apêndice B** (backlog: estado atual × RFC).
- **Pronto quando:**
  - todas as Q do arquivo aparecem no Decision Log;
  - todas as tabelas têm uma linha `default`;
  - a §11 diz “0 bloqueantes”;
  - o arquivo foi lido de volta após a gravação.

### Fase 5 — Aprovação e aplicação
- Mostre um resumo de no máximo 10 linhas: quantas regras, formatos e testes; o que você recusou e por quê; quais riscos foram aceitos.
- Peça aprovação explícita (“aprovo”). “ok” não vale.
- Depois da aprovação, gere o plano de aplicação a partir do Apêndice B:
  1. **Núcleo comum** de cerca de 30 linhas no prompt de sistema de **todos** os agentes. Ele aponta para a RFC e repete só as regras de comunicação, autonomia, evidência e correção.
  2. Remover das memórias e dos prompts as preferências duplicadas ou contraditórias, que passam a ser só ponteiros para a RFC.
  3. Ajustar rotinas (entrega, logs, horário de silêncio).
  4. Criar os comandos e formatos que ainda não existem.
- **Pronto quando:** a RFC estiver com `estado: aprovada` e o plano de aplicação tiver um dono e um critério de pronto para cada item.

## Pitfalls

- **Perguntar antes de minerar** faz o usuário repetir o que já disse 10 vezes; é exatamente o que ele quer evitar.
- **Perguntas abertas sem opções** cansam e geram respostas vagas. Sempre dê 2 a 4 opções, com a recomendada primeiro.
- **Consolidar de memória** perde respostas, porque o transcript trunca. Releia `respostas.md`.
- **Regras na memória de um agente só** não chegam aos outros. A RFC é a fonte, e o núcleo comum vai em todos.
- **Regras sem precedência** deixam o agente sem saber quem vence. A RFC deve definir: mensagem atual > RFC > regras do projeto > arquivo de agentes > skill > memória.
- **“Feito” sem evidência** foi a correção mais comum no caso original. Toda RFC precisa de regras de evidência (R-DOD).
- **Persona e tom** variam por canal. Pergunte em quais canais a persona vale.
- **RFC gigante que ninguém lê:** os agentes leem o núcleo comum; a RFC é a referência. Mantenha IDs estáveis para poder citá-los.

## Verification

- [ ] Tabela C-xx com evidência (ou “sem histórico”)
- [ ] `respostas.md` com todas as respostas, gravado rodada a rodada
- [ ] Toda regra tem ID, e as que vieram de respostas têm `Q`
- [ ] Toda tabela de regras tem uma linha `default`
- [ ] Decision Log cobre 100% das Q de `respostas.md` (confira com contagem, não de olho)
- [ ] Riscos aceitos e recusas registrados na §10
- [ ] Pelo menos 1 critério de aceite por área
- [ ] Usuário aprovou explicitamente; estado atualizado
