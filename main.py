import streamlit as st
import pandas as pd
import os
from app.menu import exibir_menu_como_cards
from app.order import adicionar_ao_carrinho, finalizar_compra, exibir_carrinho, limpar_carrinho
from app.crud import adicionar_item, editar_item, remover_item, exibir_cardapio

st.set_page_config(page_title="Cafeteria Sabor & Aroma", layout="wide")

st.title("Bem-vindo à Cafeteria Sabor & Aroma")

# Menu de navegação
st.sidebar.title("Menu")
cliente_btn = st.sidebar.button("Cliente")
funcionario_btn = st.sidebar.button("Funcionário")

# Variável para controlar o menu ativo
if 'menu_ativo' not in st.session_state:
    st.session_state.menu_ativo = 'Cliente'

# Atualizar o menu ativo com base no botão clicado
if cliente_btn:
    st.session_state.menu_ativo = 'Cliente'
elif funcionario_btn:
    st.session_state.menu_ativo = 'Funcionário'

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

elif st.session_state.menu_ativo == 'Funcionário':
    st.header("Menu do Funcionário")
    # Exibir o cardápio em forma de tabela
    exibir_cardapio()

    # Funcionalidades de CRUD para o cardápio
    opcao = st.selectbox("Escolha uma opção", ["Adicionar Item", "Editar Item", "Remover Item"])

    if opcao == "Adicionar Item":
        adicionar_item()
    elif opcao == "Editar Item":
        editar_item()
    elif opcao == "Remover Item":
        remover_item()
