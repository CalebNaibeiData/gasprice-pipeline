from sqlalchemy import create_engine
from dotenv import load_dotenv
import os


load_dotenv()




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