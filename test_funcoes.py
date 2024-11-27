import unittest
import os
from funcoes import criar_contato, listar_contatos, atualizar_contato, deletar_contato

class TestFuncoes(unittest.TestCase):
    def setUp(self):
        self.arquivo = 'test_contatos.csv'
        self.dados_teste = [
            {'nome': 'Alice', 'telefone': '123456789', 'email': 'alice@example.com', 'endereco': 'Rua A'},
            {'nome': 'Bob', 'telefone': '987654321', 'email': 'bob@example.com', 'endereco': 'Rua B'},
        ]
        self.dados_inicial = [{'nome': '', 'telefone': '', 'email': '', 'endereco': ''}]
        
    def tearDown(self):
        if os.path.exists(self.arquivo):
            os.remove(self.arquivo)

    def test_criar_contato(self):
        criar_contato(self.dados_teste[0])
        criar_contato(self.dados_teste[1])
        self.assertEqual(len(listar_contatos()), 2)
        
    def test_listar_contatos(self):
        self.assertEqual(listar_contatos(), self.dados_inicial)

    def test_atualizar_contato(self):
        criar_contato(self.dados_teste[0])
        atualizar_contato('Alice', {'nome': 'Alice', 'telefone': '111111111', 'email': 'alice_updated@example.com', 'endereco': 'Rua A1'})
        contato = listar_contatos()[0]
        self.assertEqual(contato['telefone'], '111111111')
        
    def test_deletar_contato(self):
        criar_contato(self.dados_teste[0])
        deletar_contato('Alice')
        self.assertEqual(len(listar_contatos()), 0)
        
if __name__ == '__main__':
    unittest.main()
