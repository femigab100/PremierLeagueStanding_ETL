from extract import extract_data
from transform import transform_data
from load import load_to_csv

def run_pipeline():
    print("Starting ETL Pipeline...")

    # Extract
    print("Extracting data...")
    raw_json = extract_data()

    # Transform
    print("Transforming data...")
    df = transform_data(raw_json)
    print(df.head())

    # Load
    print("Loading data into CSV...")
    load_to_csv(df)

    print("ETL Pipeline completed successfully!")

    run_pipeline()
