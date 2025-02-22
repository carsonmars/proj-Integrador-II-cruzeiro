import pandas as pd
import streamlit as st

# Carregar o cardápio de um arquivo CSV
df = pd.read_csv("cardapio.csv")

# Exibir o cardápio em uma tabela
st.title("Cardápio Sabor & Aroma")
st.dataframe(df)

# Melhorar a interface de exibição
for index, row in df.iterrows():
    st.subheader(row["nome"])
    st.write(f"Descrição: {row['descricao']}")
    st.write(f"Preço: R$ {row['preco']:.2f}")
    st.image(row["imagem"], width=200)
    st.write("---")
