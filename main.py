from sqlalchemy import create_engine
from extract import extract_data
from transform import transform_data
from load import load_data

def main():
    raw = extract_data()
    transformed = transform_data(raw)
    load_data(transformed)

    print("ETL pipeline completed successfully.")

if __name__ == "__main__":
    main()