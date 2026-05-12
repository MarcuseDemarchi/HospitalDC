from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.backend.infra.database.database import SessionLocal
from app.backend.infra.database.models import paciente
from app.backend.infra.database.schemas import PatientCreate

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/patients")
def create_patient(
    patient: PatientCreate,
    db: Session = Depends(get_db)
):
    db_patient = paciente(**patient.dict())

    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)

    return db_patient

@router.get("/patients")
def list_patients(db: Session = Depends(get_db)):
    return db.query(paciente).all()
