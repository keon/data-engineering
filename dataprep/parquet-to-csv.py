import pandas as pd
df = pd.read_parquet('fhvhv_tripdata_2020-03.parquet')
df.to_csv('fhvhv_tripdata_2020-03.csv')