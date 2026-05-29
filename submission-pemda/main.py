from utils.extract import extract_data
from utils.transform import transform_data
from utils.load import load_to_csv

def run_pipeline():
    raw_data = extract_data()
    if raw_data:
        clean_data = transform_data(raw_data)
        if clean_data is not None and not clean_data.empty:
            load_to_csv(clean_data)

if __name__ == "__main__":
    run_pipeline()
