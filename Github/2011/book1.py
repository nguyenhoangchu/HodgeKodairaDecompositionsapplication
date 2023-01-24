 # import necessary library
import pandas as pd
import numpy as np

# Adding Data from file
df = pd.read_csv("コード実行用.csv", header = None)
Mij = df
Mji = Mij.T
#checking data
r = len(Mij)
c = len(Mij.columns)
print('This is number of row: \n', r)
print('This is number of column: \n', c)
Vi = []
if r == c:

    A = Mij - Mji
    print('This is A \n', A)
    print('This is A[0] \n', A[0])
else:
    print('A is not symmetric!')
for i in range(r):
    b = (sum(A.iloc[i])/r)
    Vi.append(b)
table = pd.DataFrame()
code = []
a = 100
for i in range(0, 31):
    code.append(a)
    a = a + 100
table['prefecture'] = code 
print(table)
table['北海道'] = Vi[0:31]
table['青森県'] = Vi[31:62]
table['岩手県'] = Vi[62:93]
table['宮城県'] = Vi[93:124]
table['秋田県'] = Vi[124:155]
table['山形県'] = Vi[155:186]
table['福島県'] = Vi[186:217]
table['茨城県'] = Vi[217:248]
table['栃木県'] = Vi[248:279]
table['群馬県'] = Vi[279:310]
table['埼玉県'] = Vi[310:341]
table['千葉県'] = Vi[341:372]
table['東京都'] = Vi[372:403]
table['神奈川県'] = Vi[403:434]
table['新潟県'] = Vi[434:465]
table['富山県'] = Vi[465:496]
table['石川県'] = Vi[496:527]
table['福井県'] = Vi[527:558]
table['山梨県'] = Vi[558:589]
table['長野県'] = Vi[589:620]
table['岐阜県'] = Vi[620:651]
table['静岡県'] = Vi[651:682]
table['愛知県'] = Vi[682:713]
table['三重県'] = Vi[713:744]
table['滋賀県'] = Vi[744:775]
table['京都府'] = Vi[775:806]
table['大阪府'] = Vi[806:837]
table['兵庫県'] = Vi[837:868]
table['奈良県'] = Vi[868:899]
table['和歌山県'] = Vi[899:930]
table['鳥取県'] = Vi[930:961]
table['島根県'] = Vi[961:992]
table['岡山県'] = Vi[992:1023]
table['広島県'] = Vi[1023:1054]
table['山口県'] = Vi[1054:1085]
table['徳島県'] = Vi[1085:1116]
table['香川県'] = Vi[1116:1147]
table['愛媛県'] = Vi[1147:1178]
table['高知県'] = Vi[1178:1209]
table['福岡県'] = Vi[1209:1240]
table['佐賀県'] = Vi[1240:1271]
table['長崎県'] = Vi[1271:1302]
table['熊本県'] = Vi[1302:1333]
table['大分県'] = Vi[1333:1364]
table['宮崎県'] = Vi[1364:1395]
table['鹿児島県'] = Vi[1395:1426]
table['沖縄県'] = Vi[1426:1457]
table[:0]
table = table.T
new_header = table.iloc[0]
table = table[1:]
table.columns = new_header
table.to_csv("2011_(new)area's potential.csv", encoding='utf-8', index=True)
print(table)