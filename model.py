import pandas as pd
import numpy as np
from sklearn import linear_model
import pickle


df = pd.read_csv('c2.csv')

df

import datetime as dt
import time
from datetime import datetime
df['time'] = df['time'].apply(lambda x: datetime.timestamp(datetime.strptime(x,"%Y-%m-%d %H:%M:%S")))


df

df.dtypes

reg = linear_model.LinearRegression()
reg.fit(df[['voltage','current','energy','powerfactor','time']],df.power)

reg.coef_

reg.intercept_

df


#x=datetime.timestamp(datetime.strptime('2019-09-02 11:42:47',"%Y-%m-%d %H:%M:%S")
now = datetime.strptime('2019-09-06 8:01:30', "%Y-%m-%d %H:%M:%S")
timestamp = datetime.timestamp(now)
reg.predict([[240.4,1.02,16.45,0.92,timestamp]])


#saving model to disk
pickle.dump(reg,open('model.pkl','wb'));

# loading the model to compare the result
model=pickle.load(open('model.pkl','rb'));

print(model.predict([[240.4,1.02,16.45,0.92,timestamp]]))

