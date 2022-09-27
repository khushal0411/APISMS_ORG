import pandas as pd
import json

df = pd.read_csv('user.csv')

with open('data_user.json', 'w') as f:
    json.dump({'Data': df.to_dict(orient='records')}, f, indent=6)