import unittest

from insertsFiltroGiovanni import *

class TestConexaoBanco(unittest.TestCase):
    def test_conexaoBanco(self):
            self.assertTrue(conexaoBanco())

class TestInsertDimCurso(unittest.TestCase):
    def test_insertDimCurso(self):
            self.assertEqual(insertDimCurso(), "Cursos inseridos com sucesso!")

class TestInsertDimDisciplina(unittest.TestCase):
    def test_insertDimDisciplina(self):
            self.assertEqual(insertDimDisciplina(), "Disciplinas inseridas com sucesso!")

class TestInsertDimAula(unittest.TestCase):
    def test_insertDimAula(self):
            self.assertEqual(insertDimAula(), "Aulas inseridos com sucesso!")

class TestInsertFactAcesso(unittest.TestCase):
    def test_insertFactAcesso(self):
            self.assertEqual(insertFactAcesso(), "Acessos inseridos com sucesso!")

class TestInsertFactChat(unittest.TestCase):
    def test_insertFactChat(self):
            self.assertEqual(insertFactChat(), "Chat inseridos com sucesso!")

class TestInsertFactUsuarioChat(unittest.TestCase):
    def test_insertFactUsuarioChat(self):
            self.assertEqual(insertFactUsuarioChat(), "Usuarios Chat inseridos com sucesso!")




if __name__ == '__name__':
    unittest.main()