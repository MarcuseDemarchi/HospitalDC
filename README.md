# Sistema de Gestão Hospitalar - Hospital DC

Este projeto foi desenvolvido como o **Trabalho 02** da disciplina de Desenvolvimento de Sistemas. O objetivo é fornecer uma solução funcional de triagem para um pequeno hospital, utilizando tecnologias modernas de desenvolvimento Web e Cloud (Docker).

---

## Guia de Início Rápido (Do Zero)

Siga os passos abaixo para configurar e rodar o projeto em um computador que não possui as ferramentas instaladas.

### 1. Pré-requisitos
Antes de começar, você precisará instalar duas ferramentas fundamentais:
- **Git:** Para baixar o código do projeto. [Baixe aqui](https://git-scm.com/downloads).
- **Docker Desktop:** Para rodar os containers (inclui o Docker Compose). [Baixe aqui](https://www.docker.com/products/docker-desktop/).

> **Nota para Windows/Mac:** Após instalar o Docker Desktop, certifique-se de que ele está aberto e rodando (ícone da baleia na barra de tarefas).

### 2. Clonando o Projeto
Abra o seu terminal (CMD, PowerShell ou Terminal do Linux) e execute:
```
git clone https://github.com/MarcuseDemarchi/HospitalDC.git
cd HospitalDC
```

### 3. Executando o Sistema (Via Docker Hub)
Este projeto já possui imagens pré-construídas e hospedadas no **Docker Hub**. Isso permite que você rode o sistema completo sem precisar compilar o código localmente.

No terminal, dentro da pasta do projeto, execute:
```
docker-compose up -d
```

O Docker irá baixar automaticamente as seguintes imagens:
- `marcusedemarchi/hospitaldc:backend` (API FastAPI)
- `marcusedemarchi/hospitaldc:frontend` (Interface React)
- `postgres:15` (Banco de Dados)

---

## Como Acessar

Após o comando acima finalizar, o sistema estará disponível em:

- **Frontend (Interface do Usuário):** [http://localhost:3000](http://localhost:3000)
- **Backend (Documentação Swagger/API):** [http://localhost:8000/docs](http://localhost:8000/docs)

---

## Detalhes Técnicos para Validação

Este projeto atende aos seguintes requisitos técnicos exigidos:

### 1. Orquestração Multi-container
Utilizamos o **Docker Compose** para gerenciar três serviços independentes:
- **Banco de Dados (PostgreSQL):** Armazena os dados dos pacientes.
- **Backend (Python/FastAPI):** Lógica de negócio e conexão com o banco via SQLAlchemy.
- **Frontend (React):** Interface SPA consumindo a API.

### 2. Persistência de Dados
Configuramos um **Volume Nomeado** (`postgres_data`) no Docker. Isso garante que, mesmo que os containers sejam removidos ou o computador reiniciado, os dados dos pacientes permaneçam salvos no disco rígido do host.

### 3. Redes (Networking)
Os containers estão conectados através de uma rede interna chamada `hospital_network`. O backend comunica-se com o banco de dados usando o nome do serviço (`db`) em vez de IPs fixos, seguindo as melhores práticas de Docker.

### 4. Variáveis de Ambiente
As credenciais do banco de dados (usuário, senha e nome do banco) não estão "hardcoded" no código. Elas são definidas no `docker-compose.yml` e injetadas no backend via variáveis de ambiente (`DATABASE_URL`).

---

## Estrutura do Repositório
```
HospitalDC/
├── app/
│   ├── backend/        # Código Fonte Python (FastAPI)
│   └── frontend/       # Código Fonte React (TypeScript/JS)
├── Dockerfile.backend  # Instruções para criar a imagem do servidor
├── Dockerfile.frontend # Instruções para criar a imagem da interface
├── docker-compose.yml  # Orquestrador de todos os serviços
├── GEMINI.md           # Contexto e regras do projeto
└── evidencias/         # Prints de execução (conforme solicitado)
```

## Comandos Úteis

- **Parar o sistema:** `docker-compose stop`
- **Remover os containers:** `docker-compose down`
- **Limpar TUDO (inclusive os dados do banco):** `docker-compose down -v`
- **Recompilar localmente (caso altere o código):** `docker-compose up --build`

---
**Desenvolvido por:** Marcus De Marchi
**Disciplina:** Trabalho 02 - Faculdade