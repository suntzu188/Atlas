# Atlas Memory System v0.1

## Objetivo

O Memory System é o sistema cognitivo responsável por permitir que o Atlas mantenha continuidade, contexto e aprendizado ao longo do tempo. Ele separa informações temporárias de conhecimento consolidado e controla o que pode ser persistido automaticamente.

## Arquitetura Cognitiva

Fluxo principal:

Usuário
↓
Atlas Core
↓
Busca de memória relevante
↓
AI Gateway
↓
Modelo de IA
↓
Resposta
↓
Atualização e consolidação da memória

## Camadas de Memória

### Memória de Curto Prazo

Armazena o contexto da interação atual.

Características:
- baixa persistência;
- usada durante uma sessão;
- expira após período definido;
- otimizada para contexto imediato.

Exemplos:
- mensagens recentes;
- objetivos da conversa atual;
- informações temporárias.

### Memória Episódica

Representa eventos e experiências específicas.

Exemplos:
- decisões tomadas;
- projetos executados;
- interações importantes;
- resultados de tarefas.

Possui data, contexto, participantes e relevância associada.

### Memória Permanente

Armazena informações estáveis necessárias para a identidade e funcionamento do Atlas.

Exemplos:
- preferências aprovadas pelo CEO;
- regras permanentes;
- princípios de operação;
- configurações do sistema.

Alterações críticas exigem aprovação do CEO.

### Base de Conhecimento

Camada destinada a conhecimento externo e documentos.

Inclui:
- documentos importados;
- informações técnicas;
- conhecimento de domínio;
- referências utilizadas pelos agentes.

## Integração com Supabase

O Supabase atua como camada persistente inicial do Atlas.

Componentes utilizados:

- PostgreSQL para dados estruturados;
- pgvector para armazenamento vetorial;
- autenticação e controle de acesso;
- auditoria de alterações.

## Estrutura de Dados Principal

### memories

Armazena memórias do Atlas.

Campos conceituais:
- id;
- user_id;
- tipo de memória;
- conteúdo;
- embedding;
- relevância;
- origem;
- data de criação;
- status de aprovação.

### conversations

Mantém histórico de interações.

Campos conceituais:
- id;
- user_id;
- mensagens;
- contexto;
- timestamps;
- referências recuperadas.

### documents

Armazena documentos utilizados pelo sistema.

Campos conceituais:
- id;
- origem;
- conteúdo;
- metadados;
- embeddings;
- versão.

### knowledge_base

Representa conhecimento consolidado.

Campos conceituais:
- id;
- categoria;
- conteúdo;
- fonte;
- embeddings;
- confiabilidade.

## Embeddings e Busca Semântica

O Atlas utiliza embeddings para transformar informações em representações vetoriais.

O mecanismo permite:

- encontrar informações semanticamente relacionadas;
- recuperar contexto relevante;
- reduzir dependência de palavras exatas.

Tecnologia inicial:

- PostgreSQL + pgvector.

## Recuperação de Contexto

Antes de responder, o Atlas executa:

1. análise da intenção do usuário;
2. busca vetorial por memórias relacionadas;
3. ranking de relevância;
4. filtragem por permissão;
5. envio do contexto selecionado ao AI Gateway.

## Ranking de Relevância

Critérios:

- similaridade semântica;
- recência;
- importância definida pelo usuário;
- frequência de uso;
- nível de confiança.

## Políticas de Retenção

Tipos temporários:
- conversas descartáveis;
- contexto operacional;
- dados de execução.

Tipos permanentes:
- identidade do Atlas;
- regras aprovadas;
- preferências importantes;
- decisões estratégicas.

## Atualização e Consolidação

O Atlas pode consolidar memórias quando:

- uma informação aparece repetidamente;
- uma decisão possui impacto futuro;
- o usuário solicita armazenamento;
- uma tarefa gera conhecimento reutilizável.

Memórias antigas podem ser:

- arquivadas;
- resumidas;
- mescladas;
- removidas conforme política.

## Salvamento Automático

Pode salvar automaticamente:

- contexto necessário para concluir uma tarefa ativa;
- histórico operacional;
- resultados de agentes;
- informações explicitamente marcadas como reutilizáveis.

## Aprovação do CEO

Exige aprovação:

- alteração de identidade do Atlas;
- novas regras permanentes;
- preferências pessoais sensíveis;
- mudanças de autonomia;
- decisões estratégicas.

## Segurança

Toda memória deve possuir:

- origem rastreável;
- controle de acesso;
- histórico de alterações;
- possibilidade de exclusão.

O Memory System é uma camada independente do modelo de IA utilizado pelo AI Gateway.
