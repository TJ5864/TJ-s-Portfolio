import pandas as pd 



try:
    df = pd.read_csv("Data/all_positions_2024_projections.csv", header=[0, 1])
    df.columns = [' '.join(col).strip() for col in df.columns]
except:
    df = pd.read_csv("Data/all_positions_2024_projections.csv")
    df.columns = df.columns.str.strip()

# Optional: Fill NaNs with 0
df.fillna(0, inplace=True)

df.rename(columns={
    'Unnamed: 0_level_0 Player': 'Player',
    'Position Unnamed: 16_level_1': 'Position',
    'Misc fpts  Fantasy Points': 'Fantasy Points',
    'Misc fppg  Fantasy Points Per Game': 'Fantasy Points Per Game',
    'Unnamed: 0_level_0 Team': 'Team',
}, inplace=True)
# Save cleaned version
df.to_csv("Data/cleaned_player_projections.csv", index=False)

# Print column names to verify
print(df.columns.tolist())