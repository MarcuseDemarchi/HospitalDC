from sqlalchemy import Column, Integer, String, Boolean
from app.backend.infra.database.database import Base

class Paciente(Base):
    __tablename__ = "tbpacientes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    disease = Column(String, nullable=False)
    priority = Column(Boolean, default=False)
