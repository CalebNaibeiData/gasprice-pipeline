import http.client
from sqlalchemy import create_engine , text
import pandas as pd
import json
import psycopg2
from dotenv import load_dotenv
import os


load_dotenv()

def extract_data():
    conn = os.getenv("url")

    headers = os.getenv("api_key")

    conn.request("GET", "/gasPrice/stateUsaPrice?state=WA", headers=headers)

    res = conn.getresponse()
    data = res.read()
    gasprices_data = json.loads(data.decode("utf-8"))  # FIXED

    return gasprices_data

#gasprices_df


def transform_data(raw_data):
    df = pd.json_normalize(raw_data['result']['cities'])

    # standardize columns
    df.columns = df.columns.str.lower()

    # select + rename + clean
    df = df.rename(columns={"name": "cities"})

    df = df[[
        "cities",
        "currency",
        "gasoline",
        "midgrade",
        "premium",
        "diesel"
    ]]

    return df

def load_data(df):
   DB_host = os.getenv('DB_HOST')
   DB_database = os.getenv('DB_NAME')
   DB_user = os.getenv('DB_USER')
   DB_password = os.getenv('DB_PASSWORD')
   DB_port = os.getenv('DB_PORT')


   engine = create_engine(
            f'postgresql+psycopg2://{DB_user}:{DB_password}@{DB_host}:{DB_port}/{DB_database}'
            )
   df.to_sql(
        "final_cities",
        engine,
        if_exists="replace",
        index=False
    )


def main():
    raw = extract_data()
    transformed = transform_data(raw)
    load_data(transformed)

    print("ETL pipeline completed successfully.")

if __name__ == "__main__":
    main()