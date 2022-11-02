import pandas as pd
import numpy as np
import numpy
import torch
file_path = r'F:\机器学习\machinelearning_hw_cqut\MachineLearning_HW_CQUT\HW1 linear model\data.xlsx'
raw_data = pd.read_excel(file_path, dtype=float, header=None)
print(raw_data.shape)


data = np.array(raw_data, dtype=int)


train_data=data.copy()
x_train = train_data[:,:2]
y_train = train_data[:, 2]

print(y_train)
