import pandas as pd

sol1 = pd.read_csv('solutionDanny.csv')
sol2 = pd.read_csv('solutionJason.csv')
lst = []
for index,row in sol1.iterrows():
    lst = []
    if row['is_fraud'] != sol2.loc[index,'is_fraud']:
        lst.append(index)
        print("%d is a mistake" % (index))

print(lst)