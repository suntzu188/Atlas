# Atlas Advanced Memory System

## Visão geral

O Advanced Memory System representa a evolução do Memory Core básico do Atlas para uma arquitetura cognitiva capaz de armazenar, recuperar, consolidar e evoluir conhecimento ao longo do tempo.

O objetivo é transformar dados isolados em contexto útil para agentes de IA, permitindo continuidade, aprendizado e tomada de decisão baseada em histórico.

---

# Arquitetura de memória

O sistema é dividido em camadas complementares:

```
Memory Core
│
├── Short-Term Memory
├── Episodic Memory
├── Permanent Memory
└── Knowledge Base
```

Cada camada possui regras próprias de armazenamento, relevância, retenção e recuperação.

---

# Memória de curto prazo

A memória de curto prazo mantém informações temporárias relacionadas à interação atual.

Características:

- contexto da conversa ativa;
- mensagens recentes;
- estado temporário do agente;
- informações necessárias para completar uma tarefa imediata.

A memória de curto prazo possui ciclo de vida limitado e pode ser descartada após a conclusão do objetivo.

---

# Memória episódica

A memória episódica armazena eventos e experiências relevantes.

Exemplos:

- conversas anteriores;
- decisões tomadas;
- resultados de tarefas;
- interações importantes com usuários.

Cada episódio deve conter:

- origem;
- data;
- contexto;
- participantes;
- resultado;
- importância.

---

# Memória permanente

A memória permanente contém informações consideradas estáveis e reutilizáveis.

Exemplos:

- preferências confirmadas;
- regras de operação;
- conhecimento validado;
- padrões identificados.

Memórias permanentes devem possuir controle de qualidade e versionamento.

---

# Base de conhecimento

A Knowledge Base representa o conhecimento estruturado do Atlas.

Pode incluir:

- documentos;
- dados técnicos;
- especificações de projetos;
- decisões arquiteturais;
- informações externas aprovadas.

---

# Sistema de embeddings

O sistema de embeddings permite transformar informações em representações vetoriais para busca semântica.

## Geração

Fluxo:

1. Receber conteúdo.
2. Normalizar texto.
3. Enviar para modelo de embedding.
4. Gerar vetor semântico.
5. Armazenar junto aos metadados.

## Armazenamento

Os embeddings devem ser armazenados associados ao conteúdo original:

- memória;
- conversa;
- documento;
- conhecimento.

## Atualização

Embeddings devem ser regenerados quando:

- o conteúdo mudar;
- o modelo de embedding for atualizado;
- houver melhoria de qualidade.

## Remoção

Memórias removidas devem ter seus embeddings removidos ou invalidados.

## Versionamento

Cada embedding deve registrar:

- modelo utilizado;
- versão;
- data de criação;
- origem do conteúdo.

---

# Integração Supabase

O Advanced Memory System utiliza Supabase como camada persistente.

Estruturas principais:

## memories

Armazena memórias do sistema.

Campos esperados:

- id;
- tipo;
- conteúdo;
- importância;
- embedding;
- metadata;
- timestamps.

## conversations

Armazena históricos de interação.

## documents

Armazena documentos processados pelo sistema.

## knowledge_base

Armazena conhecimento consolidado.

## pgvector

Extensão utilizada para armazenamento e comparação de embeddings vetoriais.

---

# Busca semântica

O processo de recuperação segue:

1. Gerar embedding da consulta do usuário.
2. Comparar vetor da consulta com memórias existentes.
3. Calcular similaridade.
4. Ordenar resultados por relevância.
5. Recuperar contexto necessário.

A busca deve priorizar:

- relevância semântica;
- importância da memória;
- atualidade;
- confiança.

---

# Pipeline cognitivo

```
Usuário
↓
Análise
↓
Busca de memória
↓
Recuperação de contexto
↓
AI Gateway
↓
Resposta
↓
Avaliação
↓
Nova memória
```

O pipeline permite que cada interação gere aprendizado contínuo.

---

# Regras de memória

## Salvamento automático

O Atlas pode identificar informações relevantes automaticamente e propor armazenamento.

## Aprovação do CEO

Memórias críticas ou permanentes devem passar por aprovação antes da consolidação definitiva.

## Níveis de importância

Sugestão de classificação:

- baixa;
- média;
- alta;
- crítica.

## Expiração

Memórias temporárias podem possuir prazo de validade.

Após expiração:

- remover;
- arquivar;
- consolidar.

## Consolidação

Memórias relacionadas podem ser agrupadas para criar conhecimento mais completo.

---

# Preparação futura

O sistema deve suportar:

## Memória por agente

Cada agente poderá possuir memória especializada.

## Memória compartilhada controlada

Agentes poderão compartilhar conhecimento com regras de permissão.

## Múltiplos projetos

O Atlas poderá operar diferentes ambientes isolados.

## Histórico de decisões

Decisões importantes deverão formar uma trilha de raciocínio e evolução do sistema.

---

# Status

Documento referente ao Atlas Core v0.1.

Define a base arquitetural para evolução do Memory Core em um sistema cognitivo persistente.