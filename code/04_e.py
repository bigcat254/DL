import pandas as pd
import numpy as np
import numpy
import torch
file_path = r'F:\机器学习\machinelearning_hw_cqut\MachineLearning_HW_CQUT\HW1 linear model\data.xlsx'
raw_data = pd.read_excel(file_path, dtype=float, header=None)
print(raw_data.shape)

data= raw_data.reshape(47,3)

data_norm =data.copy()
print(data_norm)




