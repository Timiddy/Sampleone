import awswrangler as wr
import pandas as pd
from datetime import datetime
import pytz
import boto3


s3_uri="s3://timmu-athena-sql/results/data/orders/"
df=wr.s3.read_csv(s3_uri)
print(df)