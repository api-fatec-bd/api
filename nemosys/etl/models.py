from django.db import models

# Create your models here.


class DimUsuario(models.Model):
    id_usuario = models.CharField("id user", primary_key=True, max_length=50)
    nome_usuario = models.CharField("nome_usuario", null=False, max_length=100)
    codigo_permissao = models.IntegerField("codigo_permissao", null=False)
    descricao_permissao = models.CharField("descricao_permissao", null=False, max_length=50)

    class Meta:
        db_table = "dim_usuario"


class FactLoginPlataforma(models.Model):
    id_usuario = models.ForeignKey(DimUsuario, db_column='id_usuario', on_delete=models.CASCADE)
    data_login = models.DateTimeField("data_login", null=False)
    data_logoff = models.DateTimeField("data_logoff", null=False)
    quantidade_acesso = models.IntegerField("descricao_permissao", null=False)

    class Meta:
        db_table = "fact_login_plataforma"
