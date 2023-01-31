import pymongo
import pandas as pd
import json
from dataclasses import dataclass
import os


@dataclass
class EnvironmentVariable:
    mongo_db_url:str = os.getenv("MONGO_DB_URL")

env_var = EnvironmentVariable()
mongo_client = pymongo.MongoClient(env_var.mongo_db_url)
print(mongo_client)
# mongo_client = pymongo.MongoClient("mongodb+srv://mervebdurna:4161MsM14@mycluster.yrgvltw.mongodb.net/?retryWrites=true&w=majority")
# TARGET_COLUMN = "class"