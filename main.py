import pandas as pd
import json

df = pd.read_csv('org.csv')

with open('data.json', 'w') as f:
    json.dump({'Data': df.to_dict(orient='records')}, f, indent=6)