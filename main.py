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








print(df["name"])  

