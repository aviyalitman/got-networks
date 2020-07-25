import os
import sys
sys.path.append(os.path.realpath('.'))
from src import utilities


#roose_craster = utilities.find_path('Roose', 'Craster')
#print(roose_craster)
"""
0  Craster         Jon        Arya  Roose
1  Craster         Jon        Robb  Roose
"""

#dany_robb = utilities.find_path('Daenerys', 'Robb')
#print(dany_robb)
"""
0   Robb        Arya      Robert  Daenerys
1   Robb      Eddard      Robert  Daenerys
2   Robb       Jaime   Barristan  Daenerys
3   Robb       Jaime      Robert  Daenerys
4   Robb         Jon      Robert  Daenerys
5   Robb       Sansa      Robert  Daenerys
6   Robb      Tyrion      Robert  Daenerys
7   Robb       Tywin      Robert  Daenerys
8   Robb     Stannis      Robert  Daenerys
9   Robb      Tyrion     Viserys  Daenerys
"""

#jon_cersei = utilities.find_path('Jon', 'Cersei')
#print(jon_cersei)
"""
0   Cersei        Arya        Bran    Jon
1   Cersei        Arya      Robert    Jon
2   Cersei     Catelyn        Bran    Jon
3   Cersei     Catelyn        Robb    Jon
4   Cersei     Catelyn       Sansa    Jon
5   Cersei     Catelyn     Stannis    Jon
6   Cersei      Eddard        Arya    Jon
7   Cersei      Eddard        Bran    Jon
8   Cersei      Eddard        Robb    Jon
9   Cersei      Eddard      Robert    Jon
10  Cersei      Eddard       Sansa    Jon
11  Cersei       Jaime      Robert    Jon
12  Cersei       Jaime     Stannis    Jon
13  Cersei     Joffrey     Stannis    Jon
14  Cersei      Robert       Aemon    Jon
15  Cersei      Robert     Stannis    Jon
16  Cersei      Sandor      Robert    Jon
17  Cersei       Sansa        Arya    Jon
18  Cersei       Sansa        Bran    Jon
19  Cersei       Sansa      Robert    Jon
20  Cersei      Tyrion       Janos    Jon
21  Cersei      Tyrion      Robert    Jon
22  Cersei      Tyrion     Stannis    Jon
23  Cersei       Tywin      Robert    Jon
24  Cersei       Tywin     Stannis    Jon
25  Cersei       Tywin         Val    Jon
26  Cersei      Gregor        Arya    Jon
27  Cersei       Jaime        Arya    Jon
28  Cersei     Joffrey        Arya    Jon
29  Cersei      Robert        Arya    Jon
30  Cersei      Sandor        Arya    Jon
31  Cersei      Tyrion        Arya    Jon
32  Cersei        Arya      Eddard    Jon
33  Cersei     Catelyn      Eddard    Jon
34  Cersei       Jaime      Eddard    Jon
35  Cersei      Robert      Eddard    Jon
36  Cersei      Sandor      Eddard    Jon
37  Cersei       Sansa      Eddard    Jon
38  Cersei        Arya        Robb    Jon
39  Cersei     Brienne        Robb    Jon
40  Cersei       Jaime        Robb    Jon
41  Cersei     Joffrey        Robb    Jon
42  Cersei       Sansa        Robb    Jon
43  Cersei      Tyrion        Robb    Jon
44  Cersei       Tywin        Robb    Jon
45  Cersei        Arya       Sansa    Jon
46  Cersei     Brienne       Sansa    Jon
47  Cersei       Jaime       Sansa    Jon
48  Cersei     Joffrey       Sansa    Jon
49  Cersei        Lysa       Sansa    Jon
50  Cersei      Robert       Sansa    Jon
51  Cersei      Sandor       Sansa    Jon
52  Cersei        Shae       Sansa    Jon
53  Cersei      Tyrion       Sansa    Jon
"""

#dany_cersei = utilities.find_path('Dany', 'Cersei')
#print(dany_cersei)