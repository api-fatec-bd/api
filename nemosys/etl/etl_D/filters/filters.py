# users filter - DATABASE: ROCKETCHAT
def rocketUsersFilter(init_date, end_date, mongoConnection):
    filters = {"createdAt": {"$gte": init_date, "$lt": end_date}}
    fields = {"username": 1, "type": 1, "name": 1, "_id": 0}

    return mongoConnection['rocketchat']['users'].find(filters, fields)


# users filter - DATABASE:LOGS
def logsUsersFilter(init_date, end_date, mongoConnection):
    filters = {}
    fields = {"IDUSUARIO": 1, "USERNAME": 1, "CODIGO_PERMISSAO": 1, "DESCRICAO_PERMISSAO":1, "_id": 0}

    return mongoConnection['Logs']['Usuario'].find(filters, fields)


def classesFilter(init_date, end_date, mongoConnection):
    filters = {}
    fields = {"idturma": 1, "idprofessor": 1, "descricao": 1, "_id": 0}

    return mongoConnection['Logs']['Turma'].find(filters, fields)

def gradesFilter(init_date, end_date, mongoConnection):
    filters = {}
    fields = {"idaluno": 1, "iddisciplina": 1, "data": 1, "notaAvaliacao": 1, "nota": 1,  "_id": 0}

    return mongoConnection['Logs']['Nota'].find(filters, fields)


def contentFilter(init_date, end_date, mongoConnection):
    filters = {}
    fields = {"id_usuario": 1, "date": 1, "evento": 1, "id_disciplina": 1, "Titulo_Video": 1, "assunto": 1, "_id": 0}

    return mongoConnection['Logs']['Baixou'].find(filters, fields)

# aux for content ETL
def auxSubjectsFilter(init_date, end_date, mongoConnection):
    filters = {}
    fields = {"descricao":1, "_id": 0}

    return mongoConnection['Logs']['Disciplina'].find(filters, fields)

def matriculationFilter(init_date, end_date, mongoConnection):
    filters = {}
    fields = {"id_usuario": 1, "id_curso": 1, "id_turma ": 1, "_id": 0}

    return mongoConnection['Logs']['Matricula'].find(filters, fields)

#  filters list of 'users class out' events
def userExitClassFilter(init_date, end_date, mongoConnection):
    filters = {"evento":"Saida", "id_usuario": 423}
    fields = {"id_usuario": 1, "date": 1, "id_aula": 1, "_id": 0}

    return mongoConnection['Logs']['Acesso_aula'].find(filters, fields)


#  filters specific 'users class in' events
def userInClassFilter(id_user, id_aula, mongoConnection):
    filters = {"id_usuario": id_user, "id_aula": id_aula, "evento":"Entrada"}
    fields = {"date": 1, "_id": 0}

    return mongoConnection['Logs']['Acesso_aula'].find(filters, fields)