# import neccessary library
import pandas as pd
import numpy as np

# Adding Data from file
df = pd.read_csv("2005_potential.csv", header=None)
Mij = df                                                # Set df to matrix-like table
Mji = Mij.T                                             # Tranpose Mij to Mji
# checking data
r = len(Mij)                                            # len of rows
c = len(Mij.columns)                                    # len of columns
print('This is r: \n', r)
print('This is c: \n', c)
print(Mij)
print(r)
Vi = []
if r ==c:                                               # Checking if Mij is symmetric or not 
                                                        # len of rows = columns or not
    A = Mij - Mji                                        
    print('This is A \n', A)
    print('This is A[0] \n', A[0])
else:
    print('A is not symmetric!')
for i in range(r):                                      # Calculate potential
    b = (sum(A.iloc[i])/r)                              # Sum value by row
    Vi.append(b)
table = pd.DataFrame()
code = []
a = 10
for i in range(0, 53):
    code.append(a)
    a = a + 10
table['prefecture/department code'] = code
print(table)
table['hokkaido']= Vi[0:53]
table['tohoku'] = Vi[53:106]
table['kanto'] = Vi[106:159]
table['chubu'] = Vi[159:212]
table['kansai'] = Vi[212:265]
table['chukoku'] = Vi[265:318]
table['shikoku'] = Vi[318:371]
table['kyushyu'] = Vi[371:424]
table['okinawa'] = Vi[424:477]
table = table.T
new_header = table.iloc[0]
table = table[1:]
table.columns = new_header
table.to_csv('2005_(new)area\'s potential.csv', encoding='utf-8', index= True)
print(table)