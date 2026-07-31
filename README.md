# Atlas

Sistema Atlas — Chief of Staff Digital.

Este repositório contém a arquitetura, documentação, memória e implementações do ecossistema Atlas.

## Atlas Core v0.1

Núcleo executável modular com memória persistente, gateway de IA e runtime desacoplado.

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

Use o arquivo `.env.example` como referência.

### Execução

Instalar dependências:

```bash
pip install -r requirements.txt
```

Executar localmente:

```bash
uvicorn api.main:app --host 0.0.0.0 --port 8000
```

Em ambiente cloud, o comando é definido pelo `Procfile`.

## Testes da API

### Health check

```bash
curl http://localhost:8000/health
```

Resposta esperada:

```json
{
  "status": "online",
  "version": "0.1.0"
}
```

### Chat

```bash
curl -X POST http://localhost:8000/chat \
-H "Content-Type: application/json" \
-d '{"message":"Olá Atlas"}'
```

## Execução local

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
uvicorn api.main:app
```

Documentação automática:

```
http://localhost:8000/docs
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
- API desacoplada do runtime.
