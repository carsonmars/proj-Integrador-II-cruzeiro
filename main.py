import streamlit as st
import pandas as pd
import os

# Função para exibir o cardápio
def mostrar_cardapio():
    st.title("Cardápio Sabor & Aroma")
    if os.path.exists("cardapio.csv"):
        df = pd.read_csv("cardapio.csv")
        st.markdown("""
        <style>
        .card {
            border: 1px solid #ddd;
            border-radius: 10px;
            padding: 10px;
            margin: 10px 0;
            display: flex;
            align-items: center;
        }
        .card img {
            border-radius: 10px;
            margin-right: 20px;
        }
        .card-content {
            flex: 1;
        }
        </style>
        """, unsafe_allow_html=True)
        for index, row in df.iterrows():
            st.markdown(f"""
            <div class="card">
                <img src="{row["imagem"]}" width="100">
                <div class="card-content">
                    <h3>{row["nome"]}</h3>
                    <p>{row["descricao"]}</p>
                    <p><strong>Preço:</strong> R$ {row["preco"]:.2f}</p>
                </div>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.error("Arquivo 'cardapio.csv' não encontrado. Por favor, verifique se o arquivo está no diretório correto.")

# Função para fazer um pedido
def fazer_pedido():
    st.subheader("Fazer Pedido")
    if os.path.exists("cardapio.csv"):
        cardapio_df = pd.read_csv("cardapio.csv")
        item = st.selectbox("Selecione um item", cardapio_df["nome"])
        quantidade = st.number_input("Quantidade", min_value=1, max_value=10)
        if st.button("Adicionar ao Carrinho"):
            if os.path.exists("pedidos.csv"):
                pedidos_df = pd.read_csv("pedidos.csv")
            else:
                pedidos_df = pd.DataFrame(columns=["id", "item_id", "quantidade"])
            item_id = cardapio_df[cardapio_df["nome"] == item]["id"].values[0]
            novo_pedido = pd.DataFrame({"id": [len(pedidos_df)], "item_id": [item_id], "quantidade": [quantidade]})
            novo_pedido.to_csv("pedidos.csv", mode='a', header=False, index=False)
            st.write(f"{quantidade}x {item} adicionado ao carrinho.")
    else:
        st.error("Arquivo 'cardapio.csv' não encontrado. Por favor, verifique se o arquivo está no diretório correto.")

# Função para exibir o carrinho
def mostrar_carrinho():
    st.subheader("Carrinho de Compras")
    if os.path.exists("pedidos.csv"):
        pedidos_df = pd.read_csv("pedidos.csv")
        cardapio_df = pd.read_csv("cardapio.csv")
        pedidos_df = pedidos_df.merge(cardapio_df, left_on="item_id", right_on="id")
        st.dataframe(pedidos_df[["nome", "quantidade", "preco"]])
        total = (pedidos_df["quantidade"] * pedidos_df["preco"]).sum()
        st.write(f"**Total: R$ {total:.2f}**")
        if st.button("Finalizar Compra"):
            if os.path.exists("compras.csv"):
                compras_df = pd.read_csv("compras.csv")
            else:
                compras_df = pd.DataFrame(columns=["id", "item_id", "quantidade"])
            compras_df = pd.concat([compras_df, pedidos_df[["id", "item_id", "quantidade"]]])
            compras_df.to_csv("compras.csv", index=False)
            os.remove("pedidos.csv")
            st.write("Compra finalizada com sucesso!")
    else:
        st.write("Seu carrinho está vazio.")

# Funções para exibir as páginas
def mostrar_pagina_inicial():
    st.title("Bem-vindo à Cafeteria Sabor & Aroma")
    mostrar_cardapio()
    fazer_pedido()
    mostrar_carrinho()

def mostrar_pagina_pedido():
    st.title("Gerenciar Pedidos")
    if os.path.exists("pedidos.csv"):
        pedidos_df = pd.read_csv("pedidos.csv")
        cardapio_df = pd.read_csv("cardapio.csv")
        pedidos_df = pedidos_df.merge(cardapio_df, left_on="item_id", right_on="id")
        if all(col in pedidos_df.columns for col in ["id", "nome", "quantidade"]):
            st.dataframe(pedidos_df[["id", "nome", "quantidade"]])
        else:
            st.error("Colunas necessárias não encontradas no DataFrame de pedidos.")

        st.subheader("Adicionar Pedido")
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
            pedidos_df[["id", "item_id", "quantidade"]].to_csv("pedidos.csv", index=False)
            st.write("Pedido atualizado com sucesso.")

        st.subheader("Remover Pedido")
        pedido_id_remover = st.number_input("ID do Pedido para Remover", min_value=0, max_value=len(pedidos_df)-1, key="pedido_id_remover")
        if st.button("Remover Pedido"):
            pedidos_df = pedidos_df.drop(pedido_id_remover)
            pedidos_df[["id", "item_id", "quantidade"]].to_csv("pedidos.csv", index=False)
            st.write("Pedido removido com sucesso.")
    else:
        st.error("Arquivo 'pedidos.csv' não encontrado. Por favor, verifique se o arquivo está no diretório correto.")

def mostrar_pagina_editar_cardapio():
    st.title("Editar Cardápio")
    if os.path.exists("cardapio.csv"):
        cardapio_df = pd.read_csv("cardapio.csv")
        st.dataframe(cardapio_df)

        st.subheader("Adicionar Item ao Cardápio")
        nome = st.text_input("Nome do Item")
        descricao = st.text_input("Descrição")
        preco = st.number_input("Preço", min_value=0.0, format="%.2f")
        imagem = st.text_input("URL da Imagem")
        if st.button("Adicionar Item"):
            novo_item = pd.DataFrame({"id": [len(cardapio_df)], "nome": [nome], "descricao": [descricao], "preco": [preco], "imagem": [imagem]})
            novo_item.to_csv("cardapio.csv", mode='a', header=False, index=False)
            st.write(f"Item {nome} adicionado ao cardápio.")

        st.subheader("Editar Item do Cardápio")
        item_id = st.number_input("ID do Item", min_value=0, max_value=len(cardapio_df)-1)
        novo_nome = st.text_input("Novo Nome", value=cardapio_df.at[item_id, "nome"])
        nova_descricao = st.text_input("Nova Descrição", value=cardapio_df.at[item_id, "descricao"])
        novo_preco = st.number_input("Novo Preço", min_value=0.0, format="%.2f", value=cardapio_df.at[item_id, "preco"])
        nova_imagem = st.text_input("Nova URL da Imagem", value=cardapio_df.at[item_id, "imagem"])
        if st.button("Salvar Alterações"):
            cardapio_df.at[item_id, "nome"] = novo_nome
            cardapio_df.at[item_id, "descricao"] = nova_descricao
            cardapio_df.at[item_id, "preco"] = novo_preco
            cardapio_df.at[item_id, "imagem"] = nova_imagem
            cardapio_df.to_csv("cardapio.csv", index=False)
            st.write("Item atualizado com sucesso.")

        st.subheader("Remover Item do Cardápio")
        item_id_remover = st.number_input("ID do Item para Remover", min_value=0, max_value=len(cardapio_df)-1, key="item_id_remover")
        if st.button("Remover Item"):
            cardapio_df = cardapio_df.drop(item_id_remover)
            cardapio_df.to_csv("cardapio.csv", index=False)
            st.write("Item removido com sucesso.")
    else:
        st.error("Arquivo 'cardapio.csv' não encontrado. Por favor, verifique se o arquivo está no diretório correto.")

def mostrar_pagina_administracao():
    st.title("Administração da Cafeteria")
    sub_menu = ["Gerenciar Pedidos", "Editar Cardápio"]
    sub_escolha = st.selectbox("Escolha uma opção", sub_menu)
    if sub_escolha == "Gerenciar Pedidos":
        mostrar_pagina_pedido()
    elif sub_escolha == "Editar Cardápio":
        mostrar_pagina_editar_cardapio()

    if os.path.exists("compras.csv"):
        compras_df = pd.read_csv("compras.csv")
        st.dataframe(compras_df)
    else:
        st.write("Nenhuma compra foi finalizada ainda.")

# Inicializar a página
if "pagina" not in st.session_state:
    st.session_state.pagina = "inicial"

# Navegação entre páginas
menu = ["Início", "Administração"]
escolha = st.sidebar.selectbox("Menu", menu)
if escolha == "Início":
    st.session_state.pagina = "inicial"
elif escolha == "Administração":
    st.session_state.pagina = "administracao"

# Exibir a página selecionada
if st.session_state.pagina == "inicial":
    mostrar_pagina_inicial()
elif st.session_state.pagina == "administracao":
    mostrar_pagina_administracao()
