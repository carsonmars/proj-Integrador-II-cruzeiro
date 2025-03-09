# Cafeteria Sabor & Aroma

Este projeto é uma prova de conceito (PoC) de uma aplicação para gerenciar o cardápio e pedidos de uma cafeteria, incluindo um painel administrativo para gestão da plataforma.

## Estrutura do Projeto

```
cafeteria_project/
├── app/
│   ├── __init__.py
│   ├── db.py
│   ├── menu.py
│   ├── order.py
│   ├── crud.py
├── tests/
│   ├── test_menu.py
│   ├── test_order.py
│   ├── test_crud.py
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
- Conexão com uma fonte de dados (banco de dados SQLite) contendo os itens do cardápio, com colunas para nome, descrição, preço e imagem.

### Tela de Pedido

- Campos para o cliente selecionar itens do cardápio e quantidade.
- Botão para confirmar o pedido, que salva os dados no banco de dados SQLite.
- Funcionalidades de edição e remoção de pedidos.

## Integração e Testes

### Integração com Fontes de Dados

- Conexão do aplicativo a um banco de dados SQLite para armazenar informações de pedidos e cardápio.

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
| **Banco de Dados**                                                                      | **SQLite**                    |
| **Hospedagem**                                                                          | **Streamlit Community Cloud** |
| **Plataforma**                                                                          | **Streamlit**                 |
| **Modo de Codificação**                                                               | \(x\) *Tradicional*               |
| ***Link* do repositório no [GitHub](https://github.com/login) com os códigos abertos** | Desenvolvido na plataforma GitHub.  |
| ***Link* da solução em funcionamento**                                              |                                     |
| ***Link* do vídeo narrado (no mínimo 5 min)**                                       |                                     |

### Passos para Codificação

1. **Configuração do Banco de Dados**:

   - Crie o módulo `db.py` para gerenciar o banco de dados SQLite.
   - Implemente a função `conectar` para conectar ao banco de dados.
   - Implemente a função `criar_tabelas` para criar as tabelas necessárias.
2. **Módulo de Pedidos**:

   - Crie o módulo `order.py` para gerenciar os pedidos.
   - Implemente as funções `adicionar_ao_carrinho`, `exibir_carrinho`, `limpar_carrinho` e `finalizar_compra`.
3. **Módulo de Menu**:

   - Crie o módulo `menu.py` para exibir o cardápio.
   - Implemente a função `exibir_menu_como_cards`.
4. **Módulo de CRUD**:

   - Crie o módulo `crud.py` para gerenciar o cardápio.
   - Implemente as funções `adicionar_item`, `editar_item`, `remover_item` e `exibir_cardapio`.
5. **Arquivo Principal**:

   - Crie o arquivo `main.py` para iniciar a aplicação.
   - Implemente a lógica para exibir o menu do cliente e o menu do funcionário.
6. **Testes Automatizados**:

   - Crie os arquivos de teste `test_menu.py`, `test_order.py` e `test_crud.py` no diretório `tests`.
   - Implemente os testes para garantir a qualidade do código.
7. **Execução e Publicação**:

   - Execute a aplicação localmente para garantir que tudo está funcionando corretamente.
   - Publique a aplicação no Streamlit Community Cloud.
   - Compartilhe o link da aplicação com os usuários relevantes.

## Modelo Entidade-Relacionamento (MER)

O Modelo Entidade-Relacionamento (MER) a seguir fornece uma visão clara da estrutura do banco de dados utilizado na aplicação:

```
+----------------+       +----------------+       +----------------+       +----------------+
|    Cliente     |       |    Pedido      |       |    Produto     |       |   Categoria    |
+----------------+       +----------------+       +----------------+       +----------------+
| id_cliente (PK)|<------| id_pedido (PK) |       | id_produto (PK)|<------| id_categoria(PK)|
| nome           |       | data_pedido    |       | nome           |       | nome           |
| cpf            |       | status         |       | descricao      |       | descricao      |
| email          |       | id_cliente (FK)|       | preco          |       +----------------+
| telefone       |       +----------------+       | imagem         |
+----------------+                |               | estoque        |
                                  |               | id_categoria(FK)|
                                  |               +----------------+
                                  |
                                  |
                                  v
                          +----------------+
                          |  ItemPedido    |
                          +----------------+
                          | id_item (PK)   |
                          | id_pedido (FK) |
                          | id_produto (FK)|
                          | quantidade     |
                          | preco_unitario |
                          +----------------+
