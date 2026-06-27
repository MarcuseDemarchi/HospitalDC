"""
API REST - Sistema de Gestão Hospitalar (Hospital DC)
Trabalho Final - Cloud Computing - UNIDAVI
Aluno: Marcus De Marchi

Esta API fornece endpoints para consulta de pacientes internados,
servindo como camada de dados simulados para fins acadêmicos.
Os dados são carregados de um arquivo JSON externo (data/pacientes.json).
"""

import json
import os
from fastapi import FastAPI
from fastapi.responses import JSONResponse

# Inicialização da aplicação FastAPI
app = FastAPI(
    title="Hospital DC API",
    description="API REST para gestão de pacientes do Hospital DC",
    version="1.0.0"
)

# Caminho para o arquivo de dados simulados
DATA_PATH = os.path.join(os.path.dirname(__file__), "data", "pacientes.json")


def carregar_pacientes() -> list:
    """Carrega a lista de pacientes do arquivo JSON externo."""
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


# ─────────────────────────────────────────────
# ROTA 1: GET /status
# Retorna informações de saúde da aplicação
# ─────────────────────────────────────────────
@app.get("/status")
def get_status():
    """
    Endpoint de health check da API.
    Retorna nome, versão e status atual da aplicação.
    """
    return JSONResponse(
        status_code=200,
        content={
            "nome": "Hospital DC API",
            "versao": "1.0.0",
            "status": "online",
            "descricao": "API de gestão de pacientes do Hospital DC"
        }
    )


# ─────────────────────────────────────────────
# ROTA 2: GET /pacientes
# Retorna todos os pacientes cadastrados
# ─────────────────────────────────────────────
@app.get("/pacientes")
def get_pacientes():
    """
    Retorna a lista completa de pacientes internados.
    Os dados são carregados do arquivo data/pacientes.json.
    """
    try:
        pacientes = carregar_pacientes()
        return JSONResponse(
            status_code=200,
            content={
                "total": len(pacientes),
                "pacientes": pacientes
            }
        )
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"erro": "Erro interno ao carregar pacientes", "detalhe": str(e)}
        )


# ─────────────────────────────────────────────
# ROTA 3: GET /pacientes/{id}
# Retorna um único paciente pelo ID
# ─────────────────────────────────────────────
@app.get("/pacientes/{paciente_id}")
def get_paciente_por_id(paciente_id: int):
    """
    Retorna os dados de um paciente específico pelo seu ID.
    Retorna 404 caso o ID não seja encontrado.
    """
    try:
        pacientes = carregar_pacientes()
        # Busca o paciente cujo campo "id" corresponde ao parâmetro recebido
        paciente = next((p for p in pacientes if p["id"] == paciente_id), None)

        if paciente is None:
            return JSONResponse(
                status_code=404,
                content={"erro": f"Paciente com id {paciente_id} não encontrado"}
            )

        return JSONResponse(status_code=200, content=paciente)

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"erro": "Erro interno ao buscar paciente", "detalhe": str(e)}
        )
