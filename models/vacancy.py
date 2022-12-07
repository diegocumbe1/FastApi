import uuid
from typing import Optional, List
from pydantic import BaseModel, Field, HttpUrl


class Vacante(BaseModel):

    VacancyId: str = Field(default_factory=uuid.uuid4,alias="_id")
    PositionName:str
    CompanyName: str
    Salary: int
    Currency: str
    VacancyId: str = Field(default_factory=uuid.uuid4)
    VacancyLink: HttpUrl
    RequiredSkills: List

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                    "PositionName": "Python Dev",
                    "CompanyName": "Test company",
                    "Salary": 9999999,
                    "Currency": "COP",
                    "VacancyLink": "https://www.test.com",
                    "RequiredSkills": [
                        {
                            "Python": 1
                        },
                        {
                            "NoSQL": 2
                        }
                    ]
                }
        }

class VacanteUpdate(BaseModel):

    PositionName:Optional[str]
    CompanyName:Optional[str]
    Salary: Optional[str]
    Currency: Optional[str]
    VacancyLink: Optional[HttpUrl]
    RequiredSkills: List

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
                "example": {
                    "PositionName": "Python Dev update",
                    "CompanyName": "Test company update",
                    "Salary": 9999999,
                    "Currency": "COP",
                    "VacancyLink": "https://www.test.update.com",
                    "RequiredSkills": [
                        {
                            "Python": 1
                        },
                        {
                            "NoSQL": 2
                        }
                    ]
                }
        }

    

