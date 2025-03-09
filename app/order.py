import streamlit as st
import pandas as pd
import sqlite3
from app.db import conectar

# Exibe os pedidos existentes.
def exibir_pedidos():
    st.title("Gerenciar Pedidos")
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Pedido")
    pedidos = cursor.fetchall()
    df = pd.DataFrame(pedidos, columns=["id_pedido", "data_pedido", "status", "id_cliente"])
    st.dataframe(df)
    conn.close()

# Adiciona um novo pedido.
def adicionar_pedido():
    st.subheader("Adicionar Pedido")
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT id_produto, nome FROM Produto")
    produtos = cursor.fetchall()
    conn.close()
    
    produto_id = st.selectbox("Selecione um item", [produto[0] for produto in produtos], format_func=lambda x: next(produto[1] for produto in produtos if produto[0] == x))
    quantidade = st.number_input("Quantidade", min_value=1, max_value=10)
    
    if st.button("Adicionar ao Carrinho"):
        adicionar_ao_carrinho(produto_id, quantidade)
        st.write(f"{quantidade}x {produto_id} adicionado ao carrinho.")

# Edita um pedido existente.
def editar_pedido():
    st.subheader("Editar Pedido")
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Pedido")
    pedidos = cursor.fetchall()
    conn.close()
    
    pedido_id = st.selectbox("ID do Pedido", [pedido[0] for pedido in pedidos])
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT id_produto, nome FROM Produto")
    produtos = cursor.fetchall()
    conn.close()
    
    novo_produto_id = st.selectbox("Novo Item", [produto[0] for produto in produtos], format_func=lambda x: next(produto[1] for produto in produtos if produto[0] == x))
    nova_quantidade = st.number_input("Nova Quantidade", min_value=1, max_value=10)
    
    if st.button("Salvar Alterações"):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("UPDATE ItemPedido SET id_produto = ?, quantidade = ? WHERE id_pedido = ?", (novo_produto_id, nova_quantidade, pedido_id))
        conn.commit()
        conn.close()
        st.write("Pedido atualizado com sucesso.")

# Remove um pedido existente.
def remover_pedido():
    st.subheader("Remover Pedido")
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Pedido")
    pedidos = cursor.fetchall()
    conn.close()
    
    pedido_id_remover = st.selectbox("ID do Pedido para Remover", [pedido[0] for pedido in pedidos])
    
    if st.button("Remover Pedido"):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Pedido WHERE id_pedido = ?", (pedido_id_remover,))
        cursor.execute("DELETE FROM ItemPedido WHERE id_pedido = ?", (pedido_id_remover,))
        conn.commit()
        conn.close()
        st.write("Pedido removido com sucesso.")

# Adiciona um item ao carrinho.
def adicionar_ao_carrinho(produto_id, quantidade):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT preco FROM Produto WHERE id_produto = ?", (produto_id,))
    preco_unitario = cursor.fetchone()[0]
    cursor.execute("INSERT INTO ItemPedido (id_produto, quantidade, preco_unitario) VALUES (?, ?, ?)", (produto_id, quantidade, preco_unitario))
    conn.commit()
    conn.close()

# Exibe o carrinho de compras.
def exibir_carrinho():
    st.subheader("Carrinho de Compras")
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT Produto.nome, ItemPedido.quantidade, ItemPedido.preco_unitario FROM ItemPedido JOIN Produto ON ItemPedido.id_produto = Produto.id_produto")
    itens = cursor.fetchall()
    df = pd.DataFrame(itens, columns=["Produto", "Quantidade", "Preço Unitário"])
    st.table(df)
    conn.close()

# Limpa o carrinho de compras.
def limpar_carrinho():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM ItemPedido")
    conn.commit()
    conn.close()

# Finaliza a compra.
def finalizar_compra():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Pedido (status) VALUES ('Finalizado')")
    pedido_id = cursor.lastrowid
    cursor.execute("UPDATE ItemPedido SET id_pedido = ? WHERE id_pedido IS NULL", (pedido_id,))
    conn.commit()
    conn.close()
    st.success("Compra finalizada com sucesso!")
