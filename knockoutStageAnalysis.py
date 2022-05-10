import pandas as pd
import matplotlib.pyplot as plt

knockout_stage_dataset = pd.read_csv("/home/bawbaw31/Documents/datasets/LOL Worlds 2018 Knockout stage - Player Ratings.csv")

knockout_stage_dataset = knockout_stage_dataset.rename(columns={"Kills(Total)": "Kills Total",
"Assists(Total)": "Assists", "CS(Per Minute)": "CS Per Minute",
"CS(Total)": "CS Total", "Deaths(Total)": "Deaths",})

# My team stats
team_stats = knockout_stage_dataset[(knockout_stage_dataset["Team"] == "G2")].reset_index().sort_values(by=['Position'])

# Global stats by position
aggregation = {"KDA Ratio" : "mean",
              "Kills Total" : "sum",
              "Deaths" : "sum",
              "Assists" : "sum",
              "Kill Participation" : "mean",
              "CS Per Minute" : "mean",
              "CS Total" : "sum",
              "Minutes Played" : "sum",
              "Games Played" : "sum"}
mean_stats_by_team_by_position = knockout_stage_dataset.groupby(["Team", "Position"]).agg(aggregation).reset_index()

# Function stats by position for the error bars
def getStatByTeamByPosition(position, stat):
    return mean_stats_by_team_by_position[(mean_stats_by_team_by_position["Position"] == position)].reset_index()[stat]

# Mean stats by positions
mean_stats_by_position = mean_stats_by_team_by_position.groupby(["Position"]).mean().round(1).reset_index().sort_values(by=['Position'])

def knockoutBarGraphByStat(stat):
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])

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
    # ax.title(stat + " Per Position")
    ax.set_xlabel("Position")
    ax.set_ylabel(stat)
    
    # Legend
    colors = {'Other teams':'yellow', 'G2':'pink'}
    labels = list(colors.keys())
    handles = [plt.Rectangle((0,0),1,1, color=colors[label]) for label in labels]
    ax.legend(handles, labels)

    # ax.savefig('graph_' + stat + '.png')
    return fig