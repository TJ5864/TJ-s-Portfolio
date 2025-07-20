import pandas as pd 

url1 = "https://www.cbssports.com/fantasy/football/stats/QB/2024/season/projections/ppr/"
url2 = "https://www.cbssports.com/fantasy/football/stats/RB/2024/season/projections/ppr/"
url3 = "https://www.cbssports.com/fantasy/football/stats/WR/2024/season/projections/ppr/"
url4 = "https://www.cbssports.com/fantasy/football/stats/TE/2024/season/projections/ppr/"
url5 = "https://www.cbssports.com/fantasy/football/stats/K/2024/season/projections/ppr/"
url6 = "https://www.cbssports.com/fantasy/football/stats/DST/2024/season/projections/ppr/"


positions = ["QB", "RB", "WR", "TE",  "K", "DST"]
position_tables = dict.fromkeys(positions)
position_tables["QB"] = pd.read_html(url1)[0]
position_tables["RB"] = pd.read_html(url2)[0]
position_tables["WR"] = pd.read_html(url3)[0]
position_tables["TE"] = pd.read_html(url4)[0]
position_tables["K"] = pd.read_html(url5)[0]
position_tables["DST"] = pd.read_html(url6)[0]

#add player position so we cna combine tables later 
for position in positions:
    position_tables[position]["Position"] = position

combined_df = pd.concat(position_tables.values(), ignore_index=True)
combined_df.to_csv("Data/all_positions_2024_projections.csv", index=False)

print(f"Combined data saved! Total rows: {len(combined_df)}")

    




