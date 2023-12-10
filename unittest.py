import unittest
import pandas as pd

class TestDataQuality(unittest.TestCase):
    def setUp(self):
        # Supondo que você tenha um DataFrame representando seus dados
        data = {
            'Nome': ['João', 'Maria', 'Carlos', None, 'Ana'],
            'Idade': [30, 25, 40, 35, None],
            'Email': ['joao@email.com', 'maria@email.com', 'carlos@email.com', None, 'ana@email.com']
        }
        self.df = pd.DataFrame(data)

    def test_completude(self):
        # Verifica se há valores nulos nas colunas importantes
        colunas_importantes = ['Nome', 'Idade', 'Email']
        for coluna in colunas_importantes:
            with self.subTest(coluna=coluna):
                self.assertFalse(self.df[coluna].isnull().any(), f'A coluna {coluna} possui valores nulos.')

if __name__ == '__main__':
    unittest.main()
