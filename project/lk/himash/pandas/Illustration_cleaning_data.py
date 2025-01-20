import pandas as pandas

excel_values = pandas.read_csv('../resources/cars_with_issues.csv')
# no empty cells
validateEmpty = excel_values.dropna()
print(validateEmpty)

# no null cells
excel_values.dropna(inplace=True)
print(excel_values.to_string())

# Replace NULL values with the number A4:
excel_values.fillna('A4', inplace=True)
print(excel_values)

# Replace NULL values in the "brand" columns with the number A4:
excel_values["brand"].fillna('XXX', inplace=True)
print(excel_values)

# Calculate the MEAN, and replace any empty values with it
x = excel_values["cost"].mean()
excel_values["cost"].fillna(x, inplace=True)
print(excel_values)

# Calculate the MEDIAN, and replace any empty values with it
x = excel_values["cost"].median()
excel_values["cost"].fillna(x, inplace=True)
print(excel_values)

# Calculate the MODE, and replace any empty values with it
x = excel_values["cost"].mode()[0]
excel_values["cost"].fillna(x, inplace=True)
print(excel_values)

# replace wrong value
excel_values.loc[8, 'cost'] = 450
print(excel_values)

# The corr() method calculates the relationship between each column in your data set.
print(excel_values.corr())
