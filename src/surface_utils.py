# surface_utils.py

import pandas as pd
import numpy as np
from scipy.interpolate import griddata


def prepare_surface_data(csv_path):
    """
    Load and clean options data to extract strikes, days to expiry, and implied volatility.

    Returns a cleaned DataFrame with necessary columns for surface construction.
    """
    df = pd.read_csv(csv_path)
    df = df[df['impliedVolatility'] > 0]
    df['expirationDate'] = pd.to_datetime(df['expirationDate'])
    df['daysToExpiry'] = (df['expirationDate'] - pd.Timestamp.today()).dt.days
    df = df[['strike', 'daysToExpiry', 'impliedVolatility']]
    return df.dropna()


def interpolate_iv_surface(df, grid_size=50):
    """
    Interpolate IV surface over a strike-expiry grid using SciPy's griddata.

    Returns:
        X, Y: grid coordinates
        Z: interpolated volatility values
    """
    strikes = df['strike'].values
    expiries = df['daysToExpiry'].values
    ivs = df['impliedVolatility'].values

    strike_lin = np.linspace(min(strikes), max(strikes), grid_size)
    expiry_lin = np.linspace(min(expiries), max(expiries), grid_size)
    X, Y = np.meshgrid(strike_lin, expiry_lin)
    Z = griddata((strikes, expiries), ivs, (X, Y), method='cubic')

    return X, Y, Z
