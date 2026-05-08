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
