import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Obtém a URL do banco de dados das variáveis de ambiente
# No Docker Compose, passaremos algo como: postgresql://user:password@db:5432/dbname
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://hospital:hospital@db:5432/hospital")

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()
