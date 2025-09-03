from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StructField, StringType, DoubleType, IntegerType

# Initialize Spark session
spark = SparkSession.builder \
    .appName("Kafka to Console Test") \
    .getOrCreate()

# Define schema for the incoming Kafka data
schema = StructType([
    StructField("event_id", IntegerType()),
    StructField("timestamp", StringType()),
    StructField("value", StringType())
])

# Read from Kafka
df = spark \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "real-time-data") \
    .load()

# Parse the Kafka value field (assuming JSON data)
parsed_df = df.select(
    col("key").cast("string"),
    from_json(col("value").cast("string"), schema).alias("data")
).select("key", "data.*")

parsed_df.printSchema()


query = parsed_df.writeStream \
    .format("parquet")  \
    .option("path", "hdfs://hadoop-master:9000/test1/")  \
    .option("checkpointLocation", "hdfs://hadoop-master:9000/checkpoint/")  \
    .outputMode("append")  \
    .start()

# Wait for the streaming query to terminate
query.awaitTermination()