```

**Explicação do MER**

* **Categoria** : Organiza os produtos em seções do cardápio, como "Cafés", "Sobremesas", "Salgados", etc.
* **Produto** : Agora inclui uma chave estrangeira (`id_categoria`) para associar cada produto a uma categoria.
* **Cardápio** : O cardápio pode ser gerado dinamicamente a partir das categorias e produtos, exibindo os itens organizados por seção.

---

### SQL para Criação das Tabelas (Atualizado)

Aqui está o SQL atualizado para incluir a tabela `Categoria`:

```sql
-- Tabela Categoria
CREATE TABLE Categoria (
    id_categoria INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    descricao TEXT
);

-- Tabela Produto (Atualizada)
CREATE TABLE Produto (
    id_produto INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    descricao TEXT,
    preco REAL NOT NULL,
    imagem TEXT,
    estoque INTEGER NOT NULL,
    id_categoria INTEGER,
    FOREIGN KEY (id_categoria) REFERENCES Categoria(id_categoria)
);

-- Tabela Cliente
CREATE TABLE Cliente (
    id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    cpf TEXT UNIQUE,
    email TEXT NOT NULL,
    telefone TEXT
);

-- Tabela Pedido
CREATE TABLE Pedido (
    id_pedido INTEGER PRIMARY KEY AUTOINCREMENT,
    data_pedido TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status TEXT NOT NULL,
    id_cliente INTEGER,
    FOREIGN KEY (id_cliente) REFERENCES Cliente(id_cliente)
);

-- Tabela ItemPedido
CREATE TABLE ItemPedido (
    id_item INTEGER PRIMARY KEY AUTOINCREMENT,
    id_pedido INTEGER,
    id_produto INTEGER,
    quantidade INTEGER NOT NULL,
    preco_unitario REAL NOT NULL,
    FOREIGN KEY (id_pedido) REFERENCES Pedido(id_pedido),
    FOREIGN KEY (id_produto) REFERENCES Produto(id_produto)
);
```

### Como o Cardápio Funciona no Sistema

1. **Cadastro de Categorias** :

* No painel administrativo, você pode cadastrar categorias como "Cafés", "Sobremesas", "Salgados", etc.
* Exemplo:

  ```sql
  INSERT INTO Categoria (nome, descricao) VALUES ('Cafés', 'Diversos tipos de café');
  INSERT INTO Categoria (nome, descricao) VALUES ('Sobremesas', 'Bolos, tortas e doces');
  ```

2. **Cadastro de Produtos** :

* Cada produto é cadastrado associado a uma categoria.
* Exemplo:

  ```sql
  INSERT INTO Produto (nome, descricao, preco, imagem, estoque, id_categoria)
  VALUES ('Café Expresso', 'Café forte e encorpado', 5.0, 'cafe_expresso.jpg', 100, 1);
  ```

3. **Exibição do Cardápio** :

* No frontend (Streamlit), o cardápio pode ser exibido organizado por categorias.
* Exemplo de consulta SQL para exibir o cardápio:

  ```sql
  SELECT Categoria.nome AS categoria, Produto.nome, Produto.descricao, Produto.preco, Produto.imagem
  FROM Produto
  JOIN Categoria ON Produto.id_categoria = Categoria.id_categoria
  ORDER BY Categoria.nome, Produto.nome;
  ```

---

### Benefícios dessa Estrutura

* **Organização** : Os produtos são organizados por categorias, facilitando a navegação no cardápio.
* **Flexibilidade** : Você pode adicionar ou remover categorias e produtos sem afetar a estrutura do banco de dados.
* **Histórico** : O preço unitário no `ItemPedido` garante que o histórico de pedidos seja preciso, mesmo que o preço do produto mude no futuro.
