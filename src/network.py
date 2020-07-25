import utilities
import pandas as pd

class Network:
    """
    Class Network discovers first, second, and third degree relationships between characters.
    A first degree relationship is the characters appearing within 15 words of each other 
    in Storm of Swords.
    A second degree relationship is defined as a third character who has appeared within
    15 words of both characters 1 and 2. 
    A third degree relationship is defined as character 1 appearing within 15 words of  
    another character who appears within 15 words of another character who appears within
    15 words of character 2.

    Parameters
    __________
    character1 : string, cannot be None, must be present in got-nodes.csv
    character 2 : string, cannot be None, must be present in got-nodes.csv
    """
    
    def __init__(self, character1, character2):

        self.character1 = character1
        self.character2 = character2
        
        utilities.drop_tables(['all_edges', 'one_hop', 'two_hop'])
        utilities.all_edges()
        utilities.one_hop(self.character1, self.character2)
        utilities.two_hop(self.character1, self.character2)


    def are_they_friends(self):
        '''
        Boolean method to determine if the two characters have appeared within 15 words
        of each other in ASOIAF Storm of Swords.
        
        Returns 
        _______
        True : if the characters have appeared together in the same scene.
        False : if they have not appeared together.
        '''

        q = """SELECT COUNT(*) as count FROM all_edges 
            WHERE all_edges.Source = %s
            AND all_edges.Target = %s"""

        res,data = utilities.run_q(q, args=(self.character1, self.character2))
        
        num_of_appearances = data[0]['count']
        
        if num_of_appearances != 0:
            return True
        else:
            return False
    
    
    def friends(self):
        '''
        A method that determines mutual friends. 
        
        Returns 
        _______
        mutual_friends : a list of all people who have appeared together with both 
        character 1 and character 2
        '''
        
        q = "SELECT DISTINCT one_hop.one_target FROM one_hop"
        res,data = utilities.run_q(q)
        
        mutual_friends = []
        for dictionary in data:
            mutual_friends.append(dictionary['one_target'])
        
        return mutual_friends

    
    def find_network(self):
        '''
        A method that determines the two characters' expanded third-degree network. 
        
        Returns 
        _______
        network : a DataFrame of third-degree relationships between character 1 and character 2.
        '''
    
        q = """SELECT DISTINCT a.one_source, a.one_target, a.two_target, b.one_target_1
            FROM 
            w4111midterm.one_hop as a 
            JOIN 
            w4111midterm.two_hop as b 
            ON a.two_target=b.two_target and a.two_source=b.two_source 
            WHERE a.one_source != b.one_target_1
            AND a.one_source != a.two_target
            AND a.one_target != b.one_target_1
            """

        res,data = utilities.run_q(q)
        
        # convert to dataframe 
        network = pd.DataFrame(data)
        
        # assign new names for clarity 
        new_names = {'one_source':'Source', 'one_target': 'Middleman_1', 'two_target':'Middleman_2', 'one_target_1':'Target'}
        network = network.rename(columns=new_names)

        if len(network) == 0:
            return "Could not find third degree relationships for these two characters."
        
        return network
    

        

