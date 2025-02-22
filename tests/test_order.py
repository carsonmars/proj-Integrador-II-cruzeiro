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

    def test_pedido_vazio(self):
        self.assertTrue(self.df.empty)

if __name__ == '__main__':
    unittest.main()