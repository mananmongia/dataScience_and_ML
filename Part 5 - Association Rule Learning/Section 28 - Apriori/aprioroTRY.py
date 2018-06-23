# Apriori

#I  mporting The Libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
 
# IData Preprocessing
dataset = pd.read_csv('Market_Basket_Optimisation.csv', header = None)
transactions = []
for i in range(0,7501):
    transactions.append([str(dataset.values[i,j]) for j in range(0,20)])
    
# Training Apriori on data given
from apyori import apriori
rules = apriori(transactions, min_support = 0.0028, min_confidence = 0.2, min_lift = 3, min_length = 2)

#  Results
result = list(rules)