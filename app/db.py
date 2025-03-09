import sqlite3

def conectar():
    return sqlite3.connect("cafeteria.db")

def criar_tabelas():
    conn = conectar()
    cursor = conn.cursor()
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Categoria (
        id_categoria INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        descricao TEXT
    )
    """)
    
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
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Cliente (
        id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        cpf TEXT UNIQUE,
        email TEXT NOT NULL,
        telefone TEXT
    )
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Pedido (
        id_pedido INTEGER PRIMARY KEY AUTOINCREMENT,
        data_pedido TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        status TEXT NOT NULL,
        id_cliente INTEGER,
        FOREIGN KEY (id_cliente) REFERENCES Cliente(id_cliente)
    )
    """)
    
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
