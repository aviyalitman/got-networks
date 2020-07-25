import os
import sys
sys.path.append(os.path.realpath('.'))
from src import utilities, network
from src.network import Network

jon_craster = Network('Jon', 'Craster')

are_they_friends = jon_craster.are_they_friends()
# print(are_they_friends)
'''
True
'''

mutual_friends = jon_craster.friends()
# print(mutual_friends)
'''
['Aemon', 'Alliser', 'Arya', 'Bran', 'Craster', 'Eddard', 'Eddison', 'Gilly', 
'Janos', 'Jon', 'Mance', 'Meera', 'Melisandre', 'Rattleshirt', 'Robb', 'Robert', 
'Samwell', 'Sansa', 'Stannis', 'Val', 'Ygritte', 'Grenn', 'Theon', 'Karl', 'Dalla', 
'Orell', 'Qhorin', 'Styr']
'''

network = jon_craster.find_network()
# print(network)
'''
     Source Middleman_1  Middleman_2 Target
0   Craster       Mance        Dalla    Jon
1   Craster       Mance        Gilly    Jon
2   Craster       Mance       Qhorin    Jon
3   Craster       Mance  Rattleshirt    Jon
4   Craster       Mance         Styr    Jon
5   Craster       Mance          Val    Jon
6   Craster       Mance      Ygritte    Jon
7   Craster     Samwell      Eddison    Jon
8   Craster     Samwell        Gilly    Jon
9   Craster     Samwell        Grenn    Jon
10  Craster     Samwell        Janos    Jon
11  Craster     Samwell        Mance    Jon
12  Craster     Samwell       Qhorin    Jon
13  Craster     Samwell        Aemon    Jon
14  Craster       Mance      Alliser    Jon
15  Craster     Samwell         Bran    Jon
16  Craster       Mance        Janos    Jon
17  Craster       Gilly        Mance    Jon
18  Craster     Samwell        Meera    Jon
19  Craster     Samwell   Melisandre    Jon
20  Craster       Gilly      Samwell    Jon
21  Craster       Mance      Samwell    Jon
22  Craster     Samwell      Stannis    Jon
'''

cersei_dany = Network('Cersei', 'Dany')

are_they_friends2 = cersei_dany.are_they_friends()
# print(are_they_friends)
'''
False
'''

friends2 = cersei_dany.friends()
# print(friends2)
'''
['Arya', 'Brienne', 'Bronn', 'Catelyn', 'Eddard', 'Gregor', 'Jaime', 'Joffrey', 
'Lysa', 'Meryn', 'Robert', 'Sandor', 'Sansa', 'Shae', 'Tyrion', 'Tywin', 'Varys', 
'Elia', 'Ilyn', 'Pycelle']
'''

network2 = cersei_dany.find_network()
#print(network2)
'''
Could not find third degree relationships for these two characters.
'''

dany_robb = Network('Daenerys', 'Robb')

network3 = dany_robb.find_network()
# print(network3)
'''
  Source Middleman_1 Middleman_2    Target
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
'''
