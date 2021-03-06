import os
from pyspark.sql import SparkSession

if __name__ == '__main__':
    if os.name == 'nt':
        print('detected windows, setting HADOOP_HOME')
        os.environ['HADOOP_HOME'] = 'C:/hadoop/hadoop-2.7.1'

    spark = SparkSession.builder \
        .master("local") \
        .appName("Word Count") \
        .getOrCreate()
    sc = spark.sparkContext

