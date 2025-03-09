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
def adicionar_item():
    st.subheader("Adicionar Item ao Cardápio")
    nome = st.text_input("Nome do Item", key="nome_item")
    descricao = st.text_area("Descrição", key="descricao_item")
    preco = st.number_input("Preço", min_value=0.0, format="%.2f", key="preco_item")
    imagem = st.file_uploader("Envie uma imagem", type=["jpg", "jpeg", "png"], key="imagem_item")
    estoque = st.number_input("Estoque", min_value=0, key="estoque_item")
    
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT id_categoria, nome FROM Categoria")
    categorias = cursor.fetchall()
    conn.close()
    
    categoria_id = st.selectbox("Categoria", [categoria[0] for categoria in categorias], format_func=lambda x: next(categoria[1] for categoria in categorias if categoria[0] == x), key="categoria_item")
    
    if st.button("Adicionar Item"):
        if imagem is not None:
            if not os.path.exists("images"):
                os.makedirs("images")
            imagem_path = os.path.join("images", imagem.name)
            with open(imagem_path, "wb") as f:
                f.write(imagem.getbuffer())
        else:
            imagem_path = ""
        
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Produto (nome, descricao, preco, imagem, estoque, id_categoria) VALUES (?, ?, ?, ?, ?, ?)", (nome, descricao, preco, imagem_path, estoque, categoria_id))
        conn.commit()
        conn.close()
        st.success("Item adicionado com sucesso!")
        # Limpar o formulário
        st.session_state["nome_item"] = ""
        st.session_state["descricao_item"] = ""
        st.session_state["preco_item"] = 0.0
        st.session_state["imagem_item"] = None
        st.session_state["estoque_item"] = 0
        st.session_state["categoria_item"] = None
        # Atualizar a exibição do cardápio
        exibir_cardapio()

# Edita um item do cardápio.
def editar_item():
    st.subheader("Editar Item do Cardápio")
    conn = conectar()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM Produto")
    cardapio = cursor.fetchall()
    item_id = st.selectbox("Selecione o Item", [item[0] for item in cardapio])
    item = next(item for item in cardapio if item[0] == item_id)
    
    nome = st.text_input("Nome do Item", value=item[1], key="nome_item_editar")
    descricao = st.text_area("Descrição", value=item[2], key="descricao_item_editar")
    preco = st.number_input("Preço", min_value=0.0, format="%.2f", value=item[3], key="preco_item_editar")
    imagem = st.file_uploader("Envie uma nova imagem", type=["jpg", "jpeg", "png"], key="imagem_item_editar")
    estoque = st.number_input("Estoque", min_value=0, value=item[5], key="estoque_item_editar")
    
    cursor.execute("SELECT id_categoria, nome FROM Categoria")
    categorias = cursor.fetchall()
    categoria_id = st.selectbox("Categoria", [categoria[0] for categoria in categorias], index=[categoria[0] for categoria in categorias].index(item[6]), format_func=lambda x: next(categoria[1] for categoria in categorias if categoria[0] == x), key="categoria_item_editar")
    
    if st.button("Salvar Alterações"):
        if imagem is not None:
            if not os.path.exists("images"):
                os.makedirs("images")
            imagem_path = os.path.join("images", imagem.name)
            with open(imagem_path, "wb") as f:
                f.write(imagem.getbuffer())
        else:
            imagem_path = item[4]
        
        cursor.execute("UPDATE Produto SET nome = ?, descricao = ?, preco = ?, imagem = ?, estoque = ?, id_categoria = ? WHERE id_produto = ?", (nome, descricao, preco, imagem_path, estoque, categoria_id, item_id))
        conn.commit()
        conn.close()
        st.success("Item atualizado com sucesso!")
        # Atualizar a exibição do cardápio
        exibir_cardapio()

# Remove um item do cardápio.
def remover_item():
    st.subheader("Remover Item do Cardápio")
    conn = conectar()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM Produto")
    cardapio = cursor.fetchall()
    item_id = st.selectbox("Selecione o Item", [item[0] for item in cardapio])
    
    if st.button("Remover"):
        cursor.execute("DELETE FROM Produto WHERE id_produto = ?", (item_id,))
        conn.commit()
        conn.close()
        st.success("Item removido com sucesso!")
        # Atualizar a exibição do cardápio
        exibir_cardapio()
