# fetch_data.py

import yfinance as yf
import pandas as pd
import os


def fetch_iv_data(ticker_symbol, save_path, num_expirations=6):
    """
    Fetch options data for multiple expiration dates and save as CSV.

    Parameters:
    ticker_symbol : str - The underlying ticker (e.g., 'USO')
    save_path     : str - File path to save the combined CSV
    num_expirations : int - Number of expiries to include
    """
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    ticker = yf.Ticker(ticker_symbol)
    expirations = ticker.options[:num_expirations]
    all_data = []

    for expiry in expirations:
        try:
            chain = ticker.option_chain(expiry)
            calls = chain.calls.copy()
            calls['expirationDate'] = expiry
            all_data.append(calls)
        except Exception as e:
            print(f"Failed to fetch data for {expiry}: {e}")

    if all_data:
        df = pd.concat(all_data, ignore_index=True)
        df.to_csv(save_path, index=False)
        print(f"Options data saved to {save_path}")
    else:
        print("No options data fetched.")


if __name__ == "__main__":
    fetch_iv_data("BTC", r"C:\Users\adity\OneDrive\Documents\GitHub\Implied-Volatility-Surface-Visualization\data\uso_options_data.csv", num_expirations=6)
