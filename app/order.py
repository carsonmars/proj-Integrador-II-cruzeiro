# Este arquivo conterá o código relacionado aos pedidos.

import streamlit as st
import pandas as pd
import os
from datetime import datetime

def adicionar_ao_carrinho(item_id, quantidade):
    if os.path.exists("pedidos_temp.xlsx"):
        pedidos_df = pd.read_excel("pedidos_temp.xlsx", sheet_name="itens_pedido")
        if item_id in pedidos_df["produto_id"].values:
            pedidos_df.loc[pedidos_df["produto_id"] == item_id, "quantidade"] += quantidade
        else:
            novo_pedido = pd.DataFrame({"pedido_id": [1], "produto_id": [item_id], "quantidade": [quantidade]})
            pedidos_df = pd.concat([pedidos_df, novo_pedido], ignore_index=True)
    else:
        pedidos_df = pd.DataFrame(columns=["pedido_id", "produto_id", "quantidade"])
        novo_pedido = pd.DataFrame({"pedido_id": [1], "produto_id": [item_id], "quantidade": [quantidade]})
        pedidos_df = pd.concat([pedidos_df, novo_pedido], ignore_index=True)
    
    with pd.ExcelWriter("pedidos_temp.xlsx") as writer:
        pedidos_df.to_excel(writer, sheet_name="itens_pedido", index=False)
    st.write(f"{quantidade}x item adicionado ao carrinho.")

def exibir_carrinho():
    st.header("Carrinho de Compras")
    if os.path.exists("pedidos_temp.xlsx"):
        pedidos_df = pd.read_excel("pedidos_temp.xlsx", sheet_name="itens_pedido")
        cardapio_df = pd.read_excel("cardapio.xlsx")
        pedidos_df = pedidos_df.merge(cardapio_df, left_on="produto_id", right_index=True)
        st.table(pedidos_df[["nome", "quantidade", "preco"]])
        total = (pedidos_df["quantidade"] * pedidos_df["preco"]).sum()
        st.write(f"Total: R$ {total:.2f}")
    else:
        st.write("Seu carrinho está vazio.")

def limpar_carrinho():
    if os.path.exists("pedidos_temp.xlsx"):
        os.remove("pedidos_temp.xlsx")
        st.write("Carrinho limpo com sucesso!")
    else:
        st.write("O carrinho já está vazio.")

def finalizar_compra():
    if os.path.exists("pedidos_temp.xlsx"):
        pedidos_df = pd.read_excel("pedidos_temp.xlsx", sheet_name="itens_pedido")
        if os.path.exists("pedidos.xlsx"):
            try:
                pedidos_final_df = pd.read_excel("pedidos.xlsx", sheet_name="itens_pedido")
                novo_pedido_id = pedidos_final_df["pedido_id"].max() + 1
                pedidos_df["pedido_id"] = novo_pedido_id
                pedidos_final_df = pd.concat([pedidos_final_df, pedidos_df], ignore_index=True)
                with pd.ExcelWriter("pedidos.xlsx", engine="openpyxl") as writer:
                    pedidos_final_df.to_excel(writer, sheet_name="itens_pedido", index=False)
            except Exception as e:
                st.error(f"Erro ao salvar o pedido: {e}")
        else:
            pedidos_df["pedido_id"] = 1
            with pd.ExcelWriter("pedidos.xlsx", engine="openpyxl") as writer:
                pedidos_df.to_excel(writer, sheet_name="itens_pedido", index=False)
        os.remove("pedidos_temp.xlsx")
        st.write("Compra finalizada com sucesso!")
    else:
        st.write("Nenhum item no carrinho para finalizar a compra.")

