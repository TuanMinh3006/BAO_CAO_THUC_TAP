from pyspark.sql import SparkSession
import time

spark = SparkSession.builder\
        .appName("QueryORC_and_Parquet")\
        .getOrCreate()
hdfs_path="hdfs://hadoop-master:9000/test/"
orc_path=hdfs_path + "vnm_children_under_five_2020.orc"
parquet_path=hdfs_path + "vnm_children_under_five_2020.parquet"

start_time_orc_read=time.time()
df_orc=spark.read.orc(orc_path)
end_time_orc_read=time.time()

start_time_parquet_read=time.time()
df_parquet=spark.read.parquet(parquet_path)
end_time_parquet_read=time.time()

start_time_orc_query=time.time()
df_orc_sum=df_orc.count()
end_time_orc_query=time.time()
print(df_orc.printSchema())
print(df_orc.head(20))
start_time_parquet_query=time.time()
df_parquet_sum=df_parquet.count()
end_time_parquet_query=time.time()

print("ORC File Read Time: ", end_time_orc_read - start_time_orc_read)
print("Parquet File Read Time: ", end_time_parquet_read - start_time_parquet_read)

print("ORC File Query Time: ", end_time_orc_query - start_time_orc_query)
print("Parquet File Query Time: ", end_time_parquet_query - start_time_parquet_query)
