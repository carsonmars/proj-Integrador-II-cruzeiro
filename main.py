import streamlit as st
import pandas as pd
import os
from app.menu import exibir_menu_como_cards
from app.order import adicionar_ao_carrinho, fazer_pedido, finalizar_compra, exibir_carrinho

st.set_page_config(page_title="Cafeteria Sabor & Aroma", layout="wide")

st.title("Bem-vindo à Cafeteria Sabor & Aroma")

# Exibir o cardápio com cards ao iniciar o aplicativo
exibir_menu_como_cards()

# Exibir o carrinho de compras
exibir_carrinho()

# Botões de navegação
if st.button("Fazer Pedido"):
    fazer_pedido()

if st.button("Finalizar Compra"):
    finalizar_compra()
