import pandas as pd
import os

def clean_brent_data(input_path, output_path):
    # Load raw data
    df = pd.read_csv(input_path)

    # Rename columns for consistency
    df.columns = df.columns.str.strip().str.lower()
    df.rename(columns={'date': 'Date', 'price': 'Price'}, inplace=True)

    # Convert date column to datetime format
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

    # Drop rows with missing dates or prices
    df.dropna(subset=['Date', 'Price'], inplace=True)

    # Sort by date
    df.sort_values(by='Date', inplace=True)

    # Reset index
    df.reset_index(drop=True, inplace=True)

    # Export cleaned data
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"Cleaned data saved to: {output_path}")