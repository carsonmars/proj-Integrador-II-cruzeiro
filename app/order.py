import streamlit as st
import pandas as pd

item = st.selectbox("Selecione um item", ["Café Expresso", "Cappuccino", "Latte"])
quantidade = st.number_input("Quantidade", min_value=1, max_value=10)
if st.button("Adicionar ao Carrinho"):
    pedidos = pd.DataFrame({"item": [item], "quantidade": [quantidade]})
    pedidos.to_csv("pedidos.csv", mode='a', header=False, index=False)
    st.write(f"{quantidade}x {item} adicionado ao carrinho.")
