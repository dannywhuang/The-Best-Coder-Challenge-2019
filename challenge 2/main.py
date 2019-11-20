from collections import defaultdict
import pandas as pd

def exportData(dataFrame,fileName):
    dataFrame.to_csv(fileName)
    print('Data exported to csv file')
    return

def readAll():
    orders = pd.read_csv('orders.csv',dtype=str)
    devices = pd.read_csv('devices.csv',dtype=str)
    credit_cards = pd.read_csv('credit_cards.csv',dtype=str)
    bank_accounts = pd.read_csv('bank_accounts.csv',dtype=str)
    print('All data read')
    return orders,devices,credit_cards,bank_accounts

def createDict():
    dict = defaultdict(list)
    for index,row in devices.iterrows():
        dict[row['userid']].append(row['device'])
        dict[row['device']].append(row['userid'])
    print('Devices added to dict')
    for index,row in credit_cards.iterrows():
        dict[row['userid']].append(row['credit_card'])
        dict[row['credit_card']].append(row['userid'])
    print('Credit Cards added to dict')
    for index, row in bank_accounts.iterrows():
        dict[row['userid']].append(row['bank_account'])
        dict[row['bank_account']].append(row['userid'])
    print('Bank Accounts added to dict')
    print('Dictionary created')
    return dict

def bfs(start,goal):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex == goal:
            return 1
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(set(dict[vertex]) - visited)
    return 0

def findSolution():
    answers = []
    for index,row in orders.iterrows():
        print(index)
        answers.append(bfs(row['buyer_userid'],row['seller_userid']))
    return answers

orders,devices,credit_cards,bank_accounts = readAll()
dict = createDict()
answers = pd.DataFrame(data=findSolution(), index=orders['orderid'], columns=['is_fraud'])
answers.index.name = 'orderid'
exportData(answers,'solutionDanny.csv')