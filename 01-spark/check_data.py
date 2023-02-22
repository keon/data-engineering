import pandas as pd
import pyarrow.parquet as parquet

df=pd.read_parquet('./data/fhvhv_tripdata_2020-03.parquet')
print(df.head(5))