import streamlit as st
import pandas as pd
import sqlite3
from app.db import conectar
import os

# Exibe as categorias atuais.
def exibir_categorias():
    st.subheader("Categorias Atuais")
    conn = conectar()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM Categoria")
    categorias = cursor.fetchall()
    
    df = pd.DataFrame(categorias, columns=["id_categoria", "nome", "descricao"])
    st.table(df)
    
    conn.close()

# Adiciona uma categoria ao cardápio.
def adicionar_categoria():
    st.subheader("Adicionar Categoria ao Cardápio")
    nome = st.text_input("Nome da Categoria", key="nome_categoria")
    descricao = st.text_area("Descrição", key="descricao_categoria")
    
    if st.button("Adicionar Categoria"):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Categoria (nome, descricao) VALUES (?, ?)", (nome, descricao))
        conn.commit()
        conn.close()
        st.success("Categoria adicionada com sucesso!")
        # Limpar o formulário
        st.session_state["nome_categoria"] = ""
        st.session_state["descricao_categoria"] = ""

# Edita uma categoria do cardápio.
def editar_categoria():
    st.subheader("Editar Categoria do Cardápio")
    conn = conectar()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM Categoria")
    categorias = cursor.fetchall()
    categoria_id = st.selectbox("Selecione a Categoria", [categoria[0] for categoria in categorias])
    categoria = next(categoria for categoria in categorias if categoria[0] == categoria_id)
    
    nome = st.text_input("Nome da Categoria", value=categoria[1], key="nome_categoria_editar")
    descricao = st.text_area("Descrição", value=categoria[2], key="descricao_categoria_editar")
    
    if st.button("Salvar Alterações"):
        cursor.execute("UPDATE Categoria SET nome = ?, descricao = ? WHERE id_categoria = ?", (nome, descricao, categoria_id))
        conn.commit()
        conn.close()
        st.success("Categoria atualizada com sucesso!")

# Remove uma categoria do cardápio.
def remover_categoria():
    st.subheader("Remover Categoria do Cardápio")
    conn = conectar()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM Categoria")
    categorias = cursor.fetchall()
    categoria_id = st.selectbox("Selecione a Categoria", [categoria[0] for categoria in categorias])
    
    if st.button("Remover"):
        cursor.execute("DELETE FROM Categoria WHERE id_categoria = ?", (categoria_id,))
        conn.commit()
        conn.close()
        st.success("Categoria removida com sucesso!")

# Exibe o cardápio atual.
def exibir_cardapio():
    st.subheader("Cardápio Atual")
    conn = conectar()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM Produto")
    cardapio = cursor.fetchall()
    
    df = pd.DataFrame(cardapio, columns=["id_produto", "nome", "descricao", "preco", "imagem", "estoque", "id_categoria"])
    st.table(df)
    
    conn.close()

# Adiciona um item ao cardápio.
def adicionar_item(nome, descricao, preco, imagem_path, estoque, categoria_id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Produto (nome, descricao, preco, imagem, estoque, id_categoria) VALUES (?, ?, ?, ?, ?, ?)", (nome, descricao, preco, imagem_path, estoque, categoria_id))
    conn.commit()
    conn.close()
    st.success("Item adicionado com sucesso!")
    # Atualizar a exibição do cardápio
    exibir_cardapio()

# Edita um item do cardápio.
def editar_item(item_id, nome, descricao, preco, imagem_path, estoque, categoria_id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("UPDATE Produto SET nome = ?, descricao = ?, preco = ?, imagem = ?, estoque = ?, id_categoria = ? WHERE id_produto = ?", (nome, descricao, preco, imagem_path, estoque, categoria_id, item_id))
    conn.commit()
    conn.close()
    st.success("Item atualizado com sucesso!")
    # Atualizar a exibição do cardápio
    exibir_cardapio()

# Remove um item do cardápio.
def remover_item(item_id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Produto WHERE id_produto = ?", (item_id,))
    conn.commit()
    conn.close()
    st.success("Item removido com sucesso!")
    # Atualizar a exibição do cardápio
    exibir_cardapio()
