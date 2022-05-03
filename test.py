import streamlit as st
from analysis import *

# TODO : delete lorem
lorem = "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi Player oluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?"

st.set_page_config(
    layout="wide",
)

a, b, c, d, e, f = st.columns(6)

a.title("Dashboard")
page = b.selectbox('', options=['Team', 'Player'])

if page == 'Team':
    st.subheader("Comparing team stats with competition mean stats")

    c1, c2, c3 = st.columns(3)

    option = c1.selectbox('', ('Group phase', 'Knockout'))

    col1, col2, col3 = st.columns(3)
    if option == 'Group phase':
        with col1:
            st.pyplot(barGraphByStat('KDA Ratio'))
            st.pyplot(barGraphByStat('KDA Ratio'))
        with col2:
            st.pyplot(barGraphByStat('Kill Participation'))
            st.pyplot(barGraphByStat('Deaths'))
        with col3:
            st.pyplot(barGraphByStat('CS Per Minute'))
            st.markdown(lorem)