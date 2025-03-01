import pandas as pd
import streamlit as st
import os
from app.order import adicionar_ao_carrinho

def exibir_menu_como_cards():
    st.header("Cardápio")
    df = pd.read_excel("cardapio.xlsx")
    for i in range(2, len(df)):  # Comece a partir da linha 1 para ignorar os atributos da tabela
        row = df.iloc[i]
        image_path = os.path.join("src", "images", "cardapio", f"{row['id']}.jpeg")
        if os.path.exists(image_path):
            st.image(image_path, width=150)
        else:
            st.write(f"Imagem não encontrada: {image_path}")
        st.write(f"**{row['nome']}**")
        st.write(f"{row['descricao']}")
        st.write(f"Preço: R$ {row['preco']:.2f}")
        if st.button("Adicionar", key=f"add_{row['id']}"):
            adicionar_ao_carrinho(row['id'], 1)
        st.write("---")
