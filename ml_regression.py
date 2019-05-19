import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

temp=[]
sample_input = input()
try:
    while (sample_input != ''):
        temp.append(sample_input)
        sample_input = input()
except:
    pass

inputs = temp
inlen = inputs[0].split(' ')
num_features = int(inlen[0])
num_neighbors = int(inlen[1])
del inputs[0]

X = []
y = []
for i in range(0,num_neighbors):
    temp = inputs[0].split(' ')
    x = temp[0:num_features]
    b = temp[num_features]
    X.append(x)
    y.append(b)
    del inputs[0]

num_preds = inputs[0]
del inputs[0]

preds = []
for x in inputs:
    a = x.split(' ')
    preds.append(a)

ml_reg = LinearRegression()

X = np.array(X).astype(np.float64)
y = np.array(y).astype(np.float64)
preds = np.array(preds).astype(np.float64)

ml_reg.fit(X,y)

results = ml_reg.predict(preds)

for res in results:
    print(res)


