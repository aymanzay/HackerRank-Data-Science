from datetime import datetime
from sklearn.linear_model import LogisticRegression, LinearRegression, SGDRegressor
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

# Enter your code here. Read input from STDIN. Print output to STDOUT
temp=[]
sample_input = input()
try:
    while (sample_input != ''):
        temp.append(sample_input)
        sample_input = input()
except:
    pass

inputs = temp
db_len = inputs[0]
del inputs[0]

dates = []
stockprices = []
for x in inputs:
    temp = x.split('\t')
    float_days = datetime.strptime(temp[0], '%m/%d/%Y %H:%M:%S')
    dates.append(float_days)
    try:
        stockprices.append(float(temp[1]))
    except:
        stockprices.append(np.nan)
        pass

stockdf = pd.Series(stockprices, index=dates)
stockdf.index.name = 'Date'

stockdf = stockdf.reset_index(name='Price')
missing_price_dates = stockdf[stockdf['Price'].isnull()]['Date'].values
missing_price_dates = missing_price_dates.astype('datetime64[D]').astype(int)
missing_price_dates = [[x] for x in missing_price_dates]
missing_price_dates = np.asarray(missing_price_dates)

stockdf = stockdf.dropna()
dates, prices = [[x] for x in stockdf['Date'].values], stockdf['Price'].values

X_train, X_test, y_train, y_test = train_test_split(dates, prices, test_size=0.05, shuffle=False)
X_train, y_train = np.asarray(X_train), np.asarray(y_train)

mdl = SGDRegressor(shuffle=False, max_iter=5000, learning_rate='optimal', random_state=0, n_iter_no_change=30, fit_intercept=False, epsilon=0.01)
mdl.fit(X_train, y_train)

y_pred = mdl.predict(missing_price_dates)
for pred in y_pred:
    print(pred)
