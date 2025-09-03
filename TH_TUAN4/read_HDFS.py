from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder \
    .appName("Read Parquet from HDFS") \
    .getOrCreate()

# Read Parquet files from HDFS
df = spark.read \
    .format("parquet") \
    .load("hdfs://hadoop-master:9000/test1/")

# Show the data
df.show()
print(df.count())

# Print schema
df.printSchema()