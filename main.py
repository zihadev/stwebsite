import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png", width=500)

with col2:
    st.title("Ardit")
    content = """Hi, I am Ardit! I am a Python programmer and a Python teacher. I have worked with companies from all over the world both as an employee and as self-employed using Python as both a data science tool and as a language to develop applications. Some of the projects I have worked on have been using Python together with the Center for Conservation Geography to map and understand the Australian ecosystems, processing drone land images with the Swiss in-Terra, and performing data mining to gain business insights with the Australian Rapid Intelligence.
"""
    st.info(content)