import pytest
import requests
import pandas as pd
from unittest.mock import MagicMock
from utils.extract import scrape_page
from unittest.mock import patch
from utils.extract import scrape_page
from utils.extract import extract_all

@patch('utils.extract.scrape_page')
def test_extract_all(mock_scrape):
    mock_scrape.return_value = [
        {
            'Title': 'Jacket',
            'Price': '$100'
        }
    ]

    result = extract_all(total_pages=2)
    assert isinstance(result, pd.DataFrame)
    assert len(result) == 2
    
@patch('requests.Session.get')
def test_scrape_page_request_exception(mock_get):
    mock_get.side_effect = requests.exceptions.RequestException(
        "Connection Error"
    )
    session = requests.Session()
    result = scrape_page(1, session)
    assert result == []
     
@patch('requests.Session.get')
def test_scrape_page_empty(mock_get):
    mock_response = mock_get.return_value
    mock_response.status_code = 200
    mock_response.content = b"<html></html>"

    session = requests.Session()
    result = scrape_page(1, session)
    assert result == []

def test_scrape_page_success():
    # Setup mock session
    mock_session = MagicMock()
    mock_response = MagicMock()
    
    # Mocking HTML Response sesuai dengan HTML fashion-studio
    html_content = """
    <div class="collection-card">
        <h3 class="product-title">T-shirt 2</h3>
        <span class="price">$100.00</span>
        <p>Rating: ⭐ 3.9 / 5</p>
        <p>3 Colors</p>
        <p>Size: M</p>
        <p>Gender: Women</p>
    </div>
    """
    mock_response.content = html_content.encode('utf-8')
    mock_response.raise_for_status.return_value = None
    mock_session.get.return_value = mock_response
    
    # Execute
    result = scrape_page(1, mock_session)
    
    # Assertions
    assert len(result) == 1
    assert result[0]['Title'] == 'T-shirt 2'
    assert result[0]['Price'] == '$100.00'
    assert result[0]['Size'] == 'Size: M'