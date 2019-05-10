import numpy as np
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier

temp=[]
sample_input = input()
try:
    while (sample_input != ''):
        temp.append(sample_input)
        sample_input = input()
except:
    pass

inputs = temp

input_params = inputs[0].split(' ')
num_train_ex = int(input_params[0])
num_features = int(input_params[1])

pred_params = inputs[num_train_ex+1]
X_raw = []
for i in range(1, int(input_params[0])+1):
    X_raw.append(inputs[i])

X_train = []
Y = []
labels = []
for i in range(len(X_raw)):
    temp = X_raw[i].split(' ')
    labels.append(temp[0])
    y = temp[1]
    del temp[0] #remove label
    del temp[0] #remove score
    Y.append(int(y))
    tempX = []
    for j in range(int(input_params[1])):
        feature = temp[j].split(':')[1]
        tempX.append(float(feature))
    X_train.append(tempX)
X_pred = []
pred_labels=[]

X_train = np.asarray(X_train)
Y = np.asarray(Y)

for i in range(num_train_ex+2, (int(pred_params)+num_train_ex+2)):
    temp = inputs[i].split(' ')
    pred_labels.append(temp[0])
    del temp[0] #remove label
    tempX = []
    for j in range(int(input_params[1])):
        feature = temp[j].split(':')[1]
        tempX.append(float(feature))
    X_pred.append(tempX)
    
model = RandomForestClassifier(max_depth=num_train_ex, n_estimators=30, max_features=num_features)
model.fit(X_train,Y)

preds = model.predict(X_pred)

for pred, pred_label in zip(preds, pred_labels):
    if pred >= 0:
        pred = '+1'
    else:
        pred = '-1'
    print(pred_label, pred)
