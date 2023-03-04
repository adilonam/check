import math
import pandas_datareader as web
import numpy as np
import pandas as pd
# from tensorflow import keras
# from keras.models import  Sequential
# from keras.layers import Dense,LSTM
from matplotlib import pyplot as plt
from datetime import datetime
plt.style.use('fivethirtyeight')

 

class Machine():
    a_min = 0
    a_max = 0
    def __init__(self) -> None:
        pass
    def scale(self, data: np.array):
        self.a_max = np.amax(data, axis=0)
        self.a_min = np.amin(data, axis=0)
        sc_data = (data-self.a_min)/(self.a_max-self.a_min)
        return sc_data
    
    def inverse(self, data):
        in_value = data*(self.a_max-self.a_min)+self.a_min
        return in_value
    
    def get_data(self):
        df = web.get_data_yahoo(['SPY'],start='2022-10-23',end='2022-12-24')
        return df