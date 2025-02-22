import unittest

def adicionar_item(nome_item, quantidade):
    return f"{quantidade}x {nome_item} adicionado ao carrinho."

class TestMenu(unittest.TestCase):
    def test_item_adicionado(self):
        self.assertEqual(adicionar_item("Café Expresso", 2), "2x Café Expresso adicionado ao carrinho.")

if __name__ == '__main__':
    unittest.main()
