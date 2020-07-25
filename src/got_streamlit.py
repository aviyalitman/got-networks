import streamlit as st
import numpy as np
import pandas as pd
import utilities, network
from network import Network
from PIL import Image
import graphviz as graphviz


st.title('Social Networks in Game of Thrones')
image = Image.open('got.jpg')
st.image(image, caption='Who knows who in Storm of Swords (ASOIAF, Book Three)?', use_column_width=True)

got_nodes = pd.read_csv("got-nodes.csv")
characters = got_nodes['Id']

character1 = st.sidebar.selectbox(
    'Choose a GOT character',
     characters)
    
character2 = st.sidebar.selectbox(
    'Choose another GOT character',
     characters)


if character1 != character2 and st.sidebar.button('Go!'):

    relationship = Network(character1, character2)

    # first degree relationship
    are_they_friends = relationship.are_they_friends()

    if are_they_friends == True:
        st.subheader("**{}** and **{}** appeared together in Storm of Swords.".format(character1, character2))
    else:
        st.subheader("**{}** and **{}** did **not** appear together in Storm of Swords.".format(character1, character2))

    # second degree relationships
    mutual_friends = relationship.friends() 

    if len(mutual_friends) > 0:
        friend_string = ', '.join(mutual_friends)
        st.subheader("The following characters have appeared with both {} and {}:".format(character1, character2))
        st.write(friend_string)
    
    # third degree relationships
    network = relationship.find_network()
    st.subheader("{} and {}'s full relationship network:".format(character1, character2))
    st.dataframe(network)

    # creating a graph visual 
    graph = graphviz.Graph()
    graph.attr(size="10,10")

    for middleman_1 in np.unique(network['Middleman_1']):
        graph.edge(character1, middleman_1)
    
    for middleman_1, middleman_2 in zip(network['Middleman_1'], network['Middleman_2']):
        graph.edge(middleman_1, middleman_2)
    
    for middleman_2 in np.unique(network['Middleman_2']):
        graph.edge(middleman_2, character2)

    st.graphviz_chart(graph, use_container_width=True)

    st.write("*Appeared is defined as names mentioned within 15 words of each other in SoS.*")

else:
    st.write("Please select two characters.")


