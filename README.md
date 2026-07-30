# Atlas

Sistema Atlas — Chief of Staff Digital.

Este repositório contém a arquitetura, documentação, memória e futuras implementações do ecossistema Atlas.

## Atlas Core v0.1

Primeiro esqueleto executável do núcleo do Atlas.

## Execução local

1. Criar ambiente virtual:

```bash
python -m venv venv
```

2. Ativar ambiente:

Linux/macOS:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

3. Instalar dependências:

```bash
pip install -r requirements.txt
```

4. Configurar variáveis de ambiente:

Copiar `.env.example` para `.env` e preencher conforme necessário.

5. Iniciar servidor:

```bash
python main.py
```

API disponível em:

```
http://localhost:8000
```

Documentação automática:

```
http://localhost:8000/docs
```

## Estado atual

Implementado:

- estrutura modular;
- FastAPI;
- configuração inicial;
- sistema básico de rotas;
- dependências.

Ainda não implementado:

- AI Gateway;
- memória;
- agentes;
- automações.
