import numpy as np
import pandas as pd

def importQuestions(fileName):
    data = pd.read_csv(fileName)
    data2 = data['name'].str.lower().str.replace(r"([^a-z\s])", " ").str.replace(r"[\s]{2,}", " ").str.strip()
    print('Questions imported')
    return data2

def importGroups(fileName):
    data = pd.read_csv(fileName)
    data['Keywords'] = data['Keywords'].str.replace(r"(,\s*)|(\s*,)", ",")
    data['Keywords'] = data['Keywords'].str.split(",")
    print('Groups imported')
    return data

def exportData(dataFrame,fileName):
    dataFrame.to_csv(fileName)
    print('Data exported to csv file')
    return

def createDictionary():
    data = importGroups('Extra Material 2 - keyword list_with substring.csv')
    dict = {}
    for index, row in data.iterrows():
        for name in row['Keywords']:
            if (name not in dict):
                dict[name] =index
    print('Dictionary created')
    return dict

def findGroups(tokens):
    wordcount = len(tokens)
    groups = []
    used = []
    for j in range(wordcount - 3, wordcount):
        possibilities = j + 1
        for k in range(possibilities):
            strcheck = " ".join(tokens[k:k + (wordcount - j)])
            if strcheck in dict and any(strcheck in y for y in used)==False:
                used.append(strcheck)
                groups.append(int(dict[strcheck]))
    return groups

def findSolution(questions):
    answers = np.zeros(questions.size,dtype=object)
    for index, row in questions.iteritems():
        print(index)
        tokens = row.split(" ")
        groups = findGroups(tokens)
        groups.sort()
        groups = list(dict.fromkeys(groups))
        answers[index] = groups
    return answers

dict = createDictionary()
questions = importQuestions('Keyword_spam_question.csv')
answers = pd.DataFrame(data=findSolution(questions), index=range(0, questions.size), columns=['groups_found'])
answers.index.name='index'
exportData(answers,'solutionDanny.csv')