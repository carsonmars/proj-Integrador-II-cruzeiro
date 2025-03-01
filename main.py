import streamlit as st
import pandas as pd
import os
from app.menu import exibir_menu_como_cards
from app.order import adicionar_ao_carrinho, finalizar_compra, exibir_carrinho, limpar_carrinho

st.set_page_config(page_title="Cafeteria Sabor & Aroma", layout="wide")

st.title("Bem-vindo à Cafeteria Sabor & Aroma")

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
