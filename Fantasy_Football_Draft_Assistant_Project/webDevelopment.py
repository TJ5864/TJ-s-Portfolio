import streamlit as st 
import pandas as pd
import re 
import os
from openai import OpenAI
from pandasai import SmartDataframe

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])


df = pd.read_csv("Data/cleaned_player_projections.csv")


if "drafted_by_me" not in st.session_state:
    st.session_state.drafted_by_me = []
if "drafted_by_others" not in st.session_state:
    st.session_state.drafted_by_others = []

st.title("Fantasy Football Draft Assistant")
st.subheader("🤖 AI-Powered Fantasy Draft Advisor")
position = st.selectbox("Choose a position to view top players:", ["QB", "RB", "WR", "TE", "K", "DST"])

pattern = re.compile(rf"\b{position}\b", re.IGNORECASE)
filtered_df = df[df["Player"].str.contains(pattern)]

# Remove already drafted
drafted_all = st.session_state.drafted_by_me + st.session_state.drafted_by_others
available = filtered_df[~filtered_df["Player"].isin(drafted_all)]
top_players = available.sort_values(by="Fantasy Points", ascending=False).head(10)

st.subheader(f"Top {position}s Available")

# Show players and add buttons
for _, row in top_players.iterrows():
    col1, col2, col3 = st.columns([3, 1, 1])
    col1.markdown(f"**{row['Player']}** — {row['Fantasy Points']} pts")
    if col2.button("Draft Me", key=f"me_{row['Player']}"):
        st.session_state.drafted_by_me.append(row['Player'])
    if col3.button("Drafted by Other", key=f"other_{row['Player']}"):
        st.session_state.drafted_by_others.append(row['Player'])

# Show current drafted lists
with st.expander("📋 View Drafted Players"):
    st.write("**Drafted by You:**", st.session_state.drafted_by_me)
    st.write("**Drafted by Others:**", st.session_state.drafted_by_others)    


# adding AI chat bot
user_query = st.text_area("Ask your AI assistant about your data (e.g. 'Who are the top 5 RBs with highest fantasy points?'):")
if st.button("Ask AI About My Data") and user_query:
    with st.spinner("Analyzing your data..."):
        from pandasai.llm import OpenAI
        llm = LocalLLM(api_key=st.secrets["OPENAI_API_KEY"], model="gpt-4-turbo")
        sdf = SmartDataframe(df, config={"llm": llm})
        try:
            answer = sdf.chat(user_query)
            st.write(answer)
        except Exception as e:
            st.error(f"Error: {e}")
        



