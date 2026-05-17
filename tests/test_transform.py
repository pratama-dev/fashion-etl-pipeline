import pytest
import pandas as pd
from utils.transform import transform_data

def test_transform_empty_dataframe():
    empty_df = pd.DataFrame()
    result = transform_data(empty_df)
    assert result.empty

def test_transform_invalid_input():
    with pytest.raises(AttributeError):
        transform_data(None)
    
def test_transform_logic():
    data = {
        'Title': ['Kemeja', 'Unknown Product'],
        'Price': ['$10', '$100'],
        'Rating': ['4.5 / 5', 'Invalid Rating'],
        'Colors': ['3 Colors', '1 Color'],
        'Size': ['Size: L', 'Size: M'],
        'Gender': ['Gender: Men', 'Gender: Men']
    }
    df = pd.DataFrame(data)
    result = transform_data(df)
    
    # Cek penghapusan Unknown Product
    assert len(result) == 1
    # Cek konversi harga (10 * 16000)
    assert result.iloc[0]['Price'] == 160000
    # Cek pembersihan Size
    assert result.iloc[0]['Size'] == 'L'
    # Cek keberadaan timestamp
    assert 'timestamp' in result.columns