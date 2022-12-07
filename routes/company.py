from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from config.db import conn

from models.company import *


company = APIRouter()

@company.get("/", response_description="Get all companies", response_model=List[Empresa])
def find_all_companies(request: Request):
    companies = list(request.app.database["companies"].find())
    return companies

@company.get("/{companyId}", response_description="Get a single companyr by id", response_model=Empresa)
def find_company(companyId: str, request: Request):
    if (company := request.app.database["companies"].find_one({"companyId": companyId})) is not None:
        return company

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"companyId with companyId {companyId} not found")

@company.post("/create", response_description="Create a new company", status_code=status.HTTP_201_CREATED, response_model=Empresa)
def create_company(request:Request, company: Empresa = Body(...)):
    company = jsonable_encoder(company)
    new_company = request.app.database["companies"].insert_one(company)
    create_company = request.app.database["companies"].find_one({"_id":new_company.inserted_id})
    return create_company

@company.put("/update/{companyId}", response_description="Update a company", response_model=Empresa)
def update_company(companyId: str, request:Request, company: EmpresaUpdate = Body(...)):
    company = {k: v for k, v in company.dict().items() if v is not None}

    if len(company) >=1:
        update_result = request.app.database["companies"].update_one({"companyId": companyId}, {"$set": company})

        if update_result.modified_count == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"company with companyId {companyId} not found")
    
    if (
        existing_company := request.app.database["companies"].find_one({"companyId": companyId})
    ) is not None:
        return existing_company
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"company with companyId {companyId} not found")


    


@company.delete("/delete/{companyId}", response_description="delete a company")
def delete_company(companyId: str, request: Request, response: Response):
    delete_result = request.app.database["companies"].delete_one({"companyId": companyId})

    if delete_result.deleted_count == 1:
        response.status_code = status.HTTP_204_NO_CONTENT
        return  "company deleted sucesfully, {response.status_code}"

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with companyId {companyId} not found")