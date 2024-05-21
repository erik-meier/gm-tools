import pandas as pd
from pathlib import Path
from pprint import pprint

def filter_monsters_by_cr(df):
    """
    Monsters with a challenge rating of N/A are companions or retainers
    and should not be used for encounter building
    """
    return df[df["Challenge Rating"] != "N/A"]

def load_monsters():
    """
    Reads all CSV files from resources directory to compile monsters list.
    """
    dir = Path("resources")
    files = dir.glob("*.csv")
    df = pd.concat(pd.read_csv(file) for file in files)
    return filter_monsters_by_cr(df)

if __name__=="__main__":
    data = load_monsters()