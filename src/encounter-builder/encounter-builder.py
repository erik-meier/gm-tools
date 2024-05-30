import pandas as pd
from pathlib import Path
from argparse import ArgumentParser
from pprint import pprint
from encounter import Encounter

def read_args():
    parser = ArgumentParser(
        prog="Encounter Builder",
        description="List possible encounters for DND 5e combat based on some inputs",
    )
    parser.add_argument("-f", dest="filepath", default="resources/encounter-builder", help="path to monster csv files")
    parser.add_argument("-n", dest="party_size", required=True, help="number of party members")
    parser.add_argument("-v", dest="party_level", required=True, help="mean level of party")
    parser.add_argument("-t", dest="monster_type", help="type of monster to user for encounter")
    return parser.parse_args()

def cr_to_int(cr):
    if not isinstance(cr, str):
        return cr
    if "/" in cr:
        a, b = cr.split("/")
        return int(a)/int(b)
    return int(cr)

def filter_by_cr(df):
    """
    Monsters with a challenge rating of N/A are companions or retainers
    and should not be used for encounter building
    """
    return df[df["Challenge Rating"].notnull()]

def filter_by_entry(df, group):
    """
    Filter dataframe to only monsters of a certain type
    """
    if not group:
        return df
    return df[df["Entry"] == group]

def load_monsters(path):
    """
    Reads all CSV files from resources directory to compile monsters list.
    """
    dir = Path(path)
    files = list(dir.glob("*.csv"))
    if not files:
        return None
    df = pd.concat(pd.read_csv(file) for file in files)
    df["CR"] = df["Challenge Rating"].apply(lambda cr: cr_to_int(cr))
    return filter_by_cr(df)

def list_encounters_for_budget(data, cr_budget, max_size):
    """
    Given a CR budget, list all possible encounters that meet that budget using the monsters in data
    """
    incomplete = [Encounter()]
    complete = []
    while incomplete:
        curr = incomplete.pop(0)
        for index, row in data.iterrows():
            if curr.total + row["CR"] > cr_budget:
                continue
            new = curr.copy()
            new.add_monster(row["Creature Name"], row["CR"])
            if new.total == cr_budget:
                monsters = new.freeze()
                if monsters not in complete:
                    complete.append(monsters)
            else:
                incomplete.append(new)
    return complete


if __name__=="__main__":
    args = read_args()
    data = load_monsters(args.filepath)
    data = filter_by_entry(data, args.monster_type)
    encounters = list_encounters_for_budget(data, 1, 2*args.party_size)
    for encounter in encounters:
        print(encounter)
    