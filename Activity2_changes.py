# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 21:04:10 2024


"""

#C:\Users\Sweta Srivastava\dlops_activity

# Import necessary library
import pandas as pd


df = pd.read_csv('C:\Users\User\dlops\dlops_activity\roll_m22aie204')  

# Now, let's identify and list the missing values for your DataFrame 'df'
missing_values = df.isnull().sum()

# Printing missing values for each column in the DataFrame
print("Missing values in each column for roll number M21AIE244:")
print(missing_values)

# Optionally, save these results to a text file for documentation or further analysis
with open('missing_values_report_M21AIE244.txt', 'w') as f:
    f.write(f"Missing values report for roll number M21AIE244:\n{missing_values.to_string()}")
