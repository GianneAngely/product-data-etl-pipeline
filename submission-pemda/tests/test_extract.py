from unittest.mock import patch, Mock
from utils.extract import extract_data

@patch("utils.extract.requests.get")
def test_extract_data_success(mock_get):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.content = b'''
        <div class="collection-card">
            <h3 class="product-title">Jacket 1</h3>
            <span class="price">$10.00</span>
            <p>Rating: 4.5 / 5</p>
            <p>3 Colors</p>
            <p>Size: M</p>
            <p>Gender: Unisex</p>
        </div>
    '''
    mock_get.return_value = mock_response
    with patch('builtins.range', return_value=[1]):
        result = extract_data()
    assert result is not None
    assert len(result) == 1

@patch("utils.extract.requests.get")
def test_extract_data_error(mock_get):
    mock_get.side_effect = Exception("Error")
    result = extract_data()
    assert result is None
