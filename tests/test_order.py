import unittest
from app.order import adicionar_ao_carrinho, exibir_carrinho, limpar_carrinho, finalizar_compra
from app.db import conectar

class TestOrder(unittest.TestCase):
    def setUp(self):
        # Configuração inicial para os testes
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM ItemPedido")
        cursor.execute("DELETE FROM Pedido")
        cursor.execute("DELETE FROM Produto")
        cursor.execute("INSERT INTO Produto (id_produto, nome, descricao, preco, imagem, estoque, id_categoria) VALUES (1, 'Café Expresso', 'Café forte e encorpado', 5.00, '', 100, 1)")
        conn.commit()
        conn.close()

    def test_adicionar_ao_carrinho(self):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Produto WHERE id_produto = 1")
        produto = cursor.fetchone()
        conn.close()
        self.assertIsNotNone(produto)
        
        adicionar_ao_carrinho(1, 2)
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM ItemPedido WHERE id_produto = 1")
        item = cursor.fetchone()
        conn.close()
        self.assertIsNotNone(item)
        self.assertEqual(item[2], 2)

        adicionar_ao_carrinho(1, 1)
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM ItemPedido WHERE id_produto = 1")
        item = cursor.fetchone()
        conn.close()
        self.assertIsNotNone(item)
        self.assertEqual(item[2], 3)

    def test_limpar_carrinho(self):
        adicionar_ao_carrinho(1, 2)
        limpar_carrinho()
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM ItemPedido WHERE id_produto = 1")
        item = cursor.fetchone()
        conn.close()
        self.assertIsNone(item)

    def test_finalizar_compra(self):
        adicionar_ao_carrinho(1, 2)
        finalizar_compra()
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Pedido")
        pedido = cursor.fetchone()
        cursor.execute("SELECT * FROM ItemPedido WHERE id_pedido = ?", (pedido[0],))
        item = cursor.fetchone()
        conn.close()
        self.assertIsNotNone(pedido)
        self.assertIsNotNone(item)

if __name__ == '__main__':
    unittest.main()
