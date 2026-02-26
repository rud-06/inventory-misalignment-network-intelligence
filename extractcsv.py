from datasets import load_dataset

dataset = load_dataset("Dingdong-Inc/FreshRetailNet-50K")

df = dataset['train'].to_pandas()

df.to_csv("freshretailnet.csv", index=False)

print(df.head())
