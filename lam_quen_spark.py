from pyspark.sql import SQLContext
url="/home/hadoopuser/vnm_children_under_five_2020.csv"
from pyspark import SparkFiles,SparkContext
sc=SparkContext()
sc.addFile(url)
sqlContext=SQLContext(sc)
df=sqlContext.read.csv(SparkFiles.get("vnm_children_under_five_2020.csv"),header=True,inferSchema=True)
df.printSchema()
print("Total number of records: ", df.count())