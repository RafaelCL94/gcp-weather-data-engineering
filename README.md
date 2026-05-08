# GCP Weather Data Engineering Pipeline

Projeto de Engenharia de Dados desenvolvido para simular um pipeline real de ingestão contínua de dados climáticos utilizando Python e Google Cloud Platform (GCP).

O foco do projeto é demonstrar, de forma clara e objetiva, como dados externos podem ser coletados, tratados e armazenados em um data warehouse na nuvem, seguindo boas práticas de organização, versionamento e reprodutibilidade.

---

## Objetivo do Projeto

* Consumir dados climáticos de uma API pública
* Padronizar e estruturar os dados coletados
* Manter histórico incremental de medições
* Armazenar os dados em um data warehouse (BigQuery)
* Disponibilizar uma base pronta para análises e dashboards

---

## Tecnologias Utilizadas

* Python 3
* OpenWeather API
* Google Cloud Platform (GCP)
* BigQuery
* Google Cloud SDK
* Git e GitHub

### Bibliotecas Python

* requests
* pandas
* python-dotenv
* google-cloud-bigquery

---

## Arquitetura do Pipeline

1. Ingestão de dados meteorológicos via API
2. Tratamento e padronização dos dados
3. Enriquecimento com metadados (localização e timestamp)
4. Carga incremental no BigQuery
5. Persistência do histórico para análises futuras

O pipeline foi estruturado de forma modular, facilitando manutenção, automação e futuras expansões.

---

## Estrutura do Projeto

```
gcp-weather-data-engineering/
│
├── ingestion/          # Coleta de dados da API
├── load/               # Carga de dados no BigQuery
├── sql/                # Scripts SQL auxiliares
├── run_pipeline.py     # Orquestra a execução do pipeline
├── requirements.txt    # Dependências do projeto
├── .env.example        # Exemplo de variáveis de ambiente
└── README.md
```

---

## Como Executar o Projeto

### 1. Clonar o repositório

```
git clone https://github.com/RafaelCL94/gcp-weather-data-engineering.git
cd gcp-weather-data-engineering
```

### 2. Criar e ativar ambiente virtual (opcional)

```
python -m venv venv
```

Windows:

```
venv\Scripts\activate
```

### 3. Instalar dependências

```
pip install -r requirements.txt
```

### 4. Configurar variáveis de ambiente

Crie um arquivo `.env` com base no `.env.example` e informe sua chave da API e configurações do projeto.

### 5. Autenticar no Google Cloud

```
gcloud auth login
gcloud auth application-default login
gcloud config set project SEU_PROJECT_ID
```

### 6. Executar o pipeline

```
python run_pipeline.py
```

---

## Dados no BigQuery

Os dados são carregados de forma incremental na tabela:

```
weather.weather_history
```

Cada execução adiciona novos registros, preservando o histórico completo das medições climáticas.

Campos principais:

* Cidade e país
* Temperatura atual, mínima e máxima
* Sensação térmica
* Umidade e pressão
* Velocidade do vento
* Condição climática
* Latitude e longitude
* Timestamp da coleta

---

## Possíveis Evoluções

* Automatização do pipeline (scheduler)
* Criação de dashboards analíticos
* Validação e monitoramento da qualidade dos dados
* Expansão para múltiplas cidades ou dados históricos

---

## Autor

Rafael Cunha Lima
Engenharia de Dados | Python | GCP | BigQuery

GitHub: [https://github.com/RafaelCL94](https://github.com/RafaelCL94)
LinkedIn: [https://www.linkedin.com/in/rafael-lima94](https://www.linkedin.com/in/rafael-lima94)

---

Este projeto foi desenvolvido com foco em aprendizado prático e construção de portfólio profissional, simulando desafios comuns encontrados em pipelines reais de dados.
