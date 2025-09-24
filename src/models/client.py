from sqlalchemy import Column, Integer, String, Date, Enum as SQLAlchemyEnum
from services.database import Base
from pydantic import BaseModel, constr, PastDate
from enum import Enum


class ITRole(str, Enum):
    SOFTWARE_ENGINEER = "Software Engineer"
    DEVOPS_ENGINEER = "DevOps Engineer"
    DATA_SCIENTIST = "Data Scientist"
    PRODUCT_MANAGER = "Product Manager"
    UX_UI_DESIGNER = "UX/UI Designer"
    QA_ENGINEER = "QA Engineer"
    SYSTEM_ADMINISTRATOR = "System Administrator"


class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    birth_date = Column(Date)
    role = Column(SQLAlchemyEnum(ITRole))


class ClientCreate(BaseModel):
    name: constr(min_length=1)
    birth_date: PastDate
    role: ITRole

    class Config:
        orm_mode = True


class ClientUpdate(ClientCreate):
    pass