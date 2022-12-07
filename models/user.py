import uuid
from typing import Optional, List
from pydantic import BaseModel, EmailStr, Field


class Usuarios(BaseModel):

    UserId: str = Field(default_factory=uuid.uuid4,alias="_id")
    UserId: str = Field(default_factory=uuid.uuid4)
    FirstName: str
    LastName: str
    Email: EmailStr 
    YearsPreviousExperience: int 
    Skills: List

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
                    "Python": 1
                    },
                    {
                    "NoSQL": 2
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
                        "Python": 1
                        },
                        {
                        "NoSQL": 2
                        }
                    ]
            }
        }

    

