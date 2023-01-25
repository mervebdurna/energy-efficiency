import pymongo
import pandas as pd
import json
from dotenv import load_dotenv
from energy_efficiency.logger import logging
from energy_efficiency.config import mongo_client

logging.info(f"Loading enviroment variable from .env file.")
load_dotenv()

# Provide the mongodb localhost url to connect python to mongodb from config.
client = mongo_client

DATA_FILE_PATH= "/config/workspace/data/energy_efficiency.csv"
DATABASE_NAME="mydatabase"
COLLECTION_NAME="energy_efficiency"


if __name__=="__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    print(f"Rows and columns: {df.shape}")

    #Convert dataframe to json so that we can dump these record in mongo db
    df.reset_index(drop=True,inplace=True)

    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0:2])

    #insert converted json record to mongo db
    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)
    