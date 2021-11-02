# users filter ROCKETCHAT DATABASE
def rocketUsersFilter(init_date, end_date, mongoConnection):
    filters = {"createdAt": {"$gte": init_date, "$lt": end_date}}
    fields = {"username": 1, "type": 1, "name": 1}

    return mongoConnection['rocketchat']['users'].find(filters, fields)


# users filter LOGS DATABASE
def logsUsersFilter(init_date, end_date, mongoConnection):
    filters = {}
    fields = {"IDUSUARIO": 1, "USERNAME": 1, "CODIGO_PERMISSAO": 1, "DESCRICAO_PERMISSAO":1}

    return mongoConnection['Logs']['Usuario'].find(filters, fields)


def classesFilter(init_date, end_date, mongoConnection):
    filters = {}
    fields = {"idturma": 1, "idprofessor": 1, "descricao": 1}

    return mongoConnection['Logs']['Turma'].find(filters, fields)

def gradesFilter(init_date, end_date, mongoConnection):
    filters = {}
    fields = {"idaluno": 1, "iddisciplina": 1, "data": 1, "notaAvaliacao": 1, "nota": 1}

    return mongoConnection['Logs']['Nota'].find(filters, fields)


def contentFilter(init_date, end_date, mongoConnection):
    filters = {}
    fields = {"id_usuario": 1, "date": 1, "evento": 1, "id_disciplina": 1, "Titulo_Video": 1, "assunto": 1}

    return mongoConnection['Logs']['Baixou'].find(filters, fields)

# aux for content ETL
def auxSubjectsFilter(init_date, end_date, mongoConnection):
    filters = {}
    fields = {"descricao":1}

    return mongoConnection['Logs']['Disciplina'].find(filters, fields)