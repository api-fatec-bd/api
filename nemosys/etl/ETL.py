from .mongoConnection import mongoConnection
from .models import DimUsuario, FactLoginPlataforma, DimCurso,  DimAula, DimDisciplina, DimTurma
from datetime import datetime, timedelta
from django.utils.timezone import make_aware


# return today's and yesterday's date at 00:00:00
def etldates():
    t = datetime.today()
    y = t - timedelta(days=1)
    today = datetime.strptime(t.strftime('%Y-%m-%d'), '%Y-%m-%d')
    yesterday = datetime.strptime(y.strftime('%Y-%m-%d'), '%Y-%m-%d')
    return today, yesterday


# from: chatDB.rocketchat.users | to: dwDB.public.dim_usuario
def usersETL():
    tday, yday = etldates()
    filters = {"createdAt": {"$gte": yday, "$lt": tday}}
    fields = {"username": 1, "type": 1, "name": 1}

    result = mongoConnection()['rocketchat']['users'].find(filters, fields)
    if result:
        for x in result:
            newuser = DimUsuario()
            newuser.id_usuario = x["_id"]
            newuser.nome_usuario = x["name"]
            newuser.codigo_permissao = 1
            newuser.descricao_permissao = x["type"]
            newuser.save()
            print(x["username"], "ok")
        print("gg wp")
    else:
        print('no new')


# from: chatDB.rocketchat.rocketchat_sessions | to: dwDB.public.fact_login_plataforma
def sessionsETL():
    tday, yday = etldates()
    filters = {"logoutAt": {"$gte": yday, "$lt": tday}}
    # filters = {"logoutAt": {"$exists": "true"}}
    fields = {"userId": 1, "logoutAt": 1, "loginAt": 1}

    result = mongoConnection()['rocketchat']['rocketchat_sessions'].find(filters, fields)
    if result:
        print('ok lets roll')
        for x in result:
            newsession = FactLoginPlataforma()
            user = DimUsuario.objects.get(id_usuario=x["userId"])
            newsession.id_usuario = user
            newsession.data_login = make_aware(x["loginAt"])
            newsession.data_logoff = make_aware(x["logoutAt"])
            newsession.quantidade_acesso = 1
            newsession.save()
            print(x["_id"], "ok")
        print("gg wp")
    else:
        print("no new")


# from: chatDB.Logs.Turma | to: dwDB.public.dim_turma
def classesETL():

    filters = {}
    fields = {"idturma": 1, "idprofessor": 1, "descricao": 1}

    result = mongoConnection()['Logs']['Turma'].find(filters, fields)
    if result:
        print('ok lets roll')
        for x in result:
            newclass = DimTurma()
            newclass.id_turma = x["idturma"]
            newclass.id_professor = x["idprofessor"]
            newclass.descricao = x["descricao"]
            newclass.save()
            print(x["_id"], "ok")
        print("gg wp")
    else:
        print("no new")


# from: chatDB.Logs.Curso | to: dwDB.public.dim_curso
def coursesETL():

    filters = {}
    fields = {"idcurso": 1, "descricao": 1, "graduacao": 1, "duracao": 1}

    result = mongoConnection()['Logs']['Curso'].find(filters, fields)
    if result:
        print('ok lets roll')
        for x in result:
            newcourse = DimCurso()
            newcourse.id_curso = x["idcurso"]
            newcourse.descricao = x["descricao"]
            newcourse.graduacao = x["graduacao"]
            newcourse.duracao = x["duracao"]
            newcourse.save()
            print(x["_id"], "ok")
        print("gg wp")
    else:
        print("no new")


# from: chatDB.Logs.Disciplina | to: dwDB.public.dim_disciplina
def subjectsETL():
    tday, yday = etldates()
    filters = {}
    fields = {"idDisciplina": 1, "idcurso": 1, "idturma": 1, "descricao": 1}

    result = mongoConnection()['Logs']['Disciplina'].find(filters, fields)
    if result:
        print('ok lets roll')
        for x in result:
            newsubject = DimDisciplina()
            newsubject.id_disciplina = x["idDisciplina"]

            course = DimCurso.objects.get(id_curso=x["idcurso"])
            newsubject.id_curso = course

            class1 = DimTurma.objects.get(id_turma=x["idturma"])
            newsubject.id_turma = class1

            newsubject.descricao = x["descricao"]
            newsubject.save()
            print(x["_id"], "ok")
        print("gg wp")
    else:
        print("no new")


# from: chatDB.Logs.Aula | to: dwDB.public.dim_aula
def lessonsETL():
    filters = {}
    # filters = {"logoutAt": {"$exists": "true"}}
    fields = {"idAula": 1, "DateInicio": 1, "dateFim": 1, "idDisciplina": 1, "Titulo": 1, "Assunto": 1}

    result = mongoConnection()['Logs']['Aula'].find(filters, fields)
    if result:
        print('ok lets roll')
        for x in result:
            newlesson = DimAula()
            newlesson.id_aula = x["idAula"]

            newlesson.data_inicio = datetime.fromisoformat(x["DateInicio"])
            newlesson.data_fim = datetime.fromisoformat(x["dateFim"])

            subject = DimDisciplina.objects.get(id_disciplina=x["idDisciplina"])
            newlesson.id_disciplina = subject

            newlesson.titulo = x["Titulo"][:45]
            newlesson.assunto = x["Assunto"][:100]
            newlesson.duracao = (datetime.strptime(x["dateFim"], "%Y-%m-%d %H:%M:%S") - datetime.strptime(x["DateInicio"], "%Y-%m-%d %H:%M:%S")).total_seconds() / 60.0
            newlesson.save()
            print(x["_id"], "ok")
        print("gg wp")
    else:
        print("no new")
