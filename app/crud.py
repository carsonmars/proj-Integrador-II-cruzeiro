import streamlit as st
import pandas as pd
import os

def adicionar_item(nome=None, descricao=None, preco=None, imagem=None):
    if not nome:
        st.subheader("Adicionar Item ao Cardápio")
        nome = st.text_input("Nome do Item")
        descricao = st.text_area("Descrição")
        preco = st.number_input("Preço", min_value=0.0, format="%.2f")
        imagem = st.file_uploader("Imagem do Item", type=["jpeg", "jpg", "png"])

    if st.button("Adicionar") or (nome and descricao and preco):
        df = pd.read_excel("cardapio.xlsx")
        novo_id = df["id"].max() + 1 if not df.empty else 1
        novo_item = pd.DataFrame({"id": [novo_id], "nome": [nome], "descricao": [descricao], "preco": [preco]})
        df = pd.concat([df, novo_item], ignore_index=True)
        df.to_excel("cardapio.xlsx", index=False)
        if imagem:
            with open(os.path.join("src", "images", "cardapio", f"{novo_id}.jpeg"), "wb") as f:
                f.write(imagem.getbuffer())
        st.success("Item adicionado com sucesso!")

def editar_item(item_id=None, nome=None, descricao=None, preco=None, imagem=None):
    if not item_id:
        st.subheader("Editar Item do Cardápio")
        df = pd.read_excel("cardapio.xlsx")
        item_id = st.selectbox("Selecione o Item", df["id"])
        item = df[df["id"] == item_id].iloc[0]
        nome = st.text_input("Nome do Item", value=item["nome"])
        descricao = st.text_area("Descrição", value=item["descricao"])
        preco = st.number_input("Preço", min_value=0.0, format="%.2f", value=item["preco"])
        imagem = st.file_uploader("Imagem do Item", type=["jpeg", "jpg", "png"])

    if st.button("Salvar Alterações") or (item_id and nome and descricao and preco):
        df = pd.read_excel("cardapio.xlsx")
        df.loc[df["id"] == item_id, ["nome", "descricao", "preco"]] = [nome, descricao, preco]
        df.to_excel("cardapio.xlsx", index=False)
        if imagem:
            with open(os.path.join("src", "images", "cardapio", f"{item_id}.jpeg"), "wb") as f:
                f.write(imagem.getbuffer())
        st.success("Item atualizado com sucesso!")

def remover_item(item_id=None):
    if not item_id:
        st.subheader("Remover Item do Cardápio")
        df = pd.read_excel("cardapio.xlsx")
        item_id = st.selectbox("Selecione o Item", df["id"])

    if st.button("Remover") or item_id:
        df = pd.read_excel("cardapio.xlsx")
        df = df[df["id"] != item_id]
        df.to_excel("cardapio.xlsx", index=False)
        if os.path.exists(os.path.join("src", "images", "cardapio", f"{item_id}.jpeg")):
            os.remove(os.path.join("src", "images", "cardapio", f"{item_id}.jpeg"))
        st.success("Item removido com sucesso!")

def exibir_cardapio():
    st.subheader("Cardápio Atual")
    df = pd.read_excel("cardapio.xlsx")
    st.table(df)
