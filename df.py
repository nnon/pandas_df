import pandas as pd

# intialise data of lists.
data = {'Name':['Tom', 'Nick', 'Krish', 'Jack', 'Sarah', 'Jane'],
        'Age':[20, 21, 19, 18, 20, 21],
        'Gender':['M','M','M','M','F','F']}

# Create DataFrame
df = pd.DataFrame(data)

# Print the output.
print(df)

# Basic query
print(df.query('Age > 20'))
print(df.query('Name == "Tom"'))

# Add a column
df.insert(2, 'Shoe size', [10,11,12,11,5,4], False)
print(df)

height = [160, 170, 180, 190, 120, 130]
df['Height'] = height
print(df)

df1a = df.assign(weight = [200, 250, 300, 350, 120, 140])
print(df1a)


# Add a row

# Create a 2nd DataFrame

df2 = pd.DataFrame({'Name':['Tom2', 'Nick2', 'Krish2', 'Jack2'],
                    'Age':[20, 21, 19, 18],
                    'Gender':['M','M','M','M'],
                    'Shoe size':[10,11,12,11],
                    'Height':[120,130,140,150]})
print(df2)

# Left join

# Inner join

# Outer join

# Union
df3 = df.append(df2)
print(df3)

# Minus

# Index

# Group by
print(df3.groupby(['Gender']).mean())
print(df3.groupby(['Gender']).min())
print(df3.groupby(['Gender']).max())
