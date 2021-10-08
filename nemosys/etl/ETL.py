from .mongoConnection import mongoConnection
from .models import DimUsuario, FactLoginPlataforma
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

    usersdict = mongoConnection()['rocketchat']['users'].find(filters, fields)

    for x in usersdict:
        newuser = DimUsuario()
        newuser.id_usuario = x["_id"]
        newuser.nome_usuario = x["name"]
        newuser.codigo_permissao = 1
        newuser.descricao_permissao = x["type"]
        newuser.save()
        print(x["username"], "ok")

    print("gg wp")

# from: chatDB.rocketchat.rocketchat_sessions | to: dwDB.public.fact_login_plataforma
def sessionsETL():
    tday, yday = etldates()
    filters = {"logoutAt": {"$gte": yday, "$lt": tday}}
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
