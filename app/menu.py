import pandas as pd
import streamlit as st
import os

def adicionar_ao_carrinho(item_id, quantidade):
    # Implementar a lógica para adicionar o item ao carrinho
    st.write(f"Item {item_id} adicionado ao carrinho com quantidade {quantidade}")

def exibir_menu_como_cards():
    st.header("Cardápio")
    df = pd.read_excel("cardapio.xlsx")
    for i in range(0, len(df), 2):
        cols = st.columns(2)
        for j in range(2):
            if i + j < len(df):
                with cols[j]:
                    row = df.iloc[i + j]
                    image_path = os.path.join("src", "images", "cardapio", f"{row['id']}.jpeg")
                    if os.path.exists(image_path):
                        st.image(image_path, width=150)
                    else:
                        st.write(f"Imagem não encontrada: {image_path}")
                    st.write(f"**{row['nome']}**")
                    st.write(f"{row['descricao']}")
                    st.write(f"Preço: R$ {row['preco']:.2f}")
                    if st.button("Adicionar", key=f"add_{i + j}"):
                        adicionar_ao_carrinho(row['id'], 1)
                    st.write("---")
