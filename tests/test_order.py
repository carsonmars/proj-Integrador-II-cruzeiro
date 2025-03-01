# Este arquivo conterá os testes para o módulo de pedidos.
import unittest
import pandas as pd
from app.order import adicionar_ao_carrinho, limpar_carrinho, finalizar_compra

class TestOrder(unittest.TestCase):
    def setUp(self):
        # Configuração inicial para os testes
        limpar_carrinho()

    def test_adicionar_ao_carrinho(self):
        adicionar_ao_carrinho(1, 2)
        pedidos_df = pd.read_excel("pedidos_temp.xlsx", sheet_name="itens_pedido")
        self.assertEqual(len(pedidos_df), 1)
        self.assertEqual(pedidos_df.iloc[0]["produto_id"], 1)
        self.assertEqual(pedidos_df.iloc[0]["quantidade"], 2)

    def test_finalizar_compra(self):
        adicionar_ao_carrinho(1, 2)
        finalizar_compra()
        pedidos_df = pd.read_excel("pedidos.xlsx", sheet_name="itens_pedido")
        self.assertEqual(len(pedidos_df[pedidos_df["pedido_id"] == 1]), 1)
        self.assertEqual(pedidos_df.iloc[0]["produto_id"], 1)
        self.assertEqual(pedidos_df.iloc[0]["quantidade"], 2)

if __name__ == '__main__':
    unittest.main()
