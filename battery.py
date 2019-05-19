from sklearn.svm import SVR
import numpy as np
import pandas as pd

def getData():
    # Getting training data
    train_dir = 'trainingdata.txt'
    f = open(train_dir, "r")
    data = []
    for x in f:
        a = x.replace('\n', '')
        data.append(a.split(','))
    return data

if __name__ == '__main__':
    timeCharged = float(input())
    data = getData()
    df = pd.DataFrame(data, columns=['time', 'last'])
    X = np.array([df['time'].values])
    X = np.reshape(X, (100, 1))
    y = np.array(df['last'].values)

    model = SVR(kernel='rbf', C=5000, epsilon=0.0001, tol=1e-3, gamma='scale')
    model.fit(X,y)
    lasting = model.predict([[3.76]])[0]
    print(round(lasting,2))
