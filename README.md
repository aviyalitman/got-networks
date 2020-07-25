# Social Networks in Game of Thrones

The Game of Thrones/ ASOIAF world is so complex, with its hundreds of characters and settings. The story is so intricately composed that despite them being "scattered geographically and enmeshed in their own social circles," they are all related to each other somehow.
In this project, two characters are said to be related if they are mentioned within 15 words of each other in George R. R. Martin's  *A Storm of Swords*, the third novel in his series *A Song of Ice and Fire*. If the latter is true, then it is highly probable that the characters are either appearing in the same scene or talking about each other. 

This data was originally compiled by [A. Beveridge and J. Shan, "Network of Thrones," Math Horizons Magazine , Vol. 23, No. 4 (2016), pp. 18-22](https://www.maa.org/sites/default/files/pdf/Mathhorizons/NetworkofThrones%20%281%29.pdf).

## Data & Methodology

Nodes: 107; unimodal

Edges: 353; weighted; undirected

In this project, I use streamlit and Graphiz to simulate how two characters may know each other. For each pair of characters, I compute first, second, and third degree social networks. That is,

- First-degree: do the two characters know each other?
- Second-degree: who are the two characters' mutual friends/ enemies?
- Third-degree: who does a character know that knows someone that knows the other character?

## Streamlit Simulations

## ASOIAF

A quick summary of the story by [Beveridge and Shan](https://www.maa.org/sites/default/files/pdf/Mathhorizons/NetworkofThrones%20%281%29.pdf):

>The narrative starts at a time of peace, with all the houses unified under the rule of King Robert Baratheon, who holds the Iron Throne...[Then King Robert dies and all heck breaks loose.]

>Driven by cause or circumstance, characters from the many noble families launch into arduous and intertwined journeys. Among these houses are the honorable Stark family (Eddard, Catelyn, Robb, Sansa, Arya, Bran, and Jon Snow), the pompous Lannisters (Tywin, Jaime, Cersei, Tyrion, and Joffrey), the slighted Baratheons (led by Robert’s brother Stannis) and the exiled Daenerys, the last of the once powerful House Targaryen.

This project was inspired by my effort to remember all the character names and relationships after I finished reading the [ASOIAF series](https://georgerrmartin.com/book-category/?cat=song-of-ice-and-fire). 

