# AI Gateway Implementation v0.1

## Objetivo

O AI Gateway é a camada de abstração responsável por conectar o Atlas Core aos modelos de inteligência artificial externos.

Seu objetivo é impedir que o núcleo do Atlas dependa diretamente de um fornecedor específico de IA.

O Atlas Core deve conversar apenas com o AI Gateway, permitindo troca de modelos, expansão para modelos locais e controle centralizado.

---

# Arquitetura

Fluxo principal:

```
Atlas Core
    ↓
AI Gateway
    ↓
Provider Adapter
    ↓
Modelo IA
```

## Responsabilidades

### Atlas Core

Responsável por:

- interpretar solicitações;
- organizar contexto;
- consultar memória;
- enviar instruções ao Gateway.

Não deve conhecer detalhes do fornecedor de IA.

---

### AI Gateway

Responsável por:

- receber solicitações do Atlas Core;
- selecionar provider;
- aplicar configurações;
- controlar fallback;
- padronizar respostas;
- registrar operações futuras.

---

### Provider Adapter

Cada modelo possui um adaptador próprio.

Exemplo:

```
providers/
├── qwen.py
├── deepseek.py
└── openai.py
```

O adapter transforma a interface comum do Atlas em chamadas específicas de cada API.

---

# Interface Comum

Todos os providers devem implementar uma função padronizada:

```python
generate_response()
```

Entrada esperada:

- mensagem do usuário;
- contexto atual;
- memórias recuperadas;
- instruções permanentes do Atlas.

Exemplo conceitual:

```python
{
  "message": "solicitação do usuário",
  "context": "contexto da conversa",
  "memory": "memórias relevantes",
  "instructions": "regras do Atlas"
}
```

Saída esperada:

- resposta gerada;
- metadados do modelo;
- informações de uso.

---

# Estrutura planejada

```
core/
└── ai_gateway/

providers/
├── qwen.py
├── deepseek.py
└── openai.py
```

---

# Primeiro Provedor

## Prioridade inicial

O primeiro provider deve priorizar modelos com API compatível e baixo custo.

Opções avaliadas:

- Qwen;
- DeepSeek.

## Critérios de escolha

- disponibilidade de API;
- custo operacional;
- qualidade de resposta;
- facilidade de substituição;
- compatibilidade com arquitetura do Gateway.

O provider inicial deve ser implementado sem alterar o Atlas Core.

---

# Configuração

As credenciais devem existir apenas em variáveis de ambiente.

Exemplos:

```env
AI_PROVIDER=qwen
AI_API_KEY=
AI_BASE_URL=
AI_MODEL=
```

Nenhuma chave deve ser armazenada no código.

---

# Fallback de Modelos

O Gateway deve permitir futuramente:

1. tentar provider principal;
2. identificar falha;
3. trocar para provider secundário;
4. retornar resposta padronizada.

Exemplo:

```
Qwen
 ↓ falha
DeepSeek
 ↓ falha
OpenAI
```

---

# Tratamento de Erros

O AI Gateway deve controlar:

- falha de autenticação;
- indisponibilidade do modelo;
- limite de requisições;
- tempo excedido;
- respostas inválidas.

Os erros devem ser convertidos para formato interno do Atlas.

---

# Independência de Modelo

O Atlas Core não deve depender de:

- nomes específicos de modelos;
- SDKs exclusivos;
- formatos individuais de resposta.

Toda dependência externa deve ficar isolada nos adapters.

---

# Preparação Futura

O AI Gateway deve permitir evolução para:

- múltiplos modelos simultâneos;
- modelos locais;
- roteamento inteligente;
- controle de custo;
- avaliação de respostas;
- auditoria;
- seleção automática de modelo.

---

# Escopo desta fase

Implementar posteriormente:

- estrutura do Gateway;
- primeiro adapter;
- conexão com modelo real;
- testes de geração.

Não faz parte desta etapa:

- interface do usuário;
- agentes subordinados;
- automações.

Objetivo final:

Criar o cérebro de comunicação do Atlas independente do fornecedor de IA.
