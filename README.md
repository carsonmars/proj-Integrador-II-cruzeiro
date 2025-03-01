# Cafeteria Sabor & Aroma

Este projeto é uma aplicação para gerenciar o cardápio e pedidos de uma cafeteria.

## Estrutura do Projeto

```
cafeteria_project/
├── app/
│   ├── __init__.py
│   ├── menu.py
│   ├── order.py
├── tests/
│   ├── test_menu.py
│   ├── test_order.py
├── requirements.txt
├── README.md
├── setup.py
└── main.py
```

## Configuração do Ambiente

1. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

## Execução

Para iniciar a aplicação, execute:

```bash
streamlit run main.py
```

## Funcionalidades

### Tela Inicial

- Tela inicial com botões de navegação para as principais funcionalidades: “Fazer Pedido” e “Cardápio”.

### Tela de Cardápio

- Galeria para exibir os itens do cardápio.
- Conexão com uma fonte de dados (arquivo CSV) contendo os itens do cardápio, com colunas para nome, descrição, preço e imagem.

### Tela de Pedido

- Campos para o cliente selecionar itens do cardápio e quantidade.
- Botão para confirmar o pedido, que salva os dados em um arquivo CSV.
- Funcionalidades de edição e remoção de pedidos.

## Integração e Testes

### Integração com Fontes de Dados

- Conexão do aplicativo a um arquivo CSV para armazenar informações de pedidos e cardápio.

### Testes Automatizados

- Testes automatizados para garantir a qualidade do código.
- Utilização do framework `unittest` para escrever testes unitários.
- Testes de integração para adicionar, editar e remover pedidos.

## Publicação

### Hospedagem

- Utilização de uma plataforma gratuita como Streamlit Community Cloud para hospedar a aplicação.
- Conexão do repositório GitHub e configuração do pipeline de CI/CD para implantar automaticamente a aplicação.

### Compartilhamento

- Compartilhamento do link da aplicação com os usuários relevantes e configuração das permissões de acesso.

## Boas Práticas de Desenvolvimento de Software

1. **Código Limpo e Simples**: Mantenha o código fácil de ler e entender. Utilize nomes de variáveis e funções descritivos e evite complexidade desnecessária.
2. **Testes Contínuos**: Implemente testes automatizados para garantir a qualidade do código.
3. **Consistência no Código**: Adote um guia de estilo consistente, como o PEP 8, para manter a uniformidade no código.
4. **Revisão de Código**: Realize revisões de código regularmente para identificar problemas e compartilhar conhecimento entre a equipe.
5. **Documentação**: Mantenha a documentação atualizada e detalhada. Inclua comentários no código e crie documentação externa para explicar a arquitetura e o funcionamento do sistema.

## Testes da Solução

Escolha 5 colegas para testar sua aplicação, disponibilize o *link* de acesso ou os recursos necessários para que testem como usuários. Preencha a Tabela a seguir com as informações obtidas:

| **Nome:** | **Data do teste:** | **O que testou e funcionou:** | **O que testou e não funcionou -- O que deve ser corrigido:** | **Funcionalidade não testada (faltou ou não foi implementada):** |
| --------------- | ------------------------ | ----------------------------------- | -------------------------------------------------------------------- | ------------------------------------------------------------------------ |
|                 |                          |                                     |                                                                      |                                                                          |
|                 |                          |                                     |                                                                      |                                                                          |
|                 |                          |                                     |                                                                      |                                                                          |
|                 |                          |                                     |                                                                      |                                                                          |
|                 |                          |                                     |                                                                      |                                                                          |

## Vídeo da Solução Atualizada

Após levantar os *feedbacks* e executar as correções necessárias e pertinentes, grave um vídeo de **até 5 minutos** apresentando as modificações realizadas no sistema.

| ***Link* para o vídeo** |
| -------------------------------- |
|                                  |

## Codificação

Na Tabela a seguir insira as informações referentes ao desenvolvimento do código do processo.

| **Linguagem**                                                                           | **Python**                    |
| --------------------------------------------------------------------------------------------- | ----------------------------------- |
| **Banco de Dados**                                                                      | **CSV**                       |
| **Hospedagem**                                                                          | **Streamlit Community Cloud** |
| **Plataforma**                                                                          | **Streamlit**                 |
| **Modo de Codificação**                                                               | \(x\) *Tradicional*               |
| ***Link* do repositório no [GitHub](https://github.com/login) com os códigos abertos** | Desenvolvido na plataforma GitHub.  |
| ***Link* da solução em funcionamento**                                              |                                     |
| ***Link* do vídeo narrado (no mínimo 5 min)**                                       |                                     |
