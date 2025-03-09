import pandas as pd
import streamlit as st
import sqlite3
from app.order import adicionar_ao_carrinho
from app.db import conectar
import os

# Exibe o cardápio como cards.
def exibir_menu_como_cards():
    st.header("Cardápio")
    conn = conectar()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM Produto")
    cardapio = cursor.fetchall()
    
    for i in range(0, len(cardapio), 3):  # Exibir três itens por linha
        cols = st.columns(3)
        for j in range(3):
            if i + j < len(cardapio):
                with cols[j]:
                    item = cardapio[i + j]
                    if item[4] and os.path.exists(item[4]):
                        st.image(item[4], use_container_width=True)  # Exibir a imagem do item
                    st.write(f"**{item[1]}**")
                    st.write(f"{item[2]}")
                    st.write(f"Preço: R$ {item[3]:.2f}")
                    if st.button("Adicionar", key=f"add_{item[0]}"):
                        adicionar_ao_carrinho(item[0], 1)
                    st.write("---")
    
    conn.close()
