from pydantic import BaseModel
from typing import Optional

class PatientBase(BaseModel):
    name: str
    age: int
    disease: str
    priority: bool = False

class PatientCreate(PatientBase):
    pass

class PatientUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    disease: Optional[str] = None
    priority: Optional[bool] = None

class Patient(PatientBase):
    id: int

    class Config:
        from_attributes = True
