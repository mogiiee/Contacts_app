from fastapi import FastAPI
import crud,responses
from pydantic import BaseModel
from typing import Union
from fastapi.encoders import jsonable_encoder
from bson.objectid import ObjectId




app = FastAPI()

class details(BaseModel):
    first_name: str
    last_name: Union[str, None] = None
    phone_number: int = None

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/inserter")
async def inserter(item: details):
    payload = jsonable_encoder(item)

    try:
        crud.insterter(payload)
        print(type(payload))
        return responses.ResponseStruct(True, "Inserted" , str(item))
    except Exception as e:
        return responses.ResponseStruct(False, str(e),None)


@app.get("/get_all_data")
async def Get_all_data():
    response = crud.get_all_data()
    return responses.ResponseStruct(True, None,str(response))



@app.patch("/update")
async def update(id, item : details):
    crud.updater({'_id':ObjectId(id)},{'$set':{'first_name':item.first_name, 'last_name': item.last_name, "phone_number": item.phone_number}})
    return responses.ResponseStruct(True, " changed ",id + " changed to " + str(item))



@app.delete("/delete_one")
async def delete_one(id):
    crud.deleter(id)
    return responses.ResponseStruct(True, "deleted", id)



@app.delete("/delete_all")
async def reset():
    crud.delete_all()
