import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

# Custom CSS to set the width of the content
st.markdown(
    """
       <style>
       .main {
           max-width: 70%;
           margin: 0 auto;
       }
       .rounded-img {
           border-radius: 15px;
       }
       </style>
       """,
    unsafe_allow_html=True,
)

st.markdown("<h1 style='text-align: center;'>Ardit</h1>", unsafe_allow_html=True)
st.write("")
st.write("")
col1, col2 = st.columns(2)
with col1:

    st.image("images/photo.png")
with col2:
    content = """
    Hi, I am Ardit! I am a Python programmer and a Python teacher. I have worked with companies from all over the world both as an employee and as self-employed using Python as both a data science tool and as a language to develop applications. Some of the projects I have worked on have been using Python together with the Center for Conservation Geography to map and understand the Australian ecosystems, processing drone land images with the Swiss in-Terra, and performing data mining to gain business insights with the Australian Rapid Intelligence.

The vast range of things you can do with Python is just mindblowing. I have used that experience to teach Python to others from all over the world. I especially take care to explain the programming concepts always assuming my students don't have a computer science background. Indeed, you don't need a computer science degree to become a programmer. I was graduated with a Master of Science in Geospatial Technologies from the University of Muenster in Germany.

I am also the founder and author of PythonHow, a Python learning resource designed particularly for people with no previous programming experience. Try out my and you will be on for a very interesting ride.
    """
    st.info(content)

content2 = """
Below you can find some of the apps I have built in Python. Feel free to contact me!
"""


# Display a success box
st.success(content2)


col3, col4 = st.columns(2)
df = pd.read_csv("data.csv", sep=";")




with col3:
    for index, row in df.iterrows():
        if index % 2 == 0:  # Check if the index is even
            st.header(row['title'])
        # st.write(index, row)

with col4:
    for index, row in df.iterrows():
        if index % 2 != 0:  # Check if the index is even
            st.header(row['title'])