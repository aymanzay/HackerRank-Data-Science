import pandas as pd
import numpy as np
import ast
from sklearn.linear_model import SGDClassifier

# Getting training data
train_dir = 'trainingdata.txt'
f = open(train_dir, "r")
data = []
for x in f:
    data.append(x.replace('\n',''))

datalen = data[0]
del data[0]
dicts = []
for x in data:
    dicts.append(ast.literal_eval(x))

# Converting array of dicts to pd dataframe
train_df = pd.DataFrame(dicts)
# Remove non-essential features
trainX_raw = np.array(train_df.drop(columns=['Mathematics', 'serial']).values)

trainX = []
trainy = np.array(train_df['Mathematics'].values)

for x in trainX_raw:
    # keep nan values to reinforce pattern recognition; greatly increasing accuracy
    #newX = x[~np.isnan(x)]
    newX = np.nan_to_num(x)
    trainX.append(newX)

trainX = np.asarray(trainX)

# Getting data to predict
temp=[]
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

# Converting string data to dict values
pred_dicts = []
for x in pred_data_raw:
    pred_dicts.append(ast.literal_eval(x))

# Converting array of dicts to pd dataframe
pred_df = pd.DataFrame(pred_dicts)

# Converting df to classifiable np arrays
pred_Xraw = np.array(pred_df.drop(columns=['serial']).values)
pred_X = []
for x in pred_Xraw:
    #newX = x[~np.isnan(x)]
    newX = np.nan_to_num(x)
    pred_X.append(newX)

pred_X = np.asarray(pred_X)

# Declare model and fit
clf = SGDClassifier()
clf.fit(trainX, trainy)

results = clf.predict(pred_X)
for res in results:
    print(res)
