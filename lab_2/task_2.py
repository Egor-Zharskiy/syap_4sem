import pandas as pd


def if_function(value_column):
    return value_column.apply(lambda x: 'Positive' if x > 0 else 'Negative')


data = {'value': [10, -5, 20, -15]}
df = pd.DataFrame(data)
print(type(df['value']))
df['Result'] = if_function(df['value'])

print(df)
