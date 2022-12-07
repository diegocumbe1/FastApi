from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from config.db import conn

from models.user import *


user = APIRouter()

@user.get("/", response_description="Get all users", response_model=List[Usuarios])
def find_all_users(request: Request):
    users = list(request.app.database["users"].find())
    return users

@user.get("/{UserId}", response_description="Get a single userr by id", response_model=Usuarios)
def find_user(UserId: str, request: Request):
    if (user := request.app.database["users"].find_one({"UserId": UserId})) is not None:
        return user

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"userId with UserId {UserId} not found")

@user.post("/create", response_description="Create a new user", status_code=status.HTTP_201_CREATED, response_model=Usuarios)
def create_user(request:Request, user: Usuarios = Body(...)):
    user = jsonable_encoder(user)
    new_user = request.app.database["users"].insert_one(user)
    create_user = request.app.database["users"].find_one({"_id":new_user.inserted_id})
    return create_user

@user.put("/update/{UserId}", response_description="Update a user", response_model=Usuarios)
def update_user(UserId: str, request:Request, user: UsersUpdate = Body(...)):
    user = {k: v for k, v in user.dict().items() if v is not None}

    if len(user) >=1:
        update_result = request.app.database["users"].update_one({"UserId": UserId}, {"$set": user})

        if update_result.modified_count == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with UserId {UserId} not found")
    
    if (
        existing_user := request.app.database["users"].find_one({"UserId": UserId})
    ) is not None:
        return existing_user
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with UserId {UserId} not found")


    


@user.delete("/delete/{UserId}", response_description="delete a user")
def delete_user(UserId: str, request: Request, response: Response):
    delete_result = request.app.database["users"].delete_one({"UserId": UserId})

    if delete_result.deleted_count == 1:
        response.status_code = status.HTTP_204_NO_CONTENT
        return  "User deleted sucesfully, {response.status_code}"

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with UserId {UserId} not found")