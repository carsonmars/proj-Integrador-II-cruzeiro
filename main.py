import streamlit as st
import pandas as pd
import os

# Funções para exibir as páginas
def mostrar_pagina_inicial():
    st.title("Bem-vindo à Cafeteria Sabor & Aroma")
    menu = ["Fazer Pedido", "Cardápio"]
    escolha = st.selectbox("Escolha uma opção", menu)
    if escolha == "Fazer Pedido":
        st.session_state.pagina = "pedido"
    elif escolha == "Cardápio":
        st.session_state.pagina = "cardapio"

def mostrar_pagina_pedido():
    st.title("Gerenciar Pedidos")
    if os.path.exists("pedidos.csv"):
        pedidos_df = pd.read_csv("pedidos.csv")
        st.dataframe(pedidos_df)

        st.subheader("Adicionar Pedido")
        cardapio_df = pd.read_csv("cardapio.csv")
        item = st.selectbox("Selecione um item", cardapio_df["nome"])
        quantidade = st.number_input("Quantidade", min_value=1, max_value=10)
        if st.button("Adicionar ao Carrinho"):
            item_id = cardapio_df[cardapio_df["nome"] == item]["id"].values[0]
            novo_pedido = pd.DataFrame({"id": [len(pedidos_df)], "item_id": [item_id], "quantidade": [quantidade]})
            novo_pedido.to_csv("pedidos.csv", mode='a', header=False, index=False)
            st.write(f"{quantidade}x {item} adicionado ao carrinho.")

        st.subheader("Editar Pedido")
        pedido_id = st.number_input("ID do Pedido", min_value=0, max_value=len(pedidos_df)-1)
        novo_item = st.selectbox("Novo Item", cardapio_df["nome"], key="novo_item")
        nova_quantidade = st.number_input("Nova Quantidade", min_value=1, max_value=10, key="nova_quantidade")
        if st.button("Salvar Alterações"):
            item_id = cardapio_df[cardapio_df["nome"] == novo_item]["id"].values[0]
            pedidos_df.at[pedido_id, "item_id"] = item_id
            pedidos_df.at[pedido_id, "quantidade"] = nova_quantidade
            pedidos_df.to_csv("pedidos.csv", index=False)
            st.write("Pedido atualizado com sucesso.")

        st.subheader("Remover Pedido")
        pedido_id_remover = st.number_input("ID do Pedido para Remover", min_value=0, max_value=len(pedidos_df)-1, key="pedido_id_remover")
        if st.button("Remover Pedido"):
            pedidos_df = pedidos_df.drop(pedido_id_remover)
            pedidos_df.to_csv("pedidos.csv", index=False)
            st.write("Pedido removido com sucesso.")
    else:
        st.error("Arquivo 'pedidos.csv' não encontrado. Por favor, verifique se o arquivo está no diretório correto.")

def mostrar_pagina_cardapio():
    st.title("Cardápio Sabor & Aroma")
    if os.path.exists("cardapio.csv"):
        df = pd.read_csv("cardapio.csv")
        st.dataframe(df)

        for index, row in df.iterrows():
            st.subheader(row["nome"])
            st.write(f"Descrição: {row['descricao']}")
            st.write(f"Preço: R$ {row['preco']:.2f}")
            st.image(row["imagem"], width=200)
            st.write("---")
    else:
        st.error("Arquivo 'cardapio.csv' não encontrado. Por favor, verifique se o arquivo está no diretório correto.")

# Inicializar a página
if "pagina" not in st.session_state:
    st.session_state.pagina = "inicial"

# Navegação entre páginas
if st.session_state.pagina == "inicial":
    mostrar_pagina_inicial()
elif st.session_state.pagina == "pedido":
    mostrar_pagina_pedido()
elif st.session_state.pagina == "cardapio":
    mostrar_pagina_cardapio()
