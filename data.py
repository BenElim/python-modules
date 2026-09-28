import pandas as pd 

data = {
    "name": ["Alice", "Ali", "Getrude"],
    "Age": [23, 24, 26],
    "Countries": ["China", "USA", "Zanzibar"]
}

df = pd.DataFrame(data)
print(df)