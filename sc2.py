import pandas as pd
import numpy as np

df = pd.read_csv("https://github.com/chris1610/pbpython/blob/master/data/sales_data_types.csv?raw=True")

df["Customer Number"] = df['Customer Number'].astype('int')


def convert_currency(val):
    """
    125000.00
    Convert the string number value to a float
     - Remove $
     - Remove commas
     - Convert to float type
    """
    new_val = val.replace(',','').replace('$', '')
    return float(new_val)


def convert_percent(val):
    """
    Convert the percentage string to an actual floating point percent
    """
    new_val = val.replace('%', '')
    return float(new_val) / 100


df['2016'] = df['2016'].apply(convert_currency)
df['2017'] = df['2017'].apply(convert_currency)

df['Percent Growth'] = df['Percent Growth'].apply(lambda x: x.replace('%', '')).astype('float') / 100
pd.to_numeric(df['Jan Units'], errors='coerce').fillna(0)
df["Start_Date"] = pd.to_datetime(df[['Month', 'Day', 'Year']])
df["Active"] = np.where(df["Active"] == "Y", True, False)

print(df)
