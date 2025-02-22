import unittest
import pandas as pd

class TestOrder(unittest.TestCase):
    def setUp(self):
        self.df = pd.DataFrame(columns=["item", "quantidade"])

    def test_adicionar_pedido(self):
        item = "Café Expresso"
        quantidade = 2
        self.df = self.df.append({"item": item, "quantidade": quantidade}, ignore_index=True)
        self.assertEqual(self.df.iloc[0]["item"], item)
        self.assertEqual(self.df.iloc[0]["quantidade"], quantidade)

    def test_editar_pedido(self):
        self.df = self.df.append({"item": "Café Expresso", "quantidade": 2}, ignore_index=True)
        self.df.at[0, "item"] = "Cappuccino"
        self.df.at[0, "quantidade"] = 3
        self.assertEqual(self.df.iloc[0]["item"], "Cappuccino")
        self.assertEqual(self.df.iloc[0]["quantidade"], 3)

    def test_remover_pedido(self):
        self.df = self.df.append({"item": "Café Expresso", "quantidade": 2}, ignore_index=True)
        self.df = self.df.drop(0)
        self.assertTrue(self.df.empty)

    def test_pedido_vazio(self):
        self.assertTrue(self.df.empty)

if __name__ == '__main__':
    unittest.main()
