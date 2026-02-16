"""def main():
    print("Hello from programmering-inom-data-platform-lab-1!")
"""

import pandas as pd 
import numpy as np 

if __name__ == "__main__":
    df = pd.read_csv("lab 1 - csv.csv", sep=';') 
   # print(df.head()) 

df["name"] = df["name"].str.replace(r"\s+", " ", regex=True) 
df["name"] = df["name"].str.strip() 
df["name"] = df["name"].str.title()   

df["price"] = df["price"].str.replace(r"\s+", " ", regex=True)

df["price"] = pd.to_numeric(df["price"], errors="coerce")
df["price"] = df["price"].mask(df["price"] <= 0, np.nan)



df["currency"] = df["currency"].str.replace(r"\s+", " ", regex=True)
df["currency"] = df["currency"].str.strip()
df["currency"] = df["currency"].str.upper()





# Flag missing values, and replace them with NaN
df["id_missing"] = df["id"].isna()
df["name_missing"] = df["name"].isna()
df["price_missing"] = df["price"].isna()
df["currency_missing"] = df["currency"].isna()
df["created_at_missing"] = df["created_at"].isna()


df["price_extreme"] = df["price"] > 15000 #flag extremely high prices

print(df)


average_price = df["price"].mean()
median_price = df["price"].median()
number_of_products = len(df)
number_of_products_with_price = df["price"].notna().sum()

print(f"Average price: {average_price}")
print(f"Median price: {median_price}")
print(f"Number of products: {number_of_products}")
print(f"Number of products with price: {number_of_products_with_price}")





# print(df.info())
# print(df.currency) 