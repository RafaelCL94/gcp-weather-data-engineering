# GCP Weather Data Engineering Pipeline

Este projeto implementa um **pipeline completo de engenharia de dados**, responsável por coletar, transformar e armazenar dados meteorológicos em nuvem, utilizando **Python** e **Google Cloud Platform (GCP)**. O foco é em simular um pipeline real de dados climáticos para fins de estudo e portfólio em Engenharia de Dados

O objetivo é simular um cenário real de ingestão contínua de dados, aplicando boas práticas de ETL/ELT, organização de código e versionamento.

---

## 🎯 Objetivo do Projeto

- Consumir dados climáticos de uma API pública
- Estruturar e padronizar os dados coletados
- Manter histórico incremental de medições
- Armazenar os dados em um data warehouse (BigQuery)
- Criar uma base pronta para análises e dashboards

---

## 🛠️ Tecnologias Utilizadas

- **Python 3**
- **OpenWeather API**
- **Google Cloud Platform (GCP)**
  - BigQuery
  - Cloud SDK
- **Git / GitHub**
- Bibliotecas Python:
  - `requests`
  - `pandas`
  - `python-dotenv`
  - `google-cloud-bigquery`

---

## 🧱 Arquitetura do Pipeline

O pipeline foi estruturado seguindo um fluxo simples e realista de engenharia de dados:

1. **Ingestão**  
   Coleta de dados meteorológicos atuais de cidades brasileiras por meio da API OpenWeather.

2. **Processamento**  
   Tratamento, normalização e padronização dos dados, transformando o retorno da API em um formato tabular e analítico.

3. **Carga**  
   Armazenamento dos dados tratados no BigQuery, mantendo histórico incremental das medições.

Fluxo resumido:


OpenWeather API
↓
Ingestão (Python)
↓
Transformação (Pandas)
↓
Carga (BigQuery)


---

## 📁 Estrutura do Projeto


gcp-weather-data-engineering/
│
├── ingestion/
│ └── extract_weather.py # Coleta dados da API
│
├── load/
│ └── load_bigquery.py # Carga dos dados no BigQuery
│
├── sql/
│ └── create_table.sql # Script SQL auxiliar (opcional)
│
├── .env.example # Exemplo de variáveis de ambiente
├── .gitignore
├── requirements.txt
├── run_pipeline.py # Orquestra a execução do pipeline
├── run_pipeline.bat # Execução no Windows
└── README.md


---

## ⚙️ Pré-requisitos

- Python 3.9 ou superior  
- Conta ativa no Google Cloud Platform  
- Projeto configurado no GCP  
- Acesso à API OpenWeather  
- Git instalado  

---

## 🔐 Variáveis de Ambiente

As credenciais sensíveis não são versionadas.

1. Copie o arquivo `.env.example`
2. Renomeie para `.env`
3. Preencha com suas credenciais:


OPENWEATHER_API_KEY=sua_api_key
GCP_PROJECT_ID=seu_project_id

---

## 🚀 Como Executar o Projeto

### 1. Clonar o repositório
```bash
git clone https://github.com/RafaelCL94/gcp-weather-data-engineering.git
cd gcp-weather-data-engineering
2. Criar e ativar o ambiente virtual (opcional, recomendado)
python -m venv venv

Ativar no Windows:

venv\Scripts\activate
3. Instalar dependências
pip install -r requirements.txt
4. Autenticar no Google Cloud
gcloud auth login
gcloud auth application-default login
gcloud config set project SEU_PROJECT_ID
5. Executar o pipeline
python run_pipeline.py

📊 Dados Armazenados no BigQuery
Os dados são carregados de forma incremental na tabela weather.weather_history, com campos como:

Cidade e país
Temperatura atual, mínima e máxima
Sensação térmica
Umidade e pressão
Velocidade do vento
Condição climática
Latitude e longitude
Timestamp da coleta

A tabela preserva o histórico das execuções, permitindo análises ao longo do tempo.

📈 Possíveis Evoluções
Automatização do pipeline com agendador
Criação de dashboards no Looker Studio ou Power BI
Inclusão de validações de qualidade de dados
Ampliação para dados históricos ou novas cidades
Monitoramento e logging do pipeline

👤 Autor
Rafael Cunha Lima
GitHub: https://github.com/RafaelCL94

LinkedIn: https://www.linkedin.com/in/rafael-lima94

📄 Observações
Este projeto foi desenvolvido com foco em aprendizado prático e construção de portfólio em Engenharia de Dados, simulando cenários comuns encontrados em pipelines reais de ingestão e processamento de dados.
