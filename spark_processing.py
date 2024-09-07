from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StructField, StringType, FloatType

# Criando a sessão Spark
spark = SparkSession.builder \
    .appName("Kafka Spark Streaming") \
    .getOrCreate()

# Definir esquema de dados
schema = StructType([
    StructField("id", StringType(), True),
    StructField("value", FloatType(), True),
    StructField("timestamp", FloatType(), True)
])

# Conectando ao Kafka
df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "datum_topic") \
    .load()

# Processar os dados
df = df.selectExpr("CAST(value AS STRING)") \
       .select(from_json(col("value"), schema).alias("data")) \
       .select("data.*")

# Exibir os dados processados em tempo real
query = df.writeStream \
    .outputMode("append") \
    .format("console") \
    .start()

query.awaitTermination()
