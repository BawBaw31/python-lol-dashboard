import pandas as pd

# Read Groups stage CSV
group_phase_dataset = pd.read_csv(
    "./datasets/LOL Worlds 2018 Groups stage - Player Ratings.csv")

# Cleaning the data
dividable_columns = ["Kills Total", "Deaths", "Assists",
                     "CS Total", "Minutes Played", "Games Played"]

# Cleaning Rikara values => he played 2 times the number of games and that's not possible


def clean_row(i):
    for x in dividable_columns:
        group_phase_dataset.at[48, x] = group_phase_dataset.at[48, x] / 2


clean_row(48)

# Error => Jizuke is not a toplaner but a midlaner
group_phase_dataset.at[49, "Position"] = "Mid"

# Create new clean CSV
group_phase_dataset.to_csv("./datasets/group_stage.csv", index=False)

# Knockout dataset
knockout_stage_dataset = pd.read_csv(
    "/home/bawbaw31/Documents/datasets/LOL Worlds 2018 Knockout stage - Player Ratings.csv")

# Rename columns
knockout_stage_dataset = knockout_stage_dataset.rename(columns={"Kills(Total)": "Kills Total",
                                                                "Assists(Total)": "Assists", "CS(Per Minute)": "CS Per Minute",
                                                                "CS(Total)": "CS Total", "Deaths(Total)": "Deaths"})

# Create new clean CSV
knockout_stage_dataset.to_csv("./datasets/knockout_stage.csv", index=False)
