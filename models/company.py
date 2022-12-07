import uuid
from typing import Optional, List
from pydantic import BaseModel, EmailStr, Field


class Empresa(BaseModel):

    CompanyId: str = Field(default_factory=uuid.uuid4,alias="_id")
    CompanyId: str = Field(default_factory=uuid.uuid4)
    CompanyName: str
    Email: EmailStr 

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                    "CompanyName": "Test company",
                    "Email": "company.mail@gmail.com"
                }
        }

class EmpresaUpdate(BaseModel):

    CompanyName:Optional[str]
    Email: Optional[EmailStr] 

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
                "example": {
                    "CompanyName": "Test company",
                    "Email": "company.mail@gmail.com"
                
                }
        }

    

