import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)

def transform_data(df):
    try:
        if df.empty:
            return df

        # Hapus invalid title
        df = df[df['Title'] != 'Unknown Product']

        # Hapus invalid rating
        df = df[
            (df['Rating'] != 'Invalid Rating / 5') &
            (df['Rating'] != 'Not Rated')
        ]

        # Hapus invalid price
        df = df[
            (df['Price'] != 'Price Unavailable') &
            (df['Price'].notnull())
        ]

        # Bersihkan Rating
        df['Rating'] = df['Rating'].str.extract(r'(\d+\.\d+)')
        df['Rating'] = df['Rating'].astype(float)

        # Bersihkan Price
        df['Price'] = (
            df['Price']
            .replace(r'[\$,]', '', regex=True)
            .astype(float)
        )

        # USD → IDR
        df['Price'] = df['Price'] * 16000

        # Bersihkan Colors
        df['Colors'] = (
            df['Colors']
            .str.extract(r'(\d+)')
            .astype(int)
        )

        # Pastikan string
        df['Size'] = df['Size'].astype(str)
        df['Gender'] = df['Gender'].astype(str)

        # Timestamp
        df['Timestamp'] = pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')

        # Hapus duplicate
        df = df.drop_duplicates()

        logging.info("Transformasi berhasil diselesaikan.")

        return df

    except Exception as e:
        logging.error(f"Error pada tahap Transform: {e}")
        return pd.DataFrame()