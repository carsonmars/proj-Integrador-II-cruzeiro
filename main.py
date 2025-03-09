import streamlit as st

# Configurações iniciais do Streamlit
st.set_page_config(page_title="Cafeteria Sabor & Aroma", layout="wide")

from app.menu import exibir_menu_como_cards
from app.order import adicionar_ao_carrinho, finalizar_compra, exibir_carrinho, limpar_carrinho
from app.crud import adicionar_item, editar_item, remover_item, exibir_cardapio, adicionar_categoria, exibir_categorias, editar_categoria, remover_categoria
from app.db import criar_tabelas

st.title("Bem-vindo à Cafeteria Sabor & Aroma")

# Criar tabelas no banco de dados
criar_tabelas()

# Menu de navegação
st.sidebar.title("Menu")
cliente_btn = st.sidebar.button("Cliente")
administracao_btn = st.sidebar.button("Administração")

# Variável para controlar o menu ativo
if 'menu_ativo' not in st.session_state:
    st.session_state.menu_ativo = 'Cliente'

# Atualizar o menu ativo com base no botão clicado
if cliente_btn:
    st.session_state.menu_ativo = 'Cliente'
elif administracao_btn:
    st.session_state.menu_ativo = 'Administração'

# Exibir o menu ativo
if st.session_state.menu_ativo == 'Cliente':
    st.header("Menu do Cliente")
    # Exibir o cardápio com cards ao iniciar o aplicativo
    exibir_menu_como_cards()

    # Botão para limpar o carrinho
    if st.button("Limpar Carrinho"):
        limpar_carrinho()

    # Exibir o carrinho de compras
    exibir_carrinho()

    # Botão para finalizar a compra
    if st.button("Finalizar Compra"):
        finalizar_compra()

elif st.session_state.menu_ativo == 'Administração':
    st.header("Administração")
    # Botões para navegação dentro da administração
    cardapio_atual_btn = st.button("Cardápio Atual")
    categoria_produtos_btn = st.button("Categoria de Produtos")

    if cardapio_atual_btn:
        st.session_state.submenu_ativo = 'Cardápio Atual'
    elif categoria_produtos_btn:
        st.session_state.submenu_ativo = 'Categoria de Produtos'

    # Exibir o submenu ativo
    if 'submenu_ativo' in st.session_state:
        if st.session_state.submenu_ativo == 'Cardápio Atual':
            st.header("Gerenciamento do Cardápio Atual")
            opcao = st.selectbox("Escolha uma opção", ["Adicionar Item", "Editar Item", "Remover Item"])
            if opcao == "Adicionar Item":
                adicionar_item()
            elif opcao == "Editar Item":
                editar_item()
            elif opcao == "Remover Item":
                remover_item()
            exibir_cardapio()
        elif st.session_state.submenu_ativo == 'Categoria de Produtos':
            st.header("Gerenciamento de Categoria de Produtos")
            opcao = st.selectbox("Escolha uma opção", ["Adicionar Categoria", "Editar Categoria", "Remover Categoria"])
            if opcao == "Adicionar Categoria":
                adicionar_categoria()
            elif opcao == "Editar Categoria":
                editar_categoria()
            elif opcao == "Remover Categoria":
                remover_categoria()
            exibir_categorias()
