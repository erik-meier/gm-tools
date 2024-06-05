import pandas as pd
from pathlib import Path
from argparse import ArgumentParser
from pprint import pprint
from encounter import Encounter, Difficulty
from monster import Monster

def read_args():
    parser = ArgumentParser(
        prog="Encounter Builder",
        description="List possible encounters for DND 5e combat based on some inputs",
    )
    parser.add_argument("-f", dest="filepath", default="resources/encounter-builder", help="path to monster csv files")
    parser.add_argument("-n", dest="party_size", type=int, required=True, help="number of party members")
    parser.add_argument("-v", dest="party_level", required=True, help="mean level of party")
    parser.add_argument("-d", dest="difficulty", type=str, help="encounter difficulty")
    parser.add_argument("-t", dest="monster_type", help="type of monster to user for encounter")
    args = parser.parse_args()
    args.difficulty = parse_difficulty(args.difficulty)
    return args

def parse_difficulty(diff_str):
    diff_str = diff_str.lower()
    if diff_str == "trivial":
        return Difficulty.TRIVIAL
    elif diff_str == "easy":
        return Difficulty.EASY
    elif diff_str == "hard":
        return Difficulty.HARD
    else:
        return Difficulty.STANDARD


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

def create_monster_from_row(row):
    return Monster(row["Creature Name"], cr_to_int(row["Challenge Rating"]), row["Role"])

def load_monsters(path, type):
    """
    Reads all CSV files from resources directory to compile monsters list.
    """
    dir = Path(path)
    files = list(dir.glob("*.csv"))
    if not files:
        return None
    df = pd.concat(pd.read_csv(file) for file in files)
    df = filter_by_cr(df)
    df = filter_by_entry(df, type)
    return df.apply(create_monster_from_row, axis=1)

def list_encounters_for_budget(data, cr_budget, max_size):
    """
    Given a CR budget, list all possible encounters that meet that budget using the monsters in data
    """
    incomplete = [Encounter()]
    complete = []
    monsters.sort_values()
    for m in monsters:
        for enc in incomplete:
            new = enc.copy()
            new.add_monster(m)
            if new.is_valid(cr_budget, max_size):
                complete.append(new)
            elif new.is_incomplete(cr_budget, max_size):
                incomplete.append(new)
    return complete

if __name__=="__main__":
    args = read_args()
    monsters = load_monsters(args.filepath, args.monster_type)
    encounters = list_encounters_for_budget(monsters, 1, 2*args.party_size)
    for encounter in encounters:
        encounter.print()