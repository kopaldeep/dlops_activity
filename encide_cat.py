import pandas as pd

df = pd.read_excel("/Users/ishnoorsingh/Code/sem3/dlops/dlops_2_forked/dlops_activity/DryBeanDataset/Dry_Bean_Dataset.xlsx")

print(df.head())
df_encoded = pd.get_dummies(df, columns=['Class'])

# Save the modified dataset
output_path = '/Users/ishnoorsingh/Code/sem3/dlops/dlops_2_forked/dlops_activity/DryBeanDataset/Dry_Bean_Dataset_encoded.xlsx'
df_encoded.to_excel(output_path, index=False)

print("Encoded dataset saved to:", output_path)