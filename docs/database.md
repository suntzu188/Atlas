# Atlas Database Architecture v0.1

## Objetivo

Definir a arquitetura de dados do Atlas, garantindo persistência segura, escalabilidade, suporte a múltiplos agentes e independência do provedor de banco de dados.

## Princípios da Arquitetura de Dados

- separação clara entre dados temporários e permanentes;
- controle de acesso por usuário e agente;
- histórico completo de decisões importantes;
- independência da implementação de armazenamento;
- preparação para múltiplos projetos e agentes;
- auditoria de operações críticas.

## Camadas de Dados

### Memória

Dados usados para continuidade cognitiva.

Inclui:
- memórias de curto prazo;
- memórias episódicas;
- memórias permanentes.

Tabela principal:
- memories.

### Conhecimento

Informações externas utilizadas pelo Atlas.

Inclui:
- documentos;
- bases de conhecimento;
- informações vetorizadas.

Tabelas principais:
- documents;
- knowledge_base.

### Dados Permanentes

Dados fundamentais para identidade e operação:

- usuários;
- agentes;
- projetos;
- configurações.

### Dados Temporários

Dados de execução:

- sessões;
- filas de tarefas;
- estados intermediários.

## Independência do Provedor

A arquitetura deve permitir migração futura entre bancos diferentes.

O Atlas não deve depender de funcionalidades exclusivas de um único fornecedor.

O Supabase é a implementação inicial utilizando PostgreSQL.

## Banco Inicial: Supabase PostgreSQL

Recursos utilizados:

- PostgreSQL;
- pgvector;
- autenticação;
- políticas de acesso;
- logs de auditoria.

## Estrutura de Tabelas

# users

## Objetivo

Representa usuários do Atlas.

## Campos principais

- id;
- identidade;
- preferências;
- configurações;
- permissões.

## Relacionamentos

Um usuário possui:
- memórias;
- tarefas;
- projetos;
- conversas.

## Controle de acesso

Cada usuário acessa apenas seus dados autorizados.

## Ciclo de vida

Criado no cadastro e mantido enquanto existir vínculo com o Atlas.

---

# memories

## Objetivo

Armazenar informações cognitivas persistentes.

## Campos principais

- id;
- user_id;
- categoria;
- conteúdo;
- embedding;
- relevância;
- aprovação;
- timestamps.

## Relacionamentos

users → memories

## Controle de acesso

Protegido por usuário e nível de permissão.

## Ciclo de vida

Pode ser criada, consolidada, atualizada, arquivada ou removida.

---

# conversations

## Objetivo

Registrar interações entre usuário e Atlas.

## Campos principais

- id;
- user_id;
- mensagens;
- contexto;
- data;
- metadados.

## Relacionamentos

users → conversations

## Controle de acesso

Privado por usuário.

## Ciclo de vida

Pode possuir retenção limitada conforme política de memória.

---

# projects

## Objetivo

Representar objetivos e iniciativas acompanhadas pelo Atlas.

## Campos principais

- id;
- user_id;
- nome;
- descrição;
- status;
- metas.

## Relacionamentos

users → projects

projects → tasks

## Controle de acesso

Limitado ao proprietário e agentes autorizados.

## Ciclo de vida

Criado, executado, finalizado e arquivado.

---

# tasks

## Objetivo

Representar ações executáveis.

## Campos principais

- id;
- project_id;
- user_id;
- responsável;
- status;
- prioridade;
- prazo.

## Relacionamentos

users → tasks

projects → tasks

## Controle de acesso

Gerenciado por permissões do usuário e agentes.

## Ciclo de vida

Criada, atribuída, executada, concluída ou cancelada.

---

# agents

## Objetivo

Registrar agentes subordinados do ecossistema Atlas.

## Campos principais

- id;
- nome;
- função;
- agente superior;
- permissões;
- status.

## Relacionamentos

agents → agents

Permite hierarquia de agentes.

## Controle de acesso

Cada agente opera dentro das permissões definidas.

## Ciclo de vida

Criado, ativado, atualizado, desativado.

---

# documents

## Objetivo

Armazenar documentos utilizados pelo sistema.

## Campos principais

- id;
- origem;
- conteúdo;
- metadados;
- embedding;
- versão.

## Relacionamentos

documents → knowledge_base

## Controle de acesso

Aplicado conforme origem e proprietário.

## Ciclo de vida

Importação, processamento, atualização e arquivamento.

---

# knowledge_base

## Objetivo

Armazenar conhecimento consolidado.

## Campos principais

- id;
- documento relacionado;
- categoria;
- conteúdo;
- embedding;
- confiança.

## Relacionamentos

documents → knowledge_base

## Controle de acesso

Definido pela origem do conhecimento.

## Ciclo de vida

Atualizado conforme novos dados e validações.

## pgvector e Embeddings

Embeddings serão utilizados para:

- busca semântica;
- recuperação contextual;
- associação entre conhecimentos;
- suporte a agentes especializados.

## Persistência e Auditoria

Operações relevantes devem registrar:

- quem executou;
- quando ocorreu;
- qual dado foi alterado;
- motivo da alteração.

## Preparação para Múltiplos Agentes

A arquitetura suporta:

- agentes especialistas;
- agentes gestores;
- delegação hierárquica;
- memória compartilhada controlada;
- isolamento de permissões.

## Preparação para Múltiplos Projetos

Cada projeto possui:

- tarefas próprias;
- contexto próprio;
- histórico de decisões;
- agentes participantes.

## Histórico de Decisões

Decisões estratégicas devem ser persistidas para permitir:

- análise futura;
- auditoria;
- melhoria contínua do Atlas.
