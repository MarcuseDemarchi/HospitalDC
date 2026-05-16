from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.backend.infra.database.database import engine, Base
from app.backend.infra.database import models

from app.backend.routes.rt_pacientes import router as patient_router

# Cria as tabelas no banco de dados
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Hospital Management System API")

# Configuracao do CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(patient_router)

@app.get("/")
def home():
    return {
        "message": "Hospital API Running",
        "docs": "/docs"
    }
