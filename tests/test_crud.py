import unittest
import sqlite3
from app.crud import adicionar_item, editar_item, remover_item
from app.db import conectar

class TestCrud(unittest.TestCase):
    def setUp(self):
        # Configuração inicial para os testes
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Produto")
        conn.commit()
        conn.close()

    def test_adicionar_item(self):
        adicionar_item("Café Expresso", "Café forte e encorpado", 5.00, "url_imagem", 10, 1)
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Produto WHERE nome = 'Café Expresso'")
        item = cursor.fetchone()
        conn.close()
        self.assertIsNotNone(item)
        self.assertEqual(item[1], "Café Expresso")

    def test_editar_item(self):
        adicionar_item("Café Expresso", "Café forte e encorpado", 5.00, "url_imagem", 10, 1)
        editar_item(1, "Café Expresso", "Café forte e encorpado com leite", 6.00, "url_imagem", 10, 1)
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Produto WHERE id_produto = 1")
        item = cursor.fetchone()
        conn.close()
        self.assertEqual(item[2], "Café forte e encorpado com leite")
        self.assertEqual(item[3], 6.00)

    def test_remover_item(self):
        adicionar_item("Café Expresso", "Café forte e encorpado", 5.00, "url_imagem", 10, 1)
        remover_item(1)
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Produto WHERE id_produto = 1")
        item = cursor.fetchone()
        conn.close()
        self.assertIsNone(item)

if __name__ == '__main__':
    unittest.main()
