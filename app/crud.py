from . import database, responses
from bson.objectid import ObjectId


def insterter(metadata):
    database.collection.insert_one(metadata)
    return metadata
    

def deleter(id):
    database.collection.delete_one({'_id':ObjectId(id)})
    return responses.ResponseStruct(True, "deleted", None)


def updater(WrongValue,CorrectValue):
    database.collection.update_one(WrongValue,CorrectValue, upsert =True)


def get_all_data():
    response =database.collection.find({})
    li_response = list(response)
    return li_response


def delete_all():
    database.collection.delete_many({})

