# Big Data Pipeline Project

Este projeto implementa um pipeline básico de ingestão e processamento de dados em tempo real utilizando Apache Kafka e Apache Spark, além de um exemplo simples de um modelo preditivo com Scikit-learn.

## Estrutura do projeto

- `kafka_producer.py`: Produz dados de exemplo para o Kafka.
- `spark_processing.py`: Processa os dados em tempo real usando Spark.
- `predictive_model.py`: Implementa um modelo preditivo básico com Scikit-learn.
- `requirements.txt`: Dependências do projeto.

## Como executar

### 1. Iniciar o Kafka
Certifique-se de que o Kafka está instalado e em execução.

```bash
bin/kafka-server-start.sh config/server.properties
