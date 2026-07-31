# Atlas Interface

Interface mínima de chat para comunicação com o Atlas.

## Executar

1. Iniciar API:

```bash
uvicorn api.main:app --host 0.0.0.0 --port 8000
```

2. Servir interface:

```bash
python -m http.server 3000
```

3. Acessar:

```
http://localhost:3000
```

Para celular na mesma rede:

```
http://IP_DO_COMPUTADOR:3000
```

A interface envia mensagens para `/chat` da API Atlas.
