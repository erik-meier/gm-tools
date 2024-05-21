import pandas as pd
from pathlib import Path
from pprint import pprint

def load_monsters():
    """
    Reads all CSV files from resources directory to compile monsters list.
    """
    dir = Path("resources")
    files = dir.glob("*.csv")
    data = []
    for file in files:
        df = pd.read_csv(file)
        df = df[df["Challenge Rating"] != "N/A"]
        data.append(df)
    return pd.concat(data)

if __name__=="__main__":
    data = load_monsters()