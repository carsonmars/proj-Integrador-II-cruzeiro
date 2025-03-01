# Este arquivo conterá os testes para o módulo de pedidos.
import unittest
import pandas as pd
from app.order import fazer_pedido

class TestOrder(unittest.TestCase):
    def test_fazer_pedido(self):
        # Simular a adição de um pedido
        df = pd.read_csv("pedidos.csv")
        initial_length = len(df)
        fazer_pedido("Café Expresso", 2)
        df = pd.read_csv("pedidos.csv")
        self.assertEqual(len(df), initial_length + 1)

if __name__ == '__main__':
    unittest.main()
