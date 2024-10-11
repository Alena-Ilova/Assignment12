import numpy as np
import pandas as pd
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct']
income = np.array([9000, 12000, 5000, 14000, 15000, 17000, 10000, 18000, 19000, 20000])
income_without_tax = income * 0.7
expenses = np.array([3000, 6000, 8000, 9000, 4500, 10000, 14000, 15000, 12000, 19000])
data = {'Month': months,
       'Income (without tax)': income_without_tax,
       'Expenses': expenses}

df = pd.DataFrame (data)
print('Complete DataFrame:')
print(df)

first_quarter = df[df['Month'].isin(['Jan', 'Feb', 'Mar'])]
print('nData for the 1st Quarter (Jan, Feb, Mar):')
print(first_quarter)