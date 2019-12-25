import pandas as pd

# intialise data of lists.
data = {'Name':['Tom', 'nick', 'krish', 'jack'],
        'Age':[20, 21, 19, 18]}

# Create DataFrame
df = pd.DataFrame(data)

# Print the output.
print(df)

# Add a column
df.insert(2, 'Shoe size', [10,11,12,11], False)
print(df)
# Add a row

# Create a 2nd DataFrame

# Left join

# Inner join

# Outer join
