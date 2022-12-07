from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder

from models.vacancy import *


vacancy = APIRouter()

@vacancy.get("/", response_description="Get all vacancy", response_model=List[Vacante])
def find_all_vacancies(request: Request):
    vacancies = list(request.app.database["vacancies"].find())
    return vacancies

@vacancy.get("/{vacancyId}", response_description="Get a single vacancyr by id", response_model=Vacante)
def find_vacancy(vacancyId: str, request: Request):
    if (vacancy := request.app.database["vacancies"].find_one({"vacancyId": vacancyId})) is not None:
        return vacancy

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"vacancyId with vacancyId {vacancyId} not found")

@vacancy.post("/create", response_description="Create a new vacancy", status_code=status.HTTP_201_CREATED, response_model=Vacante)
def create_vacancy(request:Request, vacancy: Vacante = Body(...)):
    vacancy = jsonable_encoder(vacancy)
    new_vacancy = request.app.database["vacancies"].insert_one(vacancy)
    create_vacancy = request.app.database["vacancies"].find_one({"_id":new_vacancy.inserted_id})
    return create_vacancy

@vacancy.put("/update/{vacancyId}", response_description="Update a vacancy", response_model=Vacante)
def update_vacancy(vacancyId: str, request:Request, vacancy: VacanteUpdate = Body(...)):
    vacancy = {k: v for k, v in vacancy.dict().items() if v is not None}

    if len(vacancy) >=1:
        update_result = request.app.database["vacancies"].update_one({"vacancyId": vacancyId}, {"$set": vacancy})

        if update_result.modified_count == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"vacancy with vacancyId {vacancyId} not found")
    
    if (
        existing_vacancy := request.app.database["vacancies"].find_one({"vacancyId": vacancyId})
    ) is not None:
        return existing_vacancy
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"vacancy with vacancyId {vacancyId} not found")


    


@vacancy.delete("/delete/{vacancyId}", response_description="delete a vacancy")
def delete_vacancy(vacancyId: str, request: Request, response: Response):
    delete_result = request.app.database["vacancies"].delete_one({"vacancyId": vacancyId})

    if delete_result.deleted_count == 1:
        response.status_code = status.HTTP_204_NO_CONTENT
        return  "vacancy deleted sucesfully, {response.status_code}"

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with vacancyId {vacancyId} not found")