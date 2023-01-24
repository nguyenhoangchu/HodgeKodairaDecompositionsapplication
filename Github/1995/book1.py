# import neccessary library
import numpy as np
import pandas as pd

# Adding Data from file
df = pd.read_csv("1995/1995_potential.csv", header=None)
Mij = df                                                # Set df to matrix-like table
Mji = Mij.T                                             # Tranpose Mij to Mji
#checking data
r = len(Mij)                                            # len of rows
c = len(Mij.columns)                                    # len of columns
print('This is r: \n', r)
print('This is c: \n', c)
print(Mij)
Vi = []
if r ==c:
                                                        # Checking if Mij is symmetric or not
    A = Mij - Mji                                       # len of rows = columns or not
    print('This is A \n', A)
    print('This is A[0] \n', A[0])
else:
    print('A is not symmetric!')
for i in range(r):                                      # Calculating pontential
    b = -sum(A.iloc[i])/r                               # Sum value by row, this value is refer to be s_{i}                              
    Vi.append(-b)                                       # For QGIS and according to Paper s_{i}=-Vi so we're going to demonstrate everything
                                                        #by V_{i} not s_{i}
table = pd.DataFrame()
code = []
a = 10
for i in range(0, 46):
    code.append(a)
    a = a + 10
table['prefecture/department code'] = code
print(table)
table['hokkaido']= Vi[0:46]
table['tohoku'] = Vi[46:92]
table['kanto'] = Vi[92:138]
table['chubu'] = Vi[138:184]
table['kansai'] = Vi[184:230]
table['chukoku'] = Vi[230:276]
table['shikoku'] = Vi[276:322]
table['kyushyu'] = Vi[322:368]
table['okinawa'] = Vi[368:414]
table = table.T
new_header = table.iloc[0]
table = table[1:]
table.columns = new_header
table.to_csv('11995_(new)area\'s potential.csv', encoding='utf-8', index=True)
print(table) 