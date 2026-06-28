"""
Testes Unitários - API Hospital DC
Trabalho Final - Cloud Computing - UNIDAVI

Testes implementados:
  1. test_get_pacientes_retorna_200      → Verifica retorno HTTP 200 em GET /pacientes
  2. test_estrutura_json_pacientes       → Valida presença dos campos obrigatórios no JSON
  3. test_paciente_inexistente_404       → Verifica retorno HTTP 404 para ID inexistente
  4. test_total_pacientes_minimo_dez     → (Autoria própria) Garante que há ao menos 10
                                           registros retornados, conforme requisito acadêmico

Justificativa do 4º teste:
  O requisito do trabalho exige mínimo de 10 registros simulados. Este teste automatiza
  essa verificação, garantindo que o arquivo de dados nunca seja entregue incompleto.
  Em um contexto de CI/CD real, esse tipo de teste de integridade de dados evita que
  deploys ocorram com bases de dados corrompidas ou truncadas.
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))  # noqa: E402

from fastapi.testclient import TestClient  # noqa: E402
from app import app  # noqa: E402

# Cliente de teste do FastAPI (não sobe servidor real, simula requisições HTTP)
client = TestClient(app)


def test_get_pacientes_retorna_200():
    response = client.get("/pacientes")
    assert response.status_code == 200, (
        f"Esperado 200, recebido {response.status_code}"
    )


def test_estrutura_json_pacientes():
    response = client.get("/pacientes")
    dados = response.json()

    # Verifica campos raiz do JSON
    assert "total" in dados, "Campo 'total' ausente na resposta"
    assert "pacientes" in dados, "Campo 'pacientes' ausente na resposta"
    assert isinstance(dados["pacientes"], list), "'pacientes' deve ser uma lista"

    # Campos obrigatórios em cada registro de paciente
    campos_obrigatorios = ["id", "nome", "idade", "diagnostico", "status", "leito"]

    for paciente in dados["pacientes"]:
        for campo in campos_obrigatorios:
            assert campo in paciente, (
                f"Campo obrigatório '{campo}' ausente no paciente: {paciente}"
            )


def test_paciente_inexistente_404():
    response = client.get("/pacientes/9999")
    assert response.status_code == 404, (
        f"Esperado 404 para ID inexistente, recebido {response.status_code}"
    )

    dados = response.json()
    assert "erro" in dados, "Resposta 404 deve conter campo 'erro'"


def test_total_pacientes_minimo_dez():
    response = client.get("/pacientes")
    dados = response.json()

    total_declarado = dados["total"]
    total_real = len(dados["pacientes"])

    # Garante que o contador 'total' bate com o tamanho real da lista
    assert total_declarado == total_real, (
        f"Campo 'total' ({total_declarado}) não corresponde ao tamanho real da lista ({total_real})"
    )

    # Garante o mínimo de 10 registros
    assert total_real >= 10, (
        f"A API deve retornar ao menos 10 pacientes, mas retornou {total_real}"
    )
