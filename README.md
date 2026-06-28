# Sistema de Gestão Hospitalar — Hospital DC

Este repositório contém o sistema completo do **Hospital DC**, desenvolvido ao longo da disciplina de Cloud Computing da UNIDAVI.

- **Trabalho 02:** Sistema de triagem com Docker, FastAPI e React (pasta `app/`)
- **Trabalho Final:** API REST com testes unitários e pipeline CI/CD (pasta `api/`)

---

## Trabalho Final — API REST com CI/CD

### Sobre a API

A API simula um serviço de consulta de pacientes internados, com dados armazenados em arquivo JSON externo. Foi construída com **Python + FastAPI** e possui pipeline de Integração Contínua configurado via **GitHub Actions**.

### Rotas disponíveis

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | `/status` | Health check da aplicação |
| GET | `/pacientes` | Lista todos os pacientes |
| GET | `/pacientes/{id}` | Retorna um paciente pelo ID |

---

## Como executar localmente

### Pré-requisitos

- Python 3.11+
- pip

### Sem container (direto no Python)

```bash
# Clone o repositório
git clone https://github.com/MarcuseDemarchi/HospitalDC.git
cd HospitalDC

# Instale as dependências
pip install -r api/requirements.txt

# Execute a API
uvicorn api.app:app --reload --port 8080
```

Acesse em: http://localhost:8080

Documentação Swagger: http://localhost:8080/docs

### Com Docker (sistema completo do Trabalho 02)

```bash
docker-compose up -d
```

- Frontend: http://localhost:3000
- Backend completo: http://localhost:8000/docs

---

## Como executar os testes

```bash
# Testes simples
pytest api/tests/test_api.py -v

# Testes com cobertura
pytest api/tests/test_api.py --cov=api --cov-report=term-missing -v
```

---

## Estrutura do repositório

```
HospitalDC/
├── api/                        # Trabalho Final — API REST
│   ├── app.py                  # Código da API (FastAPI)
│   ├── requirements.txt        # Dependências Python
│   ├── data/
│   │   └── pacientes.json      # Dados simulados (12 pacientes)
│   └── tests/
│       └── test_api.py         # 4 testes unitários
├── app/                        # Trabalho 02 — Sistema completo
│   ├── backend/                # FastAPI com PostgreSQL
│   └── frontend/               # React
├── .github/
│   └── workflows/
│       └── ci.yml              # Pipeline GitHub Actions
├── Dockerfile.backend
├── Dockerfile.frontend
├── docker-compose.yml
└── README.md
```

---

## CI/CD — GitHub Actions

O pipeline é acionado automaticamente a cada `push` ou `pull request` na branch `main` e executa:

1. Checkout do código
2. Configuração do Python 3.11
3. Instalação de dependências
4. **Lint com flake8** (etapa adicional)
5. Execução dos 4 testes unitários com pytest
6. Geração e upload do relatório de cobertura

---

**Desenvolvido por:** Marcus De Marchi  
**Disciplina:** Cloud Computing — UNIDAVI  
**Professor:** Prof. Esp. Ademar Perfoll Junior