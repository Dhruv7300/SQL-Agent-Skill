import pandas as pd
from sqlalchemy import create_engine
from langchain_community.utilities import SQLDatabase
import os
from dotenv import load_dotenv

load_dotenv()
db_uri = os.getenv("DB_URI")

engine = create_engine(db_uri, pool_pre_ping=True, pool_recycle=60)

db = SQLDatabase(engine, sample_rows_in_table_info=5)

with engine.connect() as conn:
    print(f"Successfully Connected to DB")