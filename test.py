import streamlit as st
from groupStageAnalysis import *
from knockoutStageAnalysis import *

# TODO : delete lorem
lorem = "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi Player oluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?"
team_text = """Pour la réalisation de ce dashboard, j'ai manipulé deux Datasets : 
    [Group Stage Dataset](https://www.kaggle.com/kaggle/soccer-dataset/data) et 
    [Knockout Stage Dataset](https://www.kaggle.com/kaggle/soccer-dataset/data).  
    Ceux-ci contiennent des données tirées d’une compétition mondiale du jeu vidéo 
    **“League of Legends”** qui à eu lieu en **2018**.  
    Les tableaux montrent des données par joueur : 
    nombre de morts, nombre d’assassinat, et pleins d’autres métriques propres au jeu.  
    Les deux Datasets suivent le même schéma de données :  
    l’un est à propos de la **phase de “Pools”**, 
    l’autre des **phases “Éliminatoires”**."""

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
    return float(player_metric(player, metric, True)) - float(player_metric(player, metric))


st.set_page_config(
    layout="wide",
)

a, b, c, d, e, f = st.columns(6)

a.title("Dashboard")
page = b.selectbox('', options=['Team', 'Player'])

if page == 'Team':
    st.subheader("Team stats against competition mean stats")

    c1, c2, c3 = st.columns(3)

    option = c1.selectbox('', ('Group phase', 'Knockout'))

    col1, col2, col3 = st.columns(3)
    barGraphByStat = groupBarGraphByStat if option == 'Group phase'else knockoutBarGraphByStat
    with col1:
        st.pyplot(barGraphByStat('KDA Ratio'))
        st.pyplot(barGraphByStat('Kill Participation'))
    with col2:
        st.pyplot(barGraphByStat('Assists'))
        st.pyplot(barGraphByStat('Deaths'))
    with col3:
        st.pyplot(barGraphByStat('CS Per Minute'))
        st.markdown(team_text)

elif page == 'Player':
    c1, c2 = st.columns([2, 4])
    player = c1.selectbox('Player', team_players)
    c2.markdown(lorem)

    d1, z, d2, d3, d4, d5, d6 = st.columns([0.5, 1, 1, 1, 1, 1, 1])
    d1.image(f"images/{player.lower()}.png")
    d2.metric(metrics[0], player_metric(player, 0),
              round(player_metric_dif(player, 0), 1))
    d3.metric(metrics[1], player_metric(player, 1),
              round(player_metric_dif(player, 1), 2))
    d4.metric(metrics[2], player_metric(player, 2),
              round(player_metric_dif(player, 2), 0))
    d5.metric(metrics[3], player_metric(player, 3),
              round(player_metric_dif(player, 3), 0))
    d6.metric(metrics[4], player_metric(player, 4),
              round(player_metric_dif(player, 4), 1))

    e1, e2 = st.columns([2, 4])
    metric = e1.selectbox('Metric', metrics)

    f1, f0, f2 = st.columns([2, 0.5, 2])
    f2.pyplot(groupBarGraphByStatByPosition(player_position[player], metric))
    f1.pyplot(knockoutBarGraphByStatByPosition(
        player_position[player], metric))
