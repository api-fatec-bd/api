# users filter
def usersFilter(tday, yday, mongoConnection):
    filters = {"createdAt": {"$gte": yday, "$lt": tday}}
    fields = {"username": 1, "type": 1, "name": 1}

    return mongoConnection['rocketchat']['users'].find(filters, fields)
