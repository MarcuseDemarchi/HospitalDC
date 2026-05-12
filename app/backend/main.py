from fastapi import FastAPI

from app.backend.infra.database.database import engine
from app.backend.infra.database import models

from app.backend.routes.rt_pacientes import router as patient_router

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(patient_router)

@app.get("/")
def home():
    return {
        "message": "Hospital API Running"
    }