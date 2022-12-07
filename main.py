
from fastapi import FastAPI
from dotenv import dotenv_values
from pymongo import MongoClient
from routes.user import user as user_route
from routes.vacancy import vacancy as vacancy_route
from routes.company import company as company_route

config = dotenv_values(".env")

app = FastAPI()


@app.on_event("startup")
def startup_db_client():
    app.mongodb_client = MongoClient(config["ATLAS_URI"])
    app.database = app.mongodb_client[config["DB_NAME"]]

@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()

app.include_router(user_route, tags=["users"], prefix="/user")
app.include_router(vacancy_route, tags=["vacancies"], prefix="/vacancy")
app.include_router(company_route, tags=["companies"], prefix="/company")
