# Social Networks in Game of Thrones 

![jon_joff](/images/jon_joff.png)

Joffrey and Jon never actually met in *A Storm of Swords*, but their social network does not seem to be hurting. 

The Game of Thrones/ ASOIAF world is so complex, with its hundreds of characters and settings. The story is so intricately composed that despite the characters being "scattered geographically and enmeshed in their own social circles," they are all related to each other somehow.

I created a simulation of a graph database using MySQL and Python to discover 1st, 2nd, and 3rd-Degree Networks between any two characters. **This is basically the LinkedIn for Game of Thrones characters.**

Characters are said to be related if they are mentioned within 15 words of each other in George R. R. Martin's  *A Storm of Swords*, the third novel in his series *A Song of Ice and Fire*. If the latter is true, then it is highly probable that the characters are either appearing in the same scene or talking about each other. 

This was inspired by my effort to remember all the character names and relationships after I finished reading the five books in the [ASOIAF series](https://georgerrmartin.com/book-category/?cat=song-of-ice-and-fire) during quarantine. 

## Data & Methodology

Nodes: 107; unimodal

Edges: 353; undirected

I used Python, MySQL, streamlit, and Graphiz to create 1st, 2nd, and 3rd-Degree networks for a pair of characters that may show how they know each other in the world of ASOIAF. That is,

- 1st-Degree: do the two characters know each other?
- 2nd-Degree: who are the two characters' mutual friends (or enemies)?
- 3rd-Degree: which characters appear with 2nd-Degree connections?

## Examples

Daenerys Targaryen and Cersei Lannister:
![dany_cersei](/images/cersei_dany.png)

Samwell Tarly and Cersei Lannister:
![sam_cersei](/images/sam_cersei.png)

Jon Snow and Margaery Tyrell:
![jon_marg](/images/jon_marg.png)

## Streamlit Simulations

## ASOIAF

A quick summary of the story by [Beveridge and Shan](https://www.maa.org/sites/default/files/pdf/Mathhorizons/NetworkofThrones%20%281%29.pdf):

>The narrative starts at a time of peace, with all the houses unified under the rule of King Robert Baratheon, who holds the Iron Throne...[Then King Robert dies and all heck breaks loose.]

>Driven by cause or circumstance, characters from the many noble families launch into arduous and intertwined journeys. Among these houses are the honorable Stark family (Eddard, Catelyn, Robb, Sansa, Arya, Bran, and Jon Snow), the pompous Lannisters (Tywin, Jaime, Cersei, Tyrion, and Joffrey), the slighted Baratheons (led by Robert’s brother Stannis) and the exiled Daenerys, the last of the once powerful House Targaryen.

### Credits

This data was originally compiled by [A. Beveridge and J. Shan, "Network of Thrones," Math Horizons Magazine , Vol. 23, No. 4 (2016), pp. 18-22](https://www.maa.org/sites/default/files/pdf/Mathhorizons/NetworkofThrones%20%281%29.pdf).

I used the data from melaniewalsh's repository, sample-social-network-datasets. 

