import sqlite3
import time

# Conecta ao banco de dados SQLite.
# Retorna uma conexão com o banco de dados.
def conectar():
    return sqlite3.connect("cafeteria.db")

# Cria as tabelas necessárias no banco de dados SQLite.
def criar_tabelas():
    tentativas = 5
    while tentativas > 0:
        try:
            conn = conectar()
            cursor = conn.cursor()
            
            # Cria a tabela Categoria
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS Categoria (
                id_categoria INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                descricao TEXT
            )
            """)
            
            # Cria a tabela Produto
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS Produto (
                id_produto INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                descricao TEXT,
                preco REAL NOT NULL,
                imagem TEXT,
                estoque INTEGER NOT NULL,
                id_categoria INTEGER,
                FOREIGN KEY (id_categoria) REFERENCES Categoria(id_categoria)
            )
            """)
            
            # Cria a tabela Cliente
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS Cliente (
                id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                cpf TEXT UNIQUE,
                email TEXT NOT NULL,
                telefone TEXT
            )
            """)
            
            # Cria a tabela Pedido
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS Pedido (
                id_pedido INTEGER PRIMARY KEY AUTOINCREMENT,
                data_pedido TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                status TEXT NOT NULL,
                id_cliente INTEGER,
                FOREIGN KEY (id_cliente) REFERENCES Cliente(id_cliente)
            )
            """)
            
            # Cria a tabela ItemPedido
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS ItemPedido (
                id_item INTEGER PRIMARY KEY AUTOINCREMENT,
                id_pedido INTEGER,
                id_produto INTEGER,
                quantidade INTEGER NOT NULL,
                preco_unitario REAL NOT NULL,
                FOREIGN KEY (id_pedido) REFERENCES Pedido(id_pedido),
                FOREIGN KEY (id_produto) REFERENCES Produto(id_produto)
            )
            """)
            
            conn.commit()
            conn.close()
            break
        except sqlite3.OperationalError as e:
            if "database is locked" in str(e):
                tentativas -= 1
                time.sleep(1)
            else:
                raise e
