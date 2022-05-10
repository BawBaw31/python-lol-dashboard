import pandas as pd
import matplotlib.pyplot as plt

# plt.style.use('seaborn-dark')

# Read Groups stage CSV
group_phase_dataset = pd.read_csv("./datasets/LOL Worlds 2018 Groups stage - Player Ratings.csv")

# Cleaning the data
dividable_columns = ["Kills Total", "Deaths", "Assists", "CS Total", "Minutes Played", "Games Played"]

# Cleaning Rikara values => he played 2 times the number of games and that's not possible
def clean_row(i):
    for x in dividable_columns:
        group_phase_dataset.at[48, x] = group_phase_dataset.at[48, x] / 2
        
clean_row(48)

# Error => Jizuke is not a toplaner but a midlaner
group_phase_dataset.at[49, "Position"] = "Mid"

# My team stats
team_stats = (group_phase_dataset[(group_phase_dataset["Team"] == "G2")]
.reset_index().sort_values(by=['Position']))

# Global stats by position
aggregation = {
    "KDA Ratio" : "mean",
    "Kills Total" : "sum",
    "Deaths" : "sum",
    "Assists" : "sum",
    "Kill Participation" : "mean",
    "CS Per Minute" : "mean",
    "CS Total" : "sum",
    "Minutes Played" : "sum",
    "Games Played" : "sum"
}
mean_stats_by_team_by_position = (group_phase_dataset
.groupby(["Team", "Position"]).agg(aggregation).reset_index())

# Function stats by position for the error bars
def getStatByTeamByPosition(position, stat):
    return (mean_stats_by_team_by_position[
        (mean_stats_by_team_by_position["Position"] == position)]
        .reset_index()[stat])

# Mean stats by positions
mean_stats_by_position = mean_stats_by_team_by_position.groupby(["Position"]).mean().round(1).reset_index().sort_values(by=['Position'])

# Create graph function
def groupBarGraphByStat(stat):
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])
    # ax.set_facecolor('xkcd:salmon')

    barWidth = 0.4
    y1 = mean_stats_by_position[stat]
    y2 = team_stats[stat]
    r1 = range(len(y1))
    r2 = [x + barWidth for x in r1]

    # Bar Graph
    ax.bar(r1, y1, width = barWidth, color = ['yellow' for i in y1], linewidth = 2)
    ax.bar(r2, y2, width = barWidth, color = ['pink' for i in y1], linewidth = 4)
    ax.set_xticks([r + barWidth / 2 for r in r1], mean_stats_by_position['Position'])
    
    # Error Bar
    error = []
    for position in mean_stats_by_position['Position']:
        stats_by_position = getStatByTeamByPosition(position, stat)
        error.append(stats_by_position.std())
    ax.errorbar(mean_stats_by_position['Position'], y1, yerr=error, fmt="o", color="r")

    # Title & Labels
    # ax.set_title(stat + " Per Position")
    ax.set_xlabel("Position")
    ax.set_ylabel(stat)
    
    # Legend
    colors = {'Other teams':'yellow', 'G2':'pink'}
    labels = list(colors.keys())
    handles = [plt.Rectangle((0,0),1,1, color=colors[label]) for label in labels]
    ax.legend(handles, labels)

    # plt.savefig('graph_' + stat + '.png')
    return fig