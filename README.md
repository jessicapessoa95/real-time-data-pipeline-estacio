# Big Data Pipeline Project

Este projeto implementa um pipeline básico de ingestão e processamento de dados em tempo real utilizando Apache Kafka e Apache Spark, além de um exemplo simples de um modelo preditivo com Scikit-learn. O objetivo do projeto é criar uma solução prática de análise de dados em tempo real e previsão de movimentações, aplicável no contexto da gestão de colaboradores em uma empresa de outsourcing, como a Datum.

## Estrutura do projeto

O projeto é composto pelos seguintes arquivos:

- kafka_producer.py: Script responsável por produzir dados de exemplo e enviá-los ao Apache Kafka.
- spark_processing.py: Script que realiza o processamento dos dados em tempo real recebidos pelo Kafka, utilizando Apache Spark.
- predictive_model.py: Script que implementa um modelo preditivo básico, usando Scikit-learn, para prever movimentações de colaboradores.
- requirements.txt: Arquivo contendo as dependências do projeto, que devem ser instaladas para executar os scripts.

## Como executar o projeto

1. Iniciar o Kafka: Certifique-se de que o Apache Kafka está instalado e em execução. Inicie o servidor do Kafka localmente ou em um ambiente de teste.

2. Produzir dados com Kafka: Após o Kafka estar em execução, o próximo passo é rodar o script `kafka_producer.py`. Esse script será responsável por gerar e enviar dados simulados para o tópico configurado no Kafka.

3. Processar dados com Spark: Depois de o Kafka começar a enviar dados, execute o script `spark_processing.py`. Esse script processará os dados em tempo real utilizando Apache Spark, permitindo o monitoramento contínuo e a análise dos dados recebidos.

4. Executar o modelo preditivo (opcional): Após o processamento dos dados com Spark, você pode rodar o script `predictive_model.py`. Esse script aplica um modelo preditivo simples, com base nos dados processados, para fazer previsões de movimentações de colaboradores.

## Requisitos do projeto

Para garantir que o projeto funcione corretamente, é necessário instalar as dependências especificadas no arquivo `requirements.txt`. Isso inclui bibliotecas como kafka-python, pyspark, scikit-learn, pandas, entre outras.

As instruções de instalação das dependências podem ser seguidas utilizando o gerenciador de pacotes `pip`.
