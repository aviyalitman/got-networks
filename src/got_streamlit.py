import streamlit as st
import numpy as np
import pandas as pd
import utilities, network
from network import Network

st.title('Character Relationships in Game of Thrones')
st.write('Who knows who in Storm of Swords (ASOIAF, Book Three)?')

got_nodes = pd.read_csv("got-nodes.csv")
characters = got_nodes['Id']

character1 = st.sidebar.selectbox(
    'Choose a GOT character',
     characters)
    
character2 = st.sidebar.selectbox(
    'Choose another GOT character',
     characters)

if character1 != character2:

    if st.button('Go!'):

        st.write('You selected: ', character1, 'and', character2)

        relationship = Network(character1, character2)

        # first degree relationship
        are_they_friends = relationship.are_they_friends()

        if are_they_friends == True:
            st.write("{} and {} have appeared together in Storm of Swords.".format(character1, character2))
        else:
            st.write("{} and {} have not appeared together in Storm of Swords.".format(character1, character2))

        # second degree relationships
        mutual_friends = relationship.friends() 

        if len(mutual_friends) > 0:
            friend_string = ', '.join(mutual_friends)
            st.write("The following characters have appeared with both {} and {}: {}".format(character1, character2, friend_string))

        # third degree relationships
        network = relationship.find_network()
        st.write("{} and {}'s full relationship network:".format(character1, character2))
        st.write(network)

else:
    print("Please select two different characters.")


