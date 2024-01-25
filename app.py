import streamlit as st
from src import query_search
import pandas as pd
import numpy as np
import faiss

# -- Set page config
apptitle = 'ProjectPro Search Bar'

st.set_page_config(page_title=apptitle, page_icon="search")
st.image('Project pro logo_black.png', width=350)
# Title the app
st.title('ProjectPro Search Bar')
# read data
df = pd.read_csv("data/project_mappings.csv")

# load index
index = faiss.read_index('output/search.index')


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def remote_css(url):
    st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)    

def icon(icon_name):
    st.markdown(f'<i class="material-icons">{icon_name}</i>', unsafe_allow_html=True)

local_css("style.css")
remote_css('https://fonts.googleapis.com/icon?family=Material+Icons')

selected = st.text_input("", "Search...")
enter = st.button("Okay")
    


if selected:
    try:
        results_df=query_search.search(selected, index, 10,df)
    
    except Exception as e:
        print(e)
        st.write("No relevant results found for your query. Please enter a valid query!")
    else:
        st.write(results_df,unsafe_allow_html=True)

else:
    st.write("Please enter a valid query!")


