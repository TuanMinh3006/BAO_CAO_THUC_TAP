from pyspark.sql import SparkSession
from pyspark import SparkFiles,SparkContext
import time

spark=SparkSession.builder \
    .appName("SaveToHDFS")\
    .getOrCreate()

    #.config("spark.hadoop.fs.defaultFS", "hdfs://localhost:9870")\

url="/home/hadoopuser/vnm_children_under_five_2020.csv"
df=spark.read.csv(url, header=True, inferSchema=True)
df.show()
orc_path = "hdfs://hadoop-master:9000/test/vnm_children_under_five_2020.orc"
parquet_path = "hdfs://hadoop-master:9000/test/vnm_children_under_five_2020.parquet"

print(df.rdd.getNumPartitions())

start_time_orc = time.time()
df.write.mode("overwrite").orc(orc_path)
end_time_orc = time.time()
start_time_parquet = time.time()
df.write.mode("overwrite").parquet(parquet_path)
end_time_parquet = time.time()

print("Time taken to save ORC file: ", end_time_orc - start_time_orc)
print("Time taken to save Parquet file: ", end_time_parquet - start_time_parquet)

spark.stop()