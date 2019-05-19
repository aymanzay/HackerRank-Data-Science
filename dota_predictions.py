import numpy as np
from sklearn.linear_model import SGDClassifier, LogisticRegression, SGDRegressor
from sklearn import preprocessing
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split

train_X = {}
train_y = []
unique_players = []
games_played = []

# Getting training data
train_dir = 'trainingdata.txt'
f = open(train_dir, "r")
data = []
for line in f:
    if len(line) > 0:
        player_list = line.replace('\n','').split(',')
        games_played.append(player_list)
        unique_players.extend(player_list[:-1])

unique_players = list(set(unique_players))

count = 0
for x in unique_players:
    train_X[x] = count
    count = count + 1

for game in games_played:
    features = [0]*(len(unique_players))
    game_winner = int(game[-1])
    if game_winner == 1:
        train_y.append(1)
    else:
        train_y.append(-1)

    for i in range(0, len(game[:-1])):
        if i < 5:
            features[train_X[game[i]]] = 1
        else:
            features[train_X[game[i]]] = -1
    train_X.append(features)


model = LogisticRegression(C=0.1).fit(train_X,train_y)

# Getting data to predict
temp = []
sample_input = input()
try:
    while (sample_input != ''):
        temp.append(sample_input)
        sample_input = input()
except:
    pass

pred_data_raw = temp
dblen = pred_data_raw[0]
del pred_data_raw[0]

pred_data = []
for x in pred_data_raw:
    arr = x.replace('\n','').split(',')
    pred_data.append(arr)

pred_X = {}
for game in pred_data:
    features = [0] * (len(unique_players))
    for i in range(0, len(game)):
        if i < 5:
            features[pred_X[game[i]]] = 1
        else:
            features[pred_X[game[i]]] = -1
    pred_X.append(features)

results = model.predict(pred_X)
for res in results:
    print(res)


