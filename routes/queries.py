from fastapi import APIRouter, Body, Request, HTTPException, status

from models.user import *
from models.vacancy import *


queries = APIRouter()

@queries.get("/availableVacancies/{UserId}", response_description="Get a single userr by id", response_model=List[Vacante])
def find_vacancy(UserId: str, request: Request):
    if (user := request.app.database["users"].find_one({"UserId": UserId})) is not None:
        user = request.app.database["users"].find_one({"UserId": UserId})
        userSkill =user['Skills']
        for u in userSkill:
            skill = u["NameSkill"]
            # experience =u["YearsPreviousExperience"]
            # print('user',skill,experience)
            vacancies = list(request.app.database["vacancies"].find({"$or":[{
                "RequiredSkills.NameSkill":skill,
                # "Skills.YearsPreviousExperience":{"$gte":experience},
                }]}
                ))
        return vacancies

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"userId with UserId {UserId} not found")
        

@queries.get("/user/skill/{skill}/{experience}", response_description="Get a single userr2 by id", response_model=List[Usuarios])
def find_user_bySkill(skill: Tecnology, experience: int,request: Request):
    users = list(request.app.database["users"].find({
        "Skills.NameSkill":skill,
        "Skills.YearsPreviousExperience":{"$gte":experience},

        }))
    return users

@queries.get("/vacancy/skill/{skill}/{experience}", response_description="Get a single userr2 by id", response_model=List[Usuarios])
def find_user_bySkill(skill: Tecnology, experience: int,request: Request):
    users = list(request.app.database["vacancies"].find({
        "RequiredSkills.NameSkill":skill,
        "RequiredSkills.YearsPreviousExperience":{"$gte":experience},

        }))
    return users

