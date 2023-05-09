import pandas as pd
import pyarrow.parquet as parquet

#df=pd.read_parquet('./data/fhvhv_tripdata_2020-03.parquet')
#df.to_csv('fhvhv_tripdata_2020-03.csv')
df=pd.read_csv('./data/fhvhv_tripdata_2020-03.csv')
print(df.head(5))