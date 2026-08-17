from pydantic import BaseModel, Field


class Student(BaseModel):
    id: int = Field(gt=0)
    name: str
    maths: float = Field(ge=0, le=100)
    physics: float = Field(ge=0, le=100)
    chemistry: float = Field(ge=0, le=100)