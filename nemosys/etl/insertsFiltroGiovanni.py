
import psycopg2


from datetime import date

def conexaoBanco():
    conexao = psycopg2.connect(host='157.245.243.16',
                           port='5432',
                           database='PROJETO_API_NEMO',
                           user='username',
                           password='password')
    return conexao


################################################################# INSERT DIM CURSO #################################################################
def insertDimCurso(id_curso, descricao, graduacao, duracao):
    try:
        connection = conexaoBanco()
        cursor = connection.cursor()
        comando_insert = """ INSERT INTO dim_curso (id_curso, descricao, graduacao, duracao) VALUES (%s,%s,%s,%s)"""
        values = (id_curso, descricao, graduacao, duracao)
        cursor.execute(comando_insert, values)
        connection.commit()
        print("INSERT CURSO OK: ", values)
        return "Curso inserido com sucesso!"
    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record into mobile table", error)
        return "Não foi possível cadastrar cursos!"
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

##########################################################################################################################################################

################################################################# INSERT DIM AULA #################################################################
def insertDimAula(id_aula, data_inicio, data_fim, id_disciplina, titulo, duracao, assunto):
    try:
        connection = conexaoBanco()
        cursor = connection.cursor()
        comando_insert = """ INSERT INTO dim_aula (id_aula, data_inicio, data_fim, id_disciplina, titulo, duracao, assunto) VALUES (%s,%s,%s,%s,%s, %s, %s)"""
        values = (id_aula, data_inicio, data_fim, id_disciplina, titulo, duracao, assunto)
        cursor.execute(comando_insert, values)
        connection.commit()
        print("INSERT AULA OK: ", values)
        return "Aula inserida com sucesso!"
    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record into mobile table", error)
        return "Não foi possível cadastrar aulas!"
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

##########################################################################################################################################################



################################################################# INSERT DIM DICIPLINA #################################################################
def insertDimDisciplina(id_disciplina, id_curso, descricao, id_turma):
    try:
        connection = conexaoBanco()
        cursor = connection.cursor()
        comando_insert = """ INSERT INTO dim_disciplina (id_disciplina, id_curso, descricao, id_turma) VALUES (%s,%s,%s,%s)"""
        values = (id_disciplina, id_curso, descricao, id_turma)
        cursor.execute(comando_insert, values)
        connection.commit()
        print("INSERT DISCIPLINA OK: ", values)
        return "Disciplina inserida com sucesso!"
    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record into mobile table", error)
        return "Não foi possível cadastrar disciplinas!"
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

##########################################################################################################################################################


################################################################# INSERT FACT ACESSO #################################################################
def insertFactAcesso(id_usuario, data_login, data_logoff, origem):
    try:
        connection = conexaoBanco()
        cursor = connection.cursor()
        comando_insert = """ INSERT INTO fact_acesso (id_usuario, data_login, data_logoff, origem) VALUES (%s,%s,%s,%s)"""
        values = (id_usuario, data_login, data_logoff, origem)
        cursor.execute(comando_insert, values)
        connection.commit()
        print("INSERT FACT ACESSO OK: ", values)
        return "Acesso inserido com sucesso!"
    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record into mobile table", error)
        return "Não foi possível cadastrar acessos!"
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


##########################################################################################################################################################

################################################################# INSERT FACT CHAT - DIM CHAT(NO BANCO ESTÁ ASSIM) #################################################################
def insertFactChat(id_chat, data_inicio, data_fim, quantidade_usuario, descricao, duracao):
    try:
        connection = conexaoBanco()
        cursor = connection.cursor()
        comando_insert = """ INSERT INTO dim_chat (id_chat, data_inicio, data_fim, quantidade_usuario, descricao, duracao) VALUES (%s,%s,%s,%s, %s, %s)"""
        values = (id_chat, data_inicio, data_fim, quantidade_usuario, descricao, duracao)
        cursor.execute(comando_insert, values)
        connection.commit()
        print("INSERT FACT CHAT OK: ", values)
        return "Chat inserido com sucesso!"
    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record into mobile table", error)
        return "Não foi possível cadastrar chat!"
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

##########################################################################################################################################################

################################################################# INSERT FACT USUARIO CHAT #################################################################

def insertFactUsuarioChat(id_usuario_chat, id_usuario, id_chat, data_login, data_logoff, quantidade_mensagens, data_ultima_msg, tempo_participacao):
    try:
        connection = conexaoBanco()
        cursor = connection.cursor()
        comando_insert = """ INSERT INTO fact_usuario_chat (id_usuario_chat, id_usuario, id_chat, data_login, data_logoff, quantidade_mensagens, data_ultima_msg, tempo_participacao) VALUES (%s,%s,%s,%s, %s, %s, %s, %s)"""
        values = (id_usuario_chat, id_usuario, id_chat, data_login, data_logoff, quantidade_mensagens, data_ultima_msg,
                  tempo_participacao)
        cursor.execute(comando_insert, values)
        connection.commit()
        print("INSERT FACT USUARIO CHAT OK: ", values)
        return "Usuario Chat inserido com sucesso!"
    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record into mobile table", error)
        return "Não foi possível cadastrar usuario chat!"
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
##########################################################################################################################################################

