from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.backend.infra.database.database import SessionLocal
from app.backend.infra.database.models import Paciente
from app.backend.infra.database.schemas import Patient, PatientCreate, PatientUpdate

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/patients", response_model=Patient)
def create_patient(patient: PatientCreate, db: Session = Depends(get_db)):
    db_patient = Paciente(
        name=patient.name,
        age=patient.age,
        disease=patient.disease,
        priority=patient.priority
    )
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient

@router.get("/patients", response_model=List[Patient])
def list_patients(db: Session = Depends(get_db)):
    # Retorna ordenando por prioridade (True primeiro) e depois por ID
    return db.query(Paciente).order_by(Paciente.priority.desc(), Paciente.id.asc()).all()

@router.put("/patients/{patient_id}", response_model=Patient)
def update_patient(patient_id: int, patient_update: PatientUpdate, db: Session = Depends(get_db)):
    db_patient = db.query(Paciente).filter(Paciente.id == patient_id).first()
    if not db_patient:
        raise HTTPException(status_code=404, detail="Paciente nao encontrado")
    
    update_data = patient_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_patient, key, value)
    
    db.commit()
    db.refresh(db_patient)
    return db_patient

@router.delete("/patients/{patient_id}")
def delete_patient(patient_id: int, db: Session = Depends(get_db)):
    db_patient = db.query(Paciente).filter(Paciente.id == patient_id).first()
    if not db_patient:
        raise HTTPException(status_code=404, detail="Paciente nao encontrado")
    db.delete(db_patient)
    db.commit()
    return {"message": "Paciente removido com sucesso"}
