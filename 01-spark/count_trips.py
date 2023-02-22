# 패키지를 가져오고
from pyspark import SparkConf, SparkContext
import pyarrow.parquet as parquet
import pandas as pd

# Spark 설정
conf = SparkConf().setMaster("local[*]").setAppName("uber-date-trips")
sc = SparkContext(conf=conf)

# 우리가 가져올 데이터가 있는 파일
directory = "C:\projects\DataEngineering\data-engineering\01-spark\data"
filename = "fhvhv_tripdata_2020-03.parquet"

# 데이터 파싱
lines = sc.textFile(f"file:///{directory}/{filename}")
header = lines.first() 
filtered_lines = lines.filter(lambda row:row != header) 

# 필요한 부분만 골라내서 세는 부분
# countByValue로 같은 날짜등장하는 부분을 센다
dates = filtered_lines.map(lambda x: x.split(",")[2].split(" ")[0])
result = dates.countByValue()

# 아래는 Spark코드가 아닌 일반적인 파이썬 코드
# CSV로 결과값 저장 
pd.Series(result, name="trips").to_csv("trips_date1.csv")