import streamlit as st
import pandas as pd

# Carregar pedidos de um arquivo CSV
pedidos_df = pd.read_csv("pedidos.csv")

# Exibir pedidos existentes
st.title("Gerenciar Pedidos")
st.dataframe(pedidos_df)

# Adicionar novo pedido
st.subheader("Adicionar Pedido")
item = st.selectbox("Selecione um item", ["Café Expresso", "Cappuccino", "Latte"])
quantidade = st.number_input("Quantidade", min_value=1, max_value=10)
if st.button("Adicionar ao Carrinho"):
    novo_pedido = pd.DataFrame({"item": [item], "quantidade": [quantidade]})
    novo_pedido.to_csv("pedidos.csv", mode='a', header=False, index=False)
    st.write(f"{quantidade}x {item} adicionado ao carrinho.")

# Editar pedido existente
st.subheader("Editar Pedido")
pedido_id = st.number_input("ID do Pedido", min_value=0, max_value=len(pedidos_df)-1)
novo_item = st.selectbox("Novo Item", ["Café Expresso", "Cappuccino", "Latte"], key="novo_item")
nova_quantidade = st.number_input("Nova Quantidade", min_value=1, max_value=10, key="nova_quantidade")
if st.button("Salvar Alterações"):
    pedidos_df.at[pedido_id, "item"] = novo_item
    pedidos_df.at[pedido_id, "quantidade"] = nova_quantidade
    pedidos_df.to_csv("pedidos.csv", index=False)
    st.write("Pedido atualizado com sucesso.")

# Remover pedido existente
st.subheader("Remover Pedido")
pedido_id_remover = st.number_input("ID do Pedido para Remover", min_value=0, max_value=len(pedidos_df)-1, key="pedido_id_remover")
if st.button("Remover Pedido"):
    pedidos_df = pedidos_df.drop(pedido_id_remover)
    pedidos_df.to_csv("pedidos.csv", index=False)
    st.write("Pedido removido com sucesso.")
