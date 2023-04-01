import pandas as pd

def conversion():
    a=pd.read_json("student.json")
    df = a
    df.to_csv(r'data.csv', index=False)
    # print(df)

conversion()