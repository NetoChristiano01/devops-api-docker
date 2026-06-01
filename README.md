# devops-api-docker

API REST desenvolvida em Python e containerizada com Docker, com pipeline de CI/CD automatizado via GitHub Actions.

## 🚀 Sobre o projeto

Projeto prático de DevOps que demonstra a construção e deploy de uma API REST utilizando boas práticas de desenvolvimento moderno: containerização com Docker, orquestração com Docker Compose e automação de pipeline com GitHub Actions.

## 🛠️ Tecnologias utilizadas

- **Python** — desenvolvimento da API REST
- **Docker** — containerização da aplicação
- **Docker Compose** — orquestração dos serviços
- **GitHub Actions** — pipeline CI/CD automatizado

## 📁 Estrutura do projeto

```
devops-api-docker/
├── .github/
│   └── workflows/       # Pipeline CI/CD (GitHub Actions)
├── app.py               # Aplicação principal da API
├── Dockerfile           # Configuração do container
├── docker-compose.yml   # Orquestração dos serviços
└── requirements.txt     # Dependências Python
```

## ▶️ Como executar

**Pré-requisitos:** Docker e Docker Compose instalados.

```bash
# Clone o repositório
git clone https://github.com/NetoChristiano01/devops-api-docker.git
cd devops-api-docker

# Suba os containers
docker-compose up --build
```

A API estará disponível em `http://localhost:5000`

## 🔄 Pipeline CI/CD

O projeto conta com pipeline automatizado via GitHub Actions que executa a cada push na branch `main`, garantindo a integridade da aplicação.

## 👨‍💻 Autor

**Christiano Vaz Neto**  
[LinkedIn](https://www.linkedin.com/in/christiano-vaz-neto-35b141237) · [GitHub](https://github.com/NetoChristiano01)
