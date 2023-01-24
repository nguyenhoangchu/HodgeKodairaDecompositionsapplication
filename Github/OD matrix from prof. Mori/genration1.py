import pandas as pd

df= pd.read_csv('Book1.csv', index_col= False)

df1 = df.groupby(df['home_mesh1km']).agg({'ex_volume': sum}).reset_index()
df2 = df.groupby(df['work_mesh1km']).agg({'ex_volume': sum}).reset_index()
three = pd.DataFrame()
i = 1
for home in df1['home_mesh1km']:
    i = i + 1
    print(i)
    a = df2['ex_volume'] - df1.loc[(df1['home_mesh1km']) == home, ['ex_volume']]['ex_volume'].values
    three[home] = pd.Series(a)
sum1 = pd.DataFrame()
sum1 = three.sum(numeric_only=True, axis=0)
potential = sum1/len(three.index)
potential.to_csv('test_result.csv', encoding='utf-8')