# Este arquivo conterá o código relacionado aos pedidos.

import streamlit as st
import pandas as pd
import os

def fazer_pedido():
    st.header("Fazer Pedido")
    df = pd.read_excel("cardapio.xlsx")
    item = st.selectbox("Selecione um item", df['nome'])
    quantidade = st.number_input("Quantidade", min_value=1, max_value=10)
    
    if st.button("Adicionar ao Carrinho"):
        item_id = df[df['nome'] == item].index[0]
        if os.path.exists("pedidos_temp.xlsx"):
            pedidos_df = pd.read_excel("pedidos_temp.xlsx")
        else:
            pedidos_df = pd.DataFrame(columns=["pedido_id", "item_id", "quantidade"])
        novo_pedido = pd.DataFrame({"pedido_id": [1], "item_id": [item_id], "quantidade": [quantidade]})
        pedidos_df = pd.concat([pedidos_df, novo_pedido], ignore_index=True)
        pedidos_df.to_excel("pedidos_temp.xlsx", index=False)
        st.write(f"{quantidade}x {item} adicionado ao carrinho.")

def adicionar_ao_carrinho(item_id, quantidade):
    if os.path.exists("pedidos_temp.xlsx"):
        pedidos_df = pd.read_excel("pedidos_temp.xlsx")
    else:
        pedidos_df = pd.DataFrame(columns=["pedido_id", "item_id", "quantidade"])
    novo_pedido = pd.DataFrame({"pedido_id": [1], "item_id": [item_id], "quantidade": [quantidade]})
    pedidos_df = pd.concat([pedidos_df, novo_pedido], ignore_index=True)
    pedidos_df.to_excel("pedidos_temp.xlsx", index=False)
    st.write(f"{quantidade}x item adicionado ao carrinho.")

def exibir_carrinho():
    st.header("Carrinho de Compras")
    if os.path.exists("pedidos_temp.xlsx"):
        pedidos_df = pd.read_excel("pedidos_temp.xlsx")
        cardapio_df = pd.read_excel("cardapio.xlsx")
        pedidos_df = pedidos_df.merge(cardapio_df, left_on="item_id", right_index=True)
        st.table(pedidos_df[["nome", "quantidade", "preco"]])
        total = (pedidos_df["quantidade"] * pedidos_df["preco"]).sum()
        st.write(f"Total: R$ {total:.2f}")
    else:
        st.write("Seu carrinho está vazio.")

def finalizar_compra():
    if os.path.exists("pedidos_temp.xlsx"):
        pedidos_df = pd.read_excel("pedidos_temp.xlsx")
        if os.path.exists("pedidos.xlsx"):
            pedidos_final_df = pd.read_excel("pedidos.xlsx")
            pedidos_final_df = pd.concat([pedidos_final_df, pedidos_df], ignore_index=True)
        else:
            pedidos_final_df = pedidos_df
        pedidos_final_df.to_excel("pedidos.xlsx", index=False)
        os.remove("pedidos_temp.xlsx")
        st.write("Compra finalizada com sucesso!")
    else:
        st.write("Nenhum item no carrinho para finalizar a compra.")

