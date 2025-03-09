import unittest
from app.db import criar_tabelas, conectar

class TestDB(unittest.TestCase):
    def test_criar_tabelas(self):
        criar_tabelas()
        conn = conectar()
        cursor = conn.cursor()
        
        # Verificar se as tabelas foram criadas
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Categoria'")
        self.assertIsNotNone(cursor.fetchone())
        
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Produto'")
        self.assertIsNotNone(cursor.fetchone())
        
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Cliente'")
        self.assertIsNotNone(cursor.fetchone())
        
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Pedido'")
        self.assertIsNotNone(cursor.fetchone())
        
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='ItemPedido'")
        self.assertIsNotNone(cursor.fetchone())
        
        conn.close()

if __name__ == '__main__':
    unittest.main()
