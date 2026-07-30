# AI Gateway

## Visão Geral

O AI Gateway é a camada de abstração responsável por conectar o Atlas a diferentes modelos de inteligência artificial sem criar dependência de um fornecedor específico.

O Atlas Core não deve conhecer detalhes de implementação dos modelos utilizados. Toda comunicação com modelos de IA deve passar pelo AI Gateway.

Arquitetura:

Usuário
↓
Atlas Core
↓
AI Gateway
↓
Provedores de IA
↓
Modelos

## Objetivos

- Permitir troca de modelos sem alterar o Atlas Core.
- Reduzir dependência de fornecedores.
- Permitir uso de modelos pagos, gratuitos ou locais.
- Centralizar configuração, autenticação e monitoramento.
- Escolher o modelo mais adequado para cada tarefa.

## Arquitetura do Componente

O AI Gateway possui as seguintes camadas:

### Interface de Comunicação

Define um contrato único para o Atlas Core enviar solicitações.

Exemplo de informações recebidas:

- tipo de tarefa;
- contexto;
- prioridade;
- nível de raciocínio necessário;
- restrições.

### Gerenciador de Provedores

Responsável por administrar conexões com diferentes plataformas:

- Qwen;
- DeepSeek;
- modelos locais;
- OpenAI futuramente.

Cada provedor possui uma implementação independente.

### Seletor de Modelo

Escolhe automaticamente o modelo adequado baseado em:

- custo;
- velocidade;
- qualidade;
- privacidade;
- disponibilidade.

### Adaptadores

Cada modelo possui um adaptador responsável por converter o padrão interno do Atlas para o formato exigido pelo provedor.

O Atlas Core nunca acessa adaptadores diretamente.

## Troca de Modelos sem Alterar o Atlas Core

O Atlas Core utiliza apenas a interface do AI Gateway.

Exemplo:

Antes:

Atlas Core → AI Gateway → Qwen

Depois:

Atlas Core → AI Gateway → DeepSeek

Nenhuma alteração no Atlas Core é necessária.

A troca acontece apenas na configuração do provedor ativo.

## Gerenciamento de Provedores

Cada provedor deve possuir:

- nome;
- endpoint;
- autenticação;
- modelos disponíveis;
- limites de uso;
- custo estimado;
- nível de confiança.

Exemplo conceitual:

```
provider:
  name: qwen
  enabled: true
  models:
    - qwen-max
```

## Configuração de APIs

As credenciais nunca devem ficar dentro do código.

Configurações devem utilizar variáveis de ambiente:

```
AI_PROVIDER=qwen
AI_API_KEY=secret
AI_MODEL=qwen-max
```

O AI Gateway é responsável por carregar e validar essas configurações.

## Fallback entre Modelos

O sistema deve possuir estratégias de fallback.

Exemplo:

1. Modelo principal indisponível.
2. AI Gateway verifica modelos alternativos.
3. Seleciona próximo modelo compatível.
4. Registra o evento.

Exemplo:

```
Qwen
 ↓ falha
DeepSeek
 ↓ falha
Modelo local
```

## Seleção de Modelo por Tipo de Tarefa

O modelo utilizado pode variar conforme o objetivo.

### Conversação Geral

Prioridade:
- velocidade;
- baixo custo.

### Análise Complexa

Prioridade:
- raciocínio;
- qualidade.

### Dados Sensíveis

Prioridade:
- privacidade;
- execução local.

### Automações

Prioridade:
- estabilidade;
- latência.

## Independência de Fornecedor

O Atlas deve permanecer independente de qualquer empresa de inteligência artificial.

Modelos podem ser substituídos.

Provedores podem ser removidos.

Tecnologias podem evoluir.

A identidade do Atlas permanece no núcleo:

- missão;
- memória;
- arquitetura;
- agentes;
- relacionamento com o proprietário.

O AI Gateway garante que a inteligência utilizada pelo Atlas seja substituível sem comprometer o sistema.