# Candidate elimination algorithm

import numpy as np
import pandas as pd

# take data from candidate csv
data = pd.DataFrame(data=pd.read_csv('candidate.csv'))

# use the concepts, every row along with columns , except the last row
concepts = np.array(data.iloc[:,0:-1]) # row and column [row , col]

# use the final column and all the rows
target = np.array(data.iloc[:,-1])

def learn(concepts, target):
    # the first specific h will be the first row 
    specific_h = concepts[0].copy()
    #print(specific_h) #['Sunny ' 'Warm ' 'Normal ' 'Strong ' 'Warm ']
    
    general_h = [["?" for i in range(len(specific_h))] for i in range(len(specific_h))]
    #print(general_h) #[['?', '?', '?', '?', '?'], ['?', '?', '?', '?', '?'], ['?', '?', '?', '?', '?'], ['?', '?', '?', '?', '?'], ['?', '?', '?', '?', '?']]
    
    for i, h in enumerate(concepts):
        # i=index, h = values of the row
        
        if target[i] == "Yes":
            for x in range(len(specific_h)):
                if h[x] != specific_h[x]:
                    specific_h[x] = '?'
                    general_h[x][x] = '?'
                    
        if target[i] == "No":
            for x in range(len(specific_h)):
                if h[x]!=specific_h[x]:
                    general_h[x][x] = specific_h[x]
                else:
                    general_h[x][x]='?'
                    
              
    indices = [i for i,val in enumerate(general_h) if val == ['?','?','?','?','?']]
    for i in indices:
        general_h.remove(['?','?','?','?','?'])
        
    return specific_h, general_h


s_final, g_final = learn(concepts, target)
print("Final S:",s_final , sep="\n")
print("Final G:",g_final , sep="\n")