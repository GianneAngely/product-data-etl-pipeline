import pandas as pd
from datetime import datetime

def transform_data(raw_data):
    try:
        df = pd.DataFrame(raw_data)
        df = df.dropna()
        df = df.drop_duplicates()
        df = df[df['Title'] != 'Unknown Product']
        df = df[~df['Rating'].isin(['Invalid Rating / 5', 'Not Rated'])]
        df = df[df['Price'] != 'Price Unavailable']
        
        df['Price'] = df['Price'].str.replace('$', '', regex=False).str.replace(',', '', regex=False).astype('float64') * 16000
        df['Rating'] = df['Rating'].str.extract(r'(\d+\.\d+)')[0].astype('float64')
        df['Colors'] = df['Colors'].str.extract(r'(\d+)')[0].astype('int64')
        df['Size'] = df['Size'].str.replace('Size: ', '', regex=False).str.strip()
        df['Gender'] = df['Gender'].str.replace('Gender: ', '', regex=False).str.strip()
        df['Timestamp'] = datetime.now().isoformat()
        
        df = df.reset_index(drop=True)
        return df
    except Exception as e:
        print(e)
        return None
