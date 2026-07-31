# Atlas

Sistema Atlas — Chief of Staff Digital.

Este repositório contém a arquitetura, documentação, memória e implementações do ecossistema Atlas.

## Atlas Core v0.1

Núcleo executável modular com memória persistente, gateway de IA e runtime desacoplado.

## Atlas Runtime State

O Atlas separa o estado do servidor do estado cognitivo do agente.

### ONLINE

Indica que o serviço está disponível e respondendo requisições.

### State

Representa o estado operacional do agente:

- `active` — agente operacional;
- `idle` — aguardando configuração ou integração;
- `thinking` — reservado para processamento futuro.

### Mode

Representa a capacidade atual do runtime:

- `full` — integrações disponíveis e Atlas totalmente funcional;
- `degraded` — servidor online, porém com serviços externos indisponíveis.

O endpoint `/health` consulta o estado atual do runtime através do Atlas Core.

## Estrutura do projeto

- `api/` — camada FastAPI;
- `core/` — componentes centrais do Atlas;
- `memory/` — sistema de memória;
- `agents/` — agentes subordinados;
- `ai_gateway/` — abstração de provedores de IA;
- `bootstrap.py` — inicialização do runtime.

## Deploy cloud

### Variáveis de ambiente

Criar as seguintes variáveis no provedor cloud:

```env
SUPABASE_URL=
SUPABASE_KEY=
AI_PROVIDER=qwen
AI_API_KEY=
AI_MODEL=qwen-plus
AI_BASE_URL=
```

### Execução

```bash
pip install -r requirements.txt
uvicorn api.main:app --host 0.0.0.0 --port ${PORT:-8000}
```

## Testes da API

```bash
curl http://localhost:8000/health
```

Resposta:

```json
{
  "status": "online",
  "state": "active",
  "mode": "full",
  "version": "0.1.0"
}
```

## Estado atual

Implementado:

- FastAPI;
- AtlasOrchestrator;
- MemoryService;
- Memory Retrieval;
- Embeddings structure;
- Consolidation structure;
- AI Gateway;
- Qwen Provider Adapter;
- Bootstrap Runtime;
- Supabase Client Adapter;
- Runtime State Model;
- API desacoplada do runtime.
