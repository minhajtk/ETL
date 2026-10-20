from hdfs import InsecureClient
import pandas as pd

client = InsecureClient('http://127.0.0.1:50070', user='maria_dev')

filepath = '/user/maria_dev/Iqbal/titanic.csv'

with client.read(filepath) as reader:
    df = pd.read_csv(reader)

print(df.head())
