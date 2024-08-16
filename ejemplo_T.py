import pandas as pd
data = {"Jugador": ["Chan", "Alan", "Omar"],
        "Puntos": [20, 15,10],
        "Rebotes": [5,3,2]}
df = pd.DataFrame(data)
print(df)
df_trans = df.T
print(df_trans)