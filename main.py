"""def main():
    print("Hello from programmering-inom-data-platform-lab-1!")
"""

import pandas as pd 
import numpy as np 

if __name__ == "__main__":
    df = pd.read_csv("lab 1 - csv.csv", sep=';') 
    print(df.head()) 


#df["id"].str.split(",")
#print(df)  

# print(df.values) 
df["name"] = df["name"].str.replace(r"\s+", " ", regex=True) 
df["name"] = df["name"].str.strip() 
df["name"] = df["name"].str.title()   

df["price"] = df["price"].str.replace(r"\s+", " ", regex=True)






# Flag missing values, and replace them with NaN
df["id_missing"] = df["id"].isna()
df["name_missing"] = df["name"].isna()
df["price_missing"] = df["price"].isna()
df["currency_missing"] = df["currency"].isna()
df["created_at_missing"] = df["created_at"].isna()

print(df)


