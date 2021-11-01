from django.db import models

# Create your models here.
from django.db.models import UniqueConstraint


class DimUsuario(models.Model):
    id_usuario = models.CharField("id user", primary_key=True, max_length=50)
    nome_usuario = models.CharField("nome_usuario", null=False, max_length=100)
    codigo_permissao = models.IntegerField("codigo_permissao", null=False)
    descricao_permissao = models.CharField("descricao_permissao", null=False, max_length=50)

    class Meta:
        db_table = "dim_usuario"


class FactLoginPlataforma(models.Model):
    id_usuario = models.ForeignKey(DimUsuario, db_column='id_usuario', on_delete=models.PROTECT)
    data_login = models.DateTimeField("data_login", null=False)
    data_logoff = models.DateTimeField("data_logoff", null=False)
    quantidade_acesso = models.IntegerField("descricao_permissao", null=False)

    class Meta:
        db_table = "fact_login_plataforma"
        constraints = [models.UniqueConstraint(fields=['id_usuario', 'data_login', 'data_logoff'], name='unique_login')]


class DimCurso(models.Model):
    id_curso = models.IntegerField("id curso", primary_key=True)
    descricao = models.CharField("nome_usuario", null=False, max_length=50)
    graduacao = models.CharField("codigo_permissao", null=False, max_length=50)
    duracao = models.IntegerField("descricao_permissao", null=False)

    class Meta:
        db_table = "dim_curso"


class DimTurma(models.Model):
    id_turma = models.IntegerField("id_turma", primary_key=True)
    descricao = models.CharField("nome_usuario", null=False, max_length=50)
    id_professor = models.CharField("codigo_permissao", null=False, max_length=50)

    class Meta:
        db_table = "dim_turma"


class DimDisciplina(models.Model):
    id_disciplina = models.IntegerField("id curso", primary_key=True)
    descricao = models.CharField("nome_usuario", null=False, max_length=50)
    id_curso = models.ForeignKey(DimCurso, db_column='id_curso', null=False, on_delete=models.PROTECT)
    id_turma = models.ForeignKey(DimTurma, db_column='id_turma', null=False, on_delete=models.PROTECT)

    class Meta:
        db_table = "dim_disciplina"


class DimAula(models.Model):
    id_aula = models.IntegerField("id aula", primary_key=True)
    data_inicio = models.DateTimeField("data_inicio", null=False)
    data_fim = models.DateTimeField("data_fim", null=False)
    id_disciplina = models.ForeignKey(DimDisciplina, db_column='id_disciplina', null=False, on_delete=models.PROTECT)
    titulo = models.CharField("titulo", null=False, max_length=45)
    duracao = models.FloatField("duracao", null=False)
    assunto = models.CharField("assunto", null=False, max_length=100)

    class Meta:
        db_table = "dim_aula"


