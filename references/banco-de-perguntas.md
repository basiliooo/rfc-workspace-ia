# Banco de perguntas

Use como cardápio, não como questionário fixo:
- pule o que a mineração já respondeu;
- adapte as opções à realidade do usuário;
- **coloque a opção recomendada primeiro** e explique em 1 linha por que ela é a recomendada.

Faça rodadas de até 5 perguntas.

## 1. Autonomia — agir ou perguntar
- **Mudança reversível em algo que está rodando** (rotina, config, prompt de outro bot):
  - agir com backup + verificação + aviso com rollback *(recomendado)*;
  - pedir antes.
- **Instalar ferramentas/pacotes:**
  - livre se isolado, pedir se global ou se exigir conta *(recomendado)*;
  - sempre pedir;
  - livre.
- **Bot encontra algo quebrado que ninguém pediu:**
  - corrige se reversível e avisa; senão alerta *(recomendado)*;
  - só avisa.
- **Criar/melhorar skills e prompts:** livre com log *(recomendado)* | pedir.
- **Criar agente novo:** o orquestrador propõe, com aprovação *(recomendado)* | livre.
- **Apagar arquivos:**
  - duplicata/lixo livre com log, o resto pede *(recomendado)*;
  - nunca apagar, só arquivar.
- **Conectar conta (OAuth/API):**
  - o bot inicia depois de um pedido formal que lista as permissões *(recomendado)*;
  - o usuário faz sozinho.
- **Diagnóstico pronto e correção autorizada:**
  - aplica na mesma resposta *(recomendado)*;
  - mostra o plano primeiro.

## 2. Aprovação
- **O que vale como aprovação:**
  - palavras-chave (“aprovo/pode/autorizo”) em resposta ao pedido *(recomendado)*;
  - qualquer resposta positiva.
- **Validade:** só aquele escopo, sem prazo *(recomendado)* | expira em X horas.
- **Formato:** botões aprovo/não/ajustar *(recomendado)* | texto.
- **Pedido sem resposta:** lembrar todo dia no relatório *(recomendado)* | lembrar 1 vez | não lembrar.
- **Perguntas no meio do trabalho:**
  - só as rápidas, em 1 linha + botões *(recomendado)*;
  - nunca, decide sozinho.

## 3. Comunicação
- **Idioma com o usuário / entre bots / no código:**
  - sugestão: idioma do usuário para pessoas e entre bots, inglês para identificadores de código.
- **Tamanho:**
  - conciso + explicativo, sempre com o porquê *(recomendado)*;
  - mínimo possível;
  - detalhado.
- **Limite por canal** (ex.: Telegram ≤ 10 linhas + link para nota detalhada).
- **Persona/tom:** em quais canais? Fora deles, profissional direto?
- **Nível técnico:**
  - analogia para não-programador *(recomendado se o usuário não for dev)*;
  - técnico completo.
- **Fontes da web:** sempre com link *(recomendado)* | só se pedir.
- **Áudio:** em todos os canais | só no celular | nunca.
- **Voz que o usuário manda e falha na transcrição:**
  - tentar outro transcritor sozinho *(recomendado)*;
  - avisar logo.

## 4. Orquestração e equipe
- **Quem orquestra:** um agente orquestrador fixo *(recomendado)* | quem receber o pedido.
- **Dois bots podem fazer a mesma coisa:**
  - o orquestrador escolhe pela especialidade e explica *(recomendado)*;
  - perguntar.
- **Pedido feito ao bot errado:** repassa sozinho e avisa *(recomendado)* | recusa e orienta.
- **Revisão:** o orquestrador revisa tudo antes de chegar ao usuário *(recomendado)* | só o crítico.
- **Paralelismo:** sem limite | máximo N simultâneos.
- **Tarefa parada há X h:** o orquestrador avisa e reatribui *(recomendado)* | só avisa.
- **Orquestrador fora do ar:** outro agente assume provisoriamente e avisa *(recomendado)* | tudo para.
- **Bot travado:** N abordagens diferentes, depois explica o bloqueio *(recomendado: 3)*.
- **Falha de modelo/limite:** troca sozinho, avisa só se todos falharem *(recomendado)* | avisa sempre.
- **Mudar prompt/config de outro bot:** pode, avisando o que mudou e por quê *(recomendado)* | só o orquestrador.

## 5. Notificações
- **Horário de silêncio:** ex.: 23h–8h, exceto crítico, com acumulado mandado de manhã *(recomendado)* | nenhum.
- **O que é crítico:**
  - falha que para entrega a cliente;
  - cliente/lead respondeu;
  - risco de dinheiro/conta;
  - segurança.
- **Relatório diário:** horário? Mensagens separadas ou única?
- **Sugestões proativas:** a qualquer momento | só no relatório diário.
- **Fim de semana:** igual | só crítico.
- **Lembretes pessoais** (prazos, contas, tarefas paradas há +N dias): sim | não.
- **Parada de emergência:** comando `/parar` + `/retomar` *(recomendado)*.
- **Comando `status`:** o que cada bot está fazendo, em até 10 linhas.

## 6. Rotinas agendadas
- **Log:** sempre, em log próprio de rotinas; o log diário recebe só entregas e falhas *(recomendado)*.
- **Nada novo:** silêncio *(recomendado)* | “nada novo”.
- **Falha:** 1 retentativa, depois alerta *(recomendado)* | alerta imediato.
- **Onde entregar:** resumo no chat + detalhe nas notas *(recomendado)* | e-mail | só notas.

