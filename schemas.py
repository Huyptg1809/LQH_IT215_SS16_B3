from pydantic import BaseModel, Field
from typing import List

class RegistrationInput(BaseModel):
    student_id: int
    workshop_id: int

class WorkshopBasic(BaseModel):
    id: int
    title: str

    class Config:
        from_attributes = True

class StudentBasic(BaseModel):
    id: int
    full_name: str

    class Config:
        from_attributes = True

class OutputStudentWorkshops(BaseModel):
    student_id: int = Field(validation_alias="id")
    full_name: str
    workshops: List[WorkshopBasic]

    class Config:
        from_attributes = True
        populate_by_name = True

class OutputWorkshopStudents(BaseModel):
    workshop_id: int = Field(validation_alias="id")
    title: str
    students: List[StudentBasic]

    class Config:
        from_attributes = True
        populate_by_name = True
