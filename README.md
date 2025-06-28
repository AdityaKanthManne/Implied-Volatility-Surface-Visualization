# Implied Volatility Surface Visualization

This project constructs and visualizes a 3D implied volatility (IV) surface from real-world options data using Python. It maps implied volatility across strike prices and expiration dates to help uncover volatility skew and term structure—two key components in option pricing and risk management.

## Objective

- Extract options chain data for a liquid underlying (e.g., USO or SPY)
- Parse and clean the data to compute implied volatilities
- Construct a 3D surface plot of strike, expiry, and IV
- Analyze skew (strike-based IV changes) and term structure (expiry-based IV changes)

## Why This Matters

Implied volatility surfaces reflect the market's expectations for future volatility and risk. Traders, quants, and risk managers use IV surfaces to:
- Calibrate advanced pricing models (e.g., Heston, SABR)
- Price exotic or path-dependent options
- Identify arbitrage opportunities
- Construct hedging strategies

## Tools Used

- Python 3
- yFinance (data)
- NumPy, Pandas (data manipulation)
- SciPy (interpolation)
- Matplotlib, Plotly (3D visualization)

## Project Structure

```
volatility-surface-visualization/
├── data/
│   └── uso_options_data.csv
├── notebooks/
│   └── volatility_surface_analysis.ipynb
├── scripts/
│   └── fetch_data.py
├── src/
│   └── surface_utils.py
├── plots/
│   └── surface_plot.png
├── requirements.txt
└── README.md
```

## Output

- A 3D surface showing implied volatility against strike and expiry
- Visualizations of skew and term structure
- Exported images for reports or presentations

## Future Enhancements

- Fit parametric surfaces to implied vol data
- Extend to local volatility or stochastic volatility surfaces
- Compare across different asset classes (equities, oil, FX)

## Author

Aditya Kanth Manne  