## 7. Loops autônomos (trabalho noturno)
- **Pedido amplo** (“melhora tudo”): escolher 3–5 prioridades e explicar *(recomendado)* | fazer tudo.
- **Relatório:** horário + canal; seção “o que não funcionou” obrigatória.
- **Limite de gasto:** sem limite | teto por noite.

## 8. Notas / segundo cérebro
- **Antes de trabalhar:** quais arquivos de status ler?
- **Atualizar notas do projeto:** a cada mudança *(recomendado)* | só no fim da sessão.
- **Log diário:** formato do título, fuso, 1 arquivo por dia (nunca duplicar).
- **Organização:** livre para mover/renomear/apagar duplicatas com log *(recomendado)* | só sugerir.
- **Trabalho abandonado:** arquivar com motivo *(recomendado)* | apagar.
- **Link/vídeo/PDF sem instrução:**
  - estudar → 5 bullets + “vale usar?” + nota *(recomendado)*;
  - perguntar o que fazer.
- **Print sem texto:**
  - analisar e agir (bug → corrige; referência → salva) *(recomendado)*;
  - perguntar.
- **Fonte da verdade:** código no Git; bots/rotinas no servidor; notas sincronizadas?
- **Dados pessoais de clientes:**
  - só no CRM, e nas notas só resumo *(recomendado)*;
  - podem ficar nas notas.
- **Memória dos bots:**
  - só o orquestrador grava preferências do usuário;
  - cada bot grava, e a RFC vence.
- **Faxina de skills/prompts:** mensal pelo orquestrador | nunca.

## 9. Código e design (se houver)
- **Git:** commit/push em branch + preview livres, produção com aprovação *(recomendado)*.
- **Antes do push:** testes + gates de qualidade obrigatórios *(recomendado)*.
- **Idioma:** commits/comentários na língua do usuário, identificadores em inglês.
- **RFC antes de codar:** todo projeto | só os grandes.
- **Projeto novo:** estrutura nas notas + repo + RFC de escopo *(recomendado)*.
- **UI:** partir de um design system/DESIGN.md; checagem de “cara de IA” antes de mostrar.
- **Entrega visual:** prints desktop + mobile *(recomendado)*.
- **Previews para clientes:** link privado, nunca indexado *(recomendado)*.
- **Entregas em arquivo:** anexadas no chat + salvas na pasta do projeto *(recomendado)*.

## 10. Ações externas
- **Publicar em rede social:**
  - nunca sem aprovação;
  - automático se seguir formato + calendário aprovados, com teto diário *(recomendado se houver calendário)*.
- **Prospecção:**
  - 1ª mensagem automática com template aprovado, com teto diário;
  - follow-ups e respostas passam pelo usuário *(recomendado)*.
- **Templates:** aprovados pelo usuário; mudança = nova aprovação *(recomendado)*.
- **Lead/cliente respondeu:**
  - avisar na hora, mesmo no silêncio, com rascunho pronto *(recomendado)*.
- **Atendente (bot que fala com clientes):**
  - o que nunca pode dizer (preço, prazo, fechamento?);
  - como se identifica.
  - ⚠️ Se o usuário pedir que o bot **negue ser IA** quando alguém pergunta sinceramente, **discorde** e ofereça alternativas, por exemplo: não negar + chamar o humano; ou “sou o assistente de X”.
- **E-mail/agenda do usuário:** resumir e alertar, nunca responder sem ok *(recomendado)*.
- **Clientes ativos:** rascunhos de atualização para aprovação *(recomendado)* | não mexer.
- **Conteúdo com IA:** rótulo de IA conforme a política da plataforma *(recomendado)*. Se o usuário recusar, registre como **risco aceito**.
- **Imagem com o rosto do usuário:** só prompt | LoRA/fotos reais permitidos.

## 11. Dinheiro
- **Gasto com modelos/APIs:** sem limite | teto mensal.
- **Proposta/orçamento/cobrança:** bot gera rascunho, enviar/receber só com ok *(recomendado)*.
- **Preço de serviço:** o orquestrador propõe uma faixa com dados, o usuário decide *(recomendado)*.

## 12. Crescimento
- **Descoberta diária** (tendências, ferramentas, referências): top N com o porquê | não.
- **Ideias de renda:** 1 por semana com esforço estimado | não.
- **Prioridade entre projetos:** o orquestrador decide por impacto em dinheiro e explica | o usuário decide.
- **Ferramenta/repo enviado:** avaliar duplicação → veredito → instalar isolado se valer *(recomendado)*.
- **Entregas criativas:** 2–3 variações *(recomendado)* | 1.

## 13. Governança da própria RFC
- **Versionar:** sim, com mudança de regra = Decision Log + aviso *(recomendado)*.
- **Instruções contraditórias em momentos diferentes:** segue a mais recente e avisa *(recomendado)*.
- **Discordância:** o bot discorda com argumento e segue a decisão final *(recomendado)* | só obedece.
- **Métrica:** o orquestrador mede semanalmente as correções e as regras que falharam *(recomendado)*.
- **Correção nova:** regra fixa ou só desta vez? Perguntar quando não for óbvio.

## 14. Backup e continuidade
- **Backup do servidor/notas:** prioridade agora | depois.
- **Retomar sessão de outro canal:** buscar e resumir em 3 linhas *(recomendado)*.
