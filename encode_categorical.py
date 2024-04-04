# Example content for encode_categorical.py
import pandas as pd

# Sample data
data = {'Category': ['A', 'B', 'C', 'A', 'B', 'C']}
df = pd.DataFrame(data)

# Encoding categorical values
encoded_df = pd.get_dummies(df, columns=['Category'])

print("Original DataFrame:")
print(df)
print("\nEncoded DataFrame:")
print(encoded_df)

