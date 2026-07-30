# Atlas Implementation Plan v0.1

## Objetivo

Este documento define o plano técnico para transformar a arquitetura v0.1 do Atlas em software funcional.

O objetivo é criar a primeira implementação executável do Atlas Core mantendo os princípios definidos na constituição e documentação arquitetural.

---

# 1. Objetivo do Atlas Core v0.1

A primeira versão funcional do Atlas Core deve ser capaz de executar o ciclo executivo básico:

Usuário
↓
API Atlas
↓
Atlas Core
↓
Consulta de memória
↓
AI Gateway
↓
Modelo de IA
↓
Resposta ao usuário
↓
Persistência de histórico
↓
Atualização de memória quando necessário

## Capacidades obrigatórias

O Atlas Core v0.1 deve:

- receber mensagens do usuário;
- identificar contexto da solicitação;
- consultar memória relevante;
- enviar contexto ao AI Gateway;
- receber resposta do modelo;
- retornar resposta ao usuário;
- salvar histórico de conversas;
- atualizar memória conforme regras definidas.

A primeira versão não terá autonomia total ou criação dinâmica avançada de agentes.

---

# 2. Stack Inicial

## Linguagem

Recomendação inicial:

**Python**

Motivos:

- ecossistema maduro de IA;
- integração ampla com modelos;
- bibliotecas de processamento de linguagem;
- facilidade para prototipação e evolução.

## Framework Backend

Recomendação:

**FastAPI**

Responsabilidades:

- criação da API HTTP;
- validação de dados;
- endpoints do Atlas;
- integração com serviços internos.

## Estrutura de API

Endpoints iniciais esperados:

- receber mensagem;
- consultar status do Atlas;
- acessar histórico;
- gerenciar configurações futuras.

## Banco de Dados

Implementação inicial:

**Supabase PostgreSQL**

Uso:

- armazenamento persistente;
- autenticação;
- tabelas do Atlas;
- pgvector para embeddings.

## AI Gateway

O Atlas Core não deve conversar diretamente com modelos.

Toda comunicação deve passar pelo AI Gateway para permitir:

- troca de fornecedores;
- múltiplos modelos;
- modelos locais futuros;
- controle de custos;
- auditoria.

## Variáveis de Ambiente

Configurações sensíveis devem ficar fora do código.

Exemplos:

- credenciais Supabase;
- chaves de modelos;
- configurações de ambiente;
- parâmetros de execução.

## Deploy Futuro

A arquitetura deve permitir implantação em:

- servidores cloud;
- containers;
- plataformas serverless;
- ambientes privados.

---

# 3. Estrutura Inicial do Código

Estrutura planejada:

```
api/
core/
agents/
memory/
database/
config/
```

## api/

Responsável pela camada externa.

Inclui:

- rotas HTTP;
- validação;
- entrada e saída de dados.

## core/

Núcleo executivo do Atlas.

Responsável por:

- ciclo de decisão;
- coordenação dos módulos;
- execução do fluxo principal.

## agents/

Sistema hierárquico de agentes.

Inicialmente:

- estrutura base;
- registro de agentes;
- permissões.

## memory/

Sistema cognitivo.

Responsável por:

- busca de memórias;
- embeddings;
- consolidação;
- recuperação de contexto.

## database/

Camada de persistência.

Responsável por:

- conexão Supabase;
- modelos de dados;
- operações CRUD.

## config/

Configurações globais.

Inclui:

- ambiente;
- parâmetros;
- carregamento seguro de variáveis.

---

# 4. Ordem de Desenvolvimento

## Fase 1 — API Básica

Objetivo:

Criar a primeira interface de comunicação.

Implementar:

- servidor backend;
- endpoint de mensagens;
- validação básica;
- resposta simulada.

Resultado esperado:

Usuário consegue enviar mensagem para o Atlas.

---

## Fase 2 — Conexão Supabase

Objetivo:

Adicionar persistência.

Implementar:

- conexão com banco;
- modelos iniciais;
- armazenamento de usuários;
- armazenamento de conversas.

Resultado esperado:

O Atlas mantém histórico.

---

## Fase 3 — Integração AI Gateway

Objetivo:

Conectar o núcleo executivo aos modelos de IA.

Implementar:

- camada de abstração;
- envio de prompts;
- recebimento de respostas;
- controle de fornecedor.

Resultado esperado:

Atlas responde usando um modelo real.

---

## Fase 4 — Sistema de Memória

Objetivo:

Adicionar capacidade cognitiva persistente.

Implementar:

- armazenamento de memórias;
- embeddings;
- busca semântica;
- recuperação contextual;
- consolidação inicial.

Resultado esperado:

Atlas consegue utilizar experiências anteriores.

---

## Fase 5 — Primeira Interface

Objetivo:

Criar uma interface simples para interação.

Possibilidades:

- web interface;
- chat básico;
- painel administrativo inicial.

Resultado esperado:

Usuário interage sem utilizar diretamente a API.

---

## Fase 6 — Primeiro Agente Subordinado

Objetivo:

Validar a arquitetura hierárquica.

Criar:

- primeiro agente especialista;
- comunicação Atlas → agente;
- controle de permissões.

Resultado esperado:

Atlas consegue delegar uma tarefa simples.

---

# 5. Critérios de Sucesso do Atlas Core v0.1

A primeira versão será considerada funcional quando:

## Comunicação

- usuário consegue enviar mensagens;
- Atlas retorna respostas válidas.

## Memória

- conversas são persistidas;
- contexto relevante pode ser recuperado;
- informações aprovadas podem ser armazenadas.

## Inteligência

- respostas utilizam AI Gateway;
- modelo pode ser substituído sem alterar o núcleo.

## Arquitetura

- módulos possuem responsabilidades separadas;
- banco está desacoplado da lógica principal;
- memória funciona como camada independente.

## Segurança

- credenciais não ficam no código;
- acesso possui controle básico;
- operações importantes possuem histórico.

## Evolução

O Atlas Core v0.1 deve servir como fundação para:

- agentes subordinados;
- maior autonomia;
- múltiplos projetos;
- aprendizado contínuo;
- evolução do ecossistema Atlas.

---

## Estado esperado após v0.1

O Atlas será um assistente executivo funcional com memória persistente básica, arquitetura modular e preparado para expansão futura.