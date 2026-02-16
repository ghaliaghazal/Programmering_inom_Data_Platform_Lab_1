def main():
    print("Hello from programmering-inom-data-platform-lab-1!")


if __name__ == "__main__":
    main()


import pandas as pd 

df = pd.read_csv("lap 1 - csv.csv")
print(df.head())