import pandas as pd
from sqlalchemy import create_engine
from google.oauth2 import service_account
from googleapiclient.discovery import build

def load_to_csv(df, filename="products.csv"):
    try:
        df.to_csv(filename, index=False)
    except Exception as e:
        print(e)

def load_to_postgres(df, db_url):
    try:
        engine = create_engine(db_url)
        df.to_sql('products', engine, if_exists='replace', index=False)
    except Exception as e:
        print(e)

def load_to_sheets(df, spreadsheet_id, range_name="Sheet1!A1", credentials_file="google-sheets-api.json"):
    try:
        creds = service_account.Credentials.from_service_account_file(
            credentials_file, scopes=['https://www.googleapis.com/auth/spreadsheets']
        )
        service = build('sheets', 'v4', credentials=creds)
        values = [df.columns.values.tolist()] + df.values.tolist()
        body = {'values': values}
        service.spreadsheets().values().update(
            spreadsheetId=spreadsheet_id, range=range_name,
            valueInputOption="RAW", body=body
        ).execute()
    except Exception as e:
        print(e)
