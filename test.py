import streamlit as st
from groupStageAnalysis import *
from knockoutStageAnalysis import *

# TODO : delete lorem
lorem = "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi Player oluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?"
team_players = ("Hjärnan", "Jankos", "Perkz", "Wadid", "Wunder")
metrics = ("KDA Ratio", "Kill Participation", "Assists", "Deaths", "CS Per Minute")

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
        st.markdown(lorem)

elif page == 'Player':
    c1, c2 = st.columns([2, 4])
    option = c1.selectbox('Player', team_players)
    c2.markdown(lorem)

    d1, z, d2, d3, d4, d5, d6 = st.columns([0.5, 1, 1, 1, 1, 1, 1])
    d1.image(f"images/{option.lower()}.png")
    d2.metric("KDA Ratio", "4.2", "0.5")
    d3.metric("Kill Participation", "0.68 %", "-0.01 %")
    d4.metric("Assists", "47", "-4")
    d5.metric("Deaths", "13", "2")
    d6.metric("CS Per Minute", "10.2", "0.2")

    e1, e2 = st.columns([2, 4])
    option = e1.selectbox('Metric', metrics)
    f1, f2 = st.columns(2)
    f2.pyplot(groupBarGraphByStat(option))
    f1.pyplot(knockoutBarGraphByStat(option))

