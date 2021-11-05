import unittest

from insertsFiltroGiovanni import *

from datetime import datetime

class TestConexaoBanco(unittest.TestCase):
    def test_conexaoBanco(self):
            self.assertTrue(conexaoBanco())

class TestInsertDimDisciplina(unittest.TestCase):
    def test_insertDimDisciplina(self):
            self.assertEqual(insertDimDisciplina(10000, 10000, 'Teste', 10), "Disciplina inserida com sucesso!")

class TestInsertDimCurso(unittest.TestCase):
    def test_insertDimCurso(self):
            self.assertEqual(insertDimCurso(10000, 'Teste', 'Teste', 10), "Curso inserido com sucesso!")

class TestInsertDimAula(unittest.TestCase):
    def test_insertDimAula(self):
            dateTeste = datetime.strptime("2020-10-07 01:34:43", '%Y-%m-%d %H:%M:%S')
            self.assertEqual(insertDimAula(10000,dateTeste,dateTeste,10,'Teste',2,'Teste'), "Aula inserida com sucesso!")

class TestInsertFactAcesso(unittest.TestCase):
    def test_insertFactAcesso(self):
            dateTeste = datetime.strptime("2020-10-07 01:34:43", '%Y-%m-%d %H:%M:%S')
            self.assertEqual(insertFactAcesso(1,dateTeste,dateTeste,'T'), "Acesso inserido com sucesso!")

class TestInsertFactChat(unittest.TestCase):
    def test_insertFactChat(self):
            dateTeste = datetime.strptime("2020-10-07 01:34:43", '%Y-%m-%d %H:%M:%S')
            self.assertEqual(insertFactChat(10000,dateTeste,dateTeste,10,'Teste', 2), "Chat inserido com sucesso!")

class TestInsertFactUsuarioChat(unittest.TestCase):
    def test_insertFactUsuarioChat(self):
            dateTeste = datetime.strptime("2020-10-07 01:34:43", '%Y-%m-%d %H:%M:%S')
            self.assertEqual(insertFactUsuarioChat(10000,1,'10000',dateTeste,dateTeste,10,dateTeste,10.0), "Usuario Chat inserido com sucesso!")


""""
QUERY EXCLUSÃO TESTES
delete from dim_aula where id_aula = 10000;
delete from dim_disciplina where id_disciplina = 10000;
delete from dim_curso where id_curso = 10000;
delete from fact_acesso where origem = 'T';
delete from dim_chat where id_chat = '10000';
delete from fact_usuario_chat where id_usuario_chat = 10000;
"""""


if __name__ == '__name__':
    unittest.main()