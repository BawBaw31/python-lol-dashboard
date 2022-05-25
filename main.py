import streamlit as st
from groupStageAnalysis import *
from knockoutStageAnalysis import *

team_text = """Pour la réalisation de ce dashboard, j'ai manipulé deux Datasets :  
    [Group Stage Dataset](https://www.kaggle.com/datasets/kaushikburra/lol-worlds-2018-groups-stage-player-ratings) & 
    [Knockout Stage Dataset](https://www.kaggle.com/datasets/kaushikburra/lol-worlds-2018-knockout-stage-player-ratings).  
    Ceux-ci contiennent des données tirées d’une compétition mondiale du jeu vidéo 
    **“League of Legends”** qui à eu lieu en **2018**.  
    Les tableaux montrent des statistiques par joueur : 
    nombre de morts, nombre d’assassinat, et pleins d’autres métriques propres au jeu.  
    Les deux Datasets suivent le même schéma de données :  
    l'un est à propos de la **phase de “Pools”**, 
    l'autre de la **phase “Éliminatoire”**.  
    J'ai fait le choix de suivre l'équipe **G2** afin de donner un retour sur la performance 
    des joueurs de cette équipe."""

def players_text(player):
    adj = "au "
    position = player_position[player]
    if position == "ADC":
        adj = "en tant qu'"
    elif position == "Support":
        adj = "en tant que "
    elif position == "Jungle":
        adj = "en "
    return f"<h3 style='text-align: center;'>Ici vous pouvez voir la progression de {player} qui évolue {adj}{position}!</h3>"

team_players = ("Hjärnan", "Jankos", "Perkz", "Wadid", "Wunder")
player_position = {
    "Hjärnan": "ADC",
    "Jankos": "Jungle",
    "Perkz": "Mid",
    "Wadid": "Support",
    "Wunder": "Top"
}
metrics = ("KDA Ratio", "Kill Participation",
           "Assists", "Deaths", "CS Per Minute")


def player_metric(player, metric, old=None):
    dataset = group_phase_dataset if old else knockout_stage_dataset
    return dataset[(dataset["Name"] == player)][metrics[metric]]


def player_metric_dif(player, metric):
    return float(player_metric(player, metric)) - float(player_metric(player, metric, True))

# Streamlit Frontend
st.set_page_config(
    layout="wide",
)

a, b, c = st.columns([1.5, 0.5, 4])

a.title("G2 Esport Dashboard")
page = b.selectbox('', options=['Team', 'Joueurs'])

if page == 'Team':

    c1, c2 = st.columns([1, 2])
    option = c1.selectbox('', ('Phase de Pool', 'Phase Eliminatoire'))

    st.markdown("<h3 style='text-align: center;'>Statistiques de l'équipe G2 par rapport aux statistiques moyennes de la compétition</h3>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 20px; font-style: italic;'>(KDA, Kill Participation, Assists, Deaths, CS/min)</p>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    barGraphByStat = groupBarGraphByStat if option == 'Phase de Pool'else knockoutBarGraphByStat
    with col1:
        st.pyplot(barGraphByStat('KDA Ratio'))
        st.pyplot(barGraphByStat('Kill Participation'))
    with col2:
        st.pyplot(barGraphByStat('Assists'))
        st.pyplot(barGraphByStat('Deaths'))
    with col3:
        st.pyplot(barGraphByStat('CS Per Minute'))
        st.markdown(team_text)

elif page == 'Joueurs':
    c1, c2 = st.columns([2, 4])
    player = c1.selectbox('Joueur', team_players)
    c2.markdown(players_text(player), unsafe_allow_html=True)

    d1, z, d2, d3, d4, d5, d6 = st.columns([0.5, 1, 1, 1, 1, 1, 1])
    d1.image(f"images/{player.lower()}.png")
    d2.metric(metrics[0], player_metric(player, 0),
              round(player_metric_dif(player, 0), 1))
    d3.metric(metrics[1], player_metric(player, 1),
              round(player_metric_dif(player, 1), 2))
    d4.metric(metrics[2], player_metric(player, 2),
              round(player_metric_dif(player, 2), 0))
    d5.metric(metrics[3], player_metric(player, 3),
              round(player_metric_dif(player, 3), 0), "inverse")
    d6.metric(metrics[4], player_metric(player, 4),
              round(player_metric_dif(player, 4), 1))

    e1, e2 = st.columns([2, 4])
    metric = e1.selectbox('Statistique', metrics)

    f1, f0, f2 = st.columns([2, 0.5, 2])
    f1.markdown("<h3 style='text-align: center;'>Phase de Pool</h3>", unsafe_allow_html=True)
    f1.pyplot(groupBarGraphByStatByPosition(player_position[player], metric))
    f2.markdown("<h3 style='text-align: center;'>Phase Eliminatoire</h3>", unsafe_allow_html=True)
    f2.pyplot(knockoutBarGraphByStatByPosition(
        player_position[player], metric))
