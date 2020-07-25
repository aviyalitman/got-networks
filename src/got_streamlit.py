import streamlit as st
import numpy as np
import pandas as pd
import utilities

st.title('Relationship Networks in Game of Thrones')

got_nodes = pd.read_csv("got-nodes.csv")
characters = got_nodes['Id']


character1 = st.selectbox(
    'Choose a GOT character',
     characters)
    
character2 = option = st.selectbox(
    'Choose another GOT character',
     characters)

'You selected: ', character1, 'and', character2

path = utilities.find_path(character1, character2)
st.write(path)


