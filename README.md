# Hospital DC — API REST

Sistema de gestão de pacientes desenvolvido como Trabalho Final da disciplina de Cloud Computing — UNIDAVI.

**Aluno:** Marcus De Marchi  
**Professor:** Prof. Esp. Ademar Perfoll Junior

---

## Pré-requisitos

| Método | O que precisa |
|--------|--------------|
| Manual | Python 3.10+ e pip |
| Docker | Docker instalado e rodando |

---

## Execução manual (sem Docker)

```bash
# 1. Clone o repositório
git clone https://github.com/MarcuseDemarchi/HospitalDC.git
cd HospitalDC

# 2. Crie e ative o ambiente virtual
python3 -m venv venv
source venv/bin/activate        # Linux/Mac
# venv\Scripts\activate         # Windows

# 3. Instale as dependências
pip install -r api/requirements.txt

# 4. Suba a API
uvicorn api.app:app --reload --port 8080
```

Acesse: http://localhost:8080  
Documentação Swagger: http://localhost:8080/docs

---

## Execução com Docker

```bash
# 1. Clone o repositório
git clone https://github.com/MarcuseDemarchi/HospitalDC.git
cd HospitalDC

# 2. Build da imagem
docker build -t hospitaldc-api .

# 3. Sobe o container
docker run -p 8080:8080 hospitaldc-api
```

Acesse: http://localhost:8080  
Documentação Swagger: http://localhost:8080/docs

Para rodar em segundo plano:
```bash
docker run -d -p 8080:8080 --name hospitaldc hospitaldc-api
```

Para parar:
```bash
docker stop hospitaldc
```

---

## Rotas da API

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | `/status` | Health check da API |
| GET | `/pacientes` | Lista todos os pacientes |
| GET | `/pacientes/{id}` | Retorna um paciente pelo ID |

---

## Executar os testes

```bash
# Com ambiente virtual ativado:
python3 -m pytest api/tests/test_api.py -v

# Com cobertura:
python3 -m pytest api/tests/test_api.py --cov=api --cov-report=term-missing -v
```

---

## Estrutura do repositório

```
HospitalDC/
├── api/
│   ├── app.py                  # Código da API (FastAPI)
│   ├── requirements.txt        # Dependências Python
│   ├── data/
│   │   └── pacientes.json      # Dados simulados (12 pacientes)
│   └── tests/
│       └── test_api.py         # 4 testes unitários
├── .github/
│   └── workflows/
│       └── ci.yml              # Pipeline GitHub Actions
├── evidencias/                 # Prints de execução
├── Dockerfile                  # Imagem Docker da API
└── README.md
```

---

## CI/CD

O pipeline GitHub Actions roda automaticamente a cada `push` na branch `main`:

1. Checkout do código
2. Configura Python 3.11
3. Instala dependências
4. Lint com flake8
5. Executa os 4 testes com pytest
6. Gera relatório de cobertura
