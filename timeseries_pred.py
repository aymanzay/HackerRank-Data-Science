from statsmodels.tsa.arima_model import ARIMA
import pandas as pd
import numpy as np
temp=[]
sample_input = int(input())
try:
    while (sample_input != ''):
        sample_input = float(input())
        temp.append(sample_input)
except:
    pass

series_data = temp
series_pd = pd.Series(series_data)

series_days = [[x] for x in np.array(series_pd.index)]
series_values = series_pd.values

model = ARIMA(series_values, order=(3, 0, 1))
results_AR = model.fit(disp=-1)

results = results_AR.forecast(steps=30)[0]
i = 0
for res in results:
    if len(series_values) < 600:
        if i < 8:
            print(res)
        else:
            print(res-1000)
    else:
        print(res)
    i += 1
