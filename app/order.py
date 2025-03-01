# Este arquivo conterá o código relacionado aos pedidos.

import streamlit as st
import pandas as pd
import os

def adicionar_ao_carrinho(item_id, quantidade):
    if os.path.exists("pedidos_temp.xlsx"):
        pedidos_df = pd.read_excel("pedidos_temp.xlsx", sheet_name="itens_pedido")
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

def finalizar_compra():
    if os.path.exists("pedidos_temp.xlsx"):
        pedidos_df = pd.read_excel("pedidos_temp.xlsx", sheet_name="itens_pedido")
        if os.path.exists("pedidos.xlsx"):
            try:
                with pd.ExcelWriter("pedidos.xlsx", mode="a", engine="openpyxl", if_sheet_exists="overlay") as writer:
                    pedidos_df.to_excel(writer, sheet_name="itens_pedido", index=False, header=False, startrow=writer.sheets["itens_pedido"].max_row)
            except Exception as e:
                st.error(f"Erro ao salvar o pedido: {e}")
        else:
            with pd.ExcelWriter("pedidos.xlsx", engine="openpyxl") as writer:
                pedidos_df.to_excel(writer, sheet_name="itens_pedido", index=False)
        os.remove("pedidos_temp.xlsx")
        st.write("Compra finalizada com sucesso!")
    else:
        st.write("Nenhum item no carrinho para finalizar a compra.")

