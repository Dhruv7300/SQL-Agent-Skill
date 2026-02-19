from src.config.db_config import db

def run_sql_query(query):

    try:
        result = db.run_no_throw(query, include_columns=True)
    except Exception as e:
        result = str(e)

    return result