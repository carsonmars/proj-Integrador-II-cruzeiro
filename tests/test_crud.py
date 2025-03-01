import unittest
import pandas as pd
from app.crud import adicionar_item, editar_item, remover_item

class TestCrud(unittest.TestCase):
    def setUp(self):
        # Configuração inicial para os testes
        self.df = pd.DataFrame(columns=["id", "nome", "descricao", "preco"])
        self.df.to_excel("cardapio.xlsx", index=False)

    def test_adicionar_item(self):
        adicionar_item("Café Expresso", "Café forte e encorpado", 5.00)
        df = pd.read_excel("cardapio.xlsx")
        self.assertEqual(len(df), 1)
        self.assertEqual(df.iloc[0]["nome"], "Café Expresso")

    def test_editar_item(self):
        adicionar_item("Café Expresso", "Café forte e encorpado", 5.00)
        editar_item(1, "Café Expresso", "Café forte e encorpado com leite", 6.00)
        df = pd.read.excel("cardapio.xlsx")
        self.assertEqual(df.iloc[0]["descricao"], "Café forte e encorpado com leite")
        self.assertEqual(df.iloc[0]["preco"], 6.00)

    def test_remover_item(self):
        adicionar_item("Café Expresso", "Café forte e encorpado", 5.00)
        remover_item(1)
        df = pd.read.excel("cardapio.xlsx")
        self.assertEqual(len(df), 0)

if __name__ == '__main__':
    unittest.main()
