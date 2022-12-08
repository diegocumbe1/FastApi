import uuid
from typing import Optional, List
from pydantic import BaseModel, EmailStr, Field
from enum import Enum

# de ser necesario agregar mas tecnologias al enum, estas son de prueba

class Tecnology(Enum):
    Python = "Python"
    Flask = "Flask"
    HTML = "HTML"
    NoSQL = "NoSQL"
    Node = "Node"
    SQL = "SQL"
    JavaScript = "JavaScript"
    TypeScript = "TypeScript"

class Skills(BaseModel):
    NameSkill: Tecnology
    YearsPreviousExperience: int




class Usuarios(BaseModel):

    UserId: str = Field(default_factory=uuid.uuid4,alias="_id")
    UserId: str = Field(default_factory=uuid.uuid4)
    FirstName: str
    LastName: str
    Email: EmailStr 
    YearsPreviousExperience: int 
    Skills: List[Skills]

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "FirstName": "Test Name",
                "LastName": "Test Last Name",
                "Email": "un.test.no.hace.mal@gmail.com",
                "YearsPreviousExperience": 5,
                "Skills":[
                    {
                        "NameSkill":"Python",
                        "YearsPreviousExperience": 1
                    },
                    {
                        "NameSkill":"NoSQL",
                        "YearsPreviousExperience": 2
                    }
                ]
            }
        }

class UsersUpdate(BaseModel):

    FirstName: Optional[str]
    LastName: Optional[str]
    Email: Optional[EmailStr] 
    YearsPreviousExperience: Optional[int] 
    Skills: Optional[List]

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
                "example": {
                    "FirstName": "Test Name update",
                    "LastName": "Test Last Nameupdate",
                    "Email": "un.test.no.hace.mal.update@gmail.com",
                    "YearsPreviousExperience": 5,
                    "Skills":[
                    {
                        "NameSkill":"Python",
                        "YearsPreviousExperience": 1
                    },
                    {
                        "NameSkill":"NoSQL",
                        "YearsPreviousExperience": 2
                    }
                ]
            }
        }

    

