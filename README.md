# Hospital DC - Sistema de Gestao Hospitalar

Este projeto foi desenvolvido como parte do Trabalho 02 da disciplina de desenvolvimento de sistemas. Trata-se de uma aplicacao Full Stack para gerenciamento de triagem e fila de pacientes em um pequeno hospital com suporte a prioridade.

## Tecnologias Utilizadas

- Frontend: React.js (SPA) com Axios para consumo de API.
- Backend: Python com FastAPI.
- Banco de Dados: PostgreSQL 15.
- Infraestrutura: Docker e Docker Compose para orquestracao de containers.
- ORM: SQLAlchemy para mapeamento objeto-relacional.

## Arquitetura do Projeto

A solucao foi estruturada em tres servicos principais rodando em containers separados:

1. Banco de Dados (db): Container Postgres com volume persistente para garantir que os dados nao sejam perdidos ao reiniciar o sistema.
2. API Backend (backend): Desenvolvida em FastAPI, responsavel pela logica de negocio e persistencia no banco.
3. Frontend (frontend): Aplicacao React servida por um servidor Nginx (em modo de producao via Docker).

### Estrutura de Pastas Obrigatoria
```
projeto/
├── app/
│   ├── backend/        # Codigo Python / FastAPI
│   └── frontend/       # Codigo React
├── Dockerfile.backend  # Build da imagem da API
├── Dockerfile.frontend # Build da imagem do React (Nginx)
├── docker-compose.yml  # Orquestracao dos containers
├── README.md           # Documentacao do projeto
└── evidencias/         # Prints das etapas de execucao
```

## Como Executar o Projeto

Certifique-se de ter o Docker e o Docker Compose instalados em sua maquina.

IMPORTANTE: Como houve alteracao na estrutura do banco (adicao da coluna de prioridade), se voce ja rodou o projeto antes, recomendo limpar o volume antigo:
```
docker compose down -v
```

Para iniciar:
1. Clone o repositorio.
2. Na raiz do projeto, execute o comando:
    ```
    docker compose up --build
    ```
3. Acesse as interfaces:
    - Frontend: [http://localhost:3000](http://localhost:3000)
    - API (Swagger): [http://localhost:8000/docs](http://localhost:8000/docs)

## Funcionalidades (CRUD)

- Cadastrar Paciente: Formulario para adicionar nome, idade, sintomas e nivel de prioridade a fila.
- Listar Pacientes: Visualizacao em tempo real da fila, com pacientes prioritarios no topo.
- Editar Paciente: Permite alterar os dados ou a prioridade de um paciente ja cadastrado.
- Dar Alta (Deletar): Botao para remover o paciente da fila apos o atendimento.

---