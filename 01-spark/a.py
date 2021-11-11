x = sc.parallelize([
    ("MATH", 7), ("MATH", 2), ("ENGLISH", 7),
    ("SCIENCE", 7), ("ENGLISH", 4), ("ENGLISH", 9),
    ("MATH", 8), ("MATH", 3), ("ENGLISH", 4),
    ("SCIENCE", 6), ("SCIENCE", 9), ("SCIENCE", 5)], 3)
 
y = x.groupByKey()
 
print(y.getNumPartitions()) 
# 3
 
y = x.groupByKey(2)
print(y.getNumPartitions())
# 2
 
for t in y.collect():
    print(t[0], list(t[1]))
    
# MATH [7, 2, 8, 3]
# ENGLISH [7, 4, 9, 4]
# SCIENCE [7, 6, 9, 5]

grouped = sc.parallelize([
  "C", "C++", "Python", "Java", "C#"
]).groupBy(lambda x: x[0]).collect()

for k, v in grouped:
  print(k, list(v))

sc.parallelize([
  "C", "C++", "Python", "Java", "C#"
]).groupByKey()


x = sc.parallelize([
    ("MATH", 7), ("MATH", 2), ("ENGLISH", 7),
    ("SCIENCE", 7), ("ENGLISH", 4), ("ENGLISH", 9),
    ("MATH", 8), ("MATH", 3), ("ENGLISH", 4),
    ("SCIENCE", 6), ("SCIENCE", 9), ("SCIENCE", 5)], 3)

tickers = sc.parallelize([
  (1, ("Google", "GOOGL", "USA")),
  (2, ("Netflix", "NFLX", "USA")),
  (3, ("Amazon", "AMZN", "USA")),
  (4, ("Tesla", "TSLA", "USA")),
  (5, ("Samsung", "005930", "Korea")),
  (6, ("Kakao", "035720", "Korea"))
])

prices = sc.parallelize([
  (1, (2984, "USD")), (2, (645, "USD")),
  (3, (3518, "USD")), (4, (1222, "USD")),
  (5, (70600, "KRW")), (6, (125000, "KRW"))
])

tickerPrice = tickers.join(prices)
tickerPrice.collect() 
# [(1, (('Google', 'GOOGL', 'USA'), (2984, 'USD'))), 
#  (2, (('Netflix', 'NFLX', 'USA'), (645, 'USD'))),
#  (3, (('Amazon', 'AMZN', 'USA'), (3518, 'USD'))),
#  (4, (('Tesla', 'TSLA', 'USA'), (1222, 'USD'))),
#  (5, (('Samsung', '005930', 'Korea'), (70600, 'KRW'))),
#  (6, (('Kakao', '035720', 'Korea'), (125000, 'KRW')))]


tickerPrice.filter(lambda x: x[1][0][2] == "USA").collect()
# [(1, (('Google', 'GOOGL', 'USA'), (2984, 'USD'))), 
#  (2, (('Netflix', 'NFLX', 'USA'), (645, 'USD'))),
#  (3, (('Amazon', 'AMZN', 'USA'), (3518, 'USD'))),
#  (4, (('Tesla', 'TSLA', 'USA'), (1222, 'USD')))]

tickerPrice.filter(lambda x: x[1][1][1] == "KRW").collect()
# [(5, (('Samsung', '005930', 'Korea'), (70600, 'KRW'))),
#  (6, (('Kakao', '035720', 'Korea'), (125000, 'KRW')))]


# CASE 1: join 먼저, filter 나중에
tickerPrice = tickers.join(prices)
tickerPrice.filter(lambda x: x[1][0][2] == "USA" and x[1][1][0] > 2000).collect()
# [(1, (('Google', 'GOOGL', 'USA'), (2984, 'USD'))), (3, (('Amazon', 'AMZN', 'USA'), (3518, 'USD')))]

# CASE 2: filter 먼저, join 나중에
filteredTicker = tickers.filter(lambda x: x[1][2] == "USA")
filteredPrice = prices.filter(lambda x: x[1][0] > 2000)
filteredTicker.join(filteredPrice).collect()
# [(1, (('Google', 'GOOGL', 'USA'), (2984, 'USD'))), (3, (('Amazon', 'AMZN', 'USA'), (3518, 'USD')))]

for t in x.groupByKey().collect():
    print(t[0], list(t[1]))

x.keys().distinct().count()
# 3


rdd1 =  sc.parallelize([("foo", 1), ("bar", 2), ("baz", 3)])
rdd2 =  sc.parallelize([("foo", 4), ("bar", 5), ("bar", 6),("zoo", 1)])

rdd1.join(rdd2).collect()
# [('bar', (2, 5)), ('bar', (2, 6)), ('foo', (1, 4))]

rdd1.leftOuterJoin(rdd2).collect()
# [('baz', (3, None)), ('bar', (2, 5)), ('bar', (2, 6)), ('foo', (1, 4))]

rdd1.rightOuterJoin(rdd2).collect()
# [('bar', (2, 5)), ('bar', (2, 6)), ('zoo', (None, 1)), ('foo', (1, 4))]


# reduceByKey
# (textRDD
#  .flatMap(lambda line: line.split())
#  .map(lambda word: (word, 1))
#  .reduceByKey(lambda a, b: a + b))

# # groupByKey
# (textRDD
#  .flatMap(lambda line: line.split())
#  .map(lambda word: (word, 1))
#  .groupByKey()
#  .map(lambda (w, counts): (w, sum(counts))))


from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("test-app").getOrCreate()

#JSON
dataframe = spark.read.json('dataset/nyt2.json')
#TXT FILES# 
dataframe_txt = spark.read.text('text_data.txt')
#CSV FILES# 
dataframe_csv = spark.read.csv('csv_data.csv')
#PARQUET FILES# 
dataframe_parquet = spark.read.load('parquet_data.parquet')


# RDD
lines = sc.textFile("example.csv")
data = lines.map(lambda x: x.split(","))
preprocessed = data.map(lambda x: Row(name=x[0], price=int(x[1])))

# Infer
df = spark.createDataFrame(preprocessed)


# Specify
schema = StructType(
  StructField("name", StringType(), True),
  StructField("price", StringType(), True) 
)
spark.createDataFrame(preprocessed, schema).show()