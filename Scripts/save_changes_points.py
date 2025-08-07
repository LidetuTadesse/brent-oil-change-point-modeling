import pandas as pd
import numpy as np

from pathlib import Path

base_dir = Path(__file__).resolve().parent.parent  # two levels up from script
data_path = base_dir / "data" / "processed" / "brent_log_features.csv"
output_path = base_dir / "backend" / "models" / "change_points.csv"

print("Reading CSV from:", data_path)
df = pd.read_csv(data_path)
print(df.head(300))


# Drop NaNs from Log_Return column
df = df.dropna(subset=['Log_Return'])

# Use the 'Log_Return' or another relevant column
signal = df['Log_Return'].values

# Compute rolling mean and std
window = 10
rolling_mean = pd.Series(signal).rolling(window).mean()
rolling_std = pd.Series(signal).rolling(window).std()

# Simple rule: changepoint if abs difference in rolling mean > threshold
threshold = 2 * np.nanmean(rolling_std)
change_indices = np.where(np.abs(np.diff(rolling_mean)) > threshold)[0]

# Map indices to dates (+1 because diff reduces length by 1)
change_dates = df.iloc[change_indices + 1].copy()
change_dates = change_dates[['Date']]  # Only keep date column

# Save to CSV
change_dates.to_csv(output_path, index=False)
