from unittest.mock import patch, MagicMock
from utils.load import load_to_csv, load_to_postgres, load_to_sheets
import pandas as pd

@patch("utils.load.pd.DataFrame.to_csv")
def test_load_to_csv(mock_to_csv):
    df = pd.DataFrame({'Title': ['A'], 'Price': [1000]})
    load_to_csv(df, "test.csv")
    mock_to_csv.assert_called_once_with("test.csv", index=False)

@patch("utils.load.create_engine")
@patch("utils.load.pd.DataFrame.to_sql")
def test_load_to_postgres(mock_to_sql, mock_create_engine):
    df = pd.DataFrame({'Title': ['A'], 'Price': [1000]})
    load_to_postgres(df, "dummy_url")
    mock_to_sql.assert_called_once()

@patch("utils.load.build")
@patch("utils.load.service_account.Credentials.from_service_account_file")
def test_load_to_sheets(mock_creds, mock_build):
    df = pd.DataFrame({'Title': ['A'], 'Price': [1000]})
    mock_service = MagicMock()
    mock_build.return_value = mock_service
    load_to_sheets(df, "dummy_id", "Sheet1!A1", "dummy.json")
    mock_build.assert_called_once()
    mock_service.spreadsheets().values().update.assert_called_once()
