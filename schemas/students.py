def serializeDict(item) -> dict:
    return {
        "id": str(item["_id"]),
        "name": item["name"],
        "age": item["age"],
        "address": item["address"],
    }

def serializeList(entity) -> list:
    return [serializeDict(item) for item in entity]