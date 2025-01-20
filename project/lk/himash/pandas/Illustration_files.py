import pandas as pandas

# read cvs
excel_values = pandas.read_csv('../resources/SampleData.csv')
print(excel_values)

# default rows
print(pandas.options.display.max_rows)

# max row count
pandas.options.display.max_rows = 99
print(excel_values)

# read json
jsonValues = pandas.read_json('../resources/cars.json')
# use to_string() to print the entire DataFrame
print(jsonValues.to_string())
#  first n rows
print(jsonValues.head(4))
#  first 5 rows
print(jsonValues.head())
#  last n rows
print(jsonValues.tail(4))
#  first 5 rows
print(jsonValues.tail())
# getting info
print(jsonValues.info())

# If your JSON code is not in a file, but in a Python Dictionary, you can load it into a DataFrame directly
carsArr = [
    {
        "id": 1,
        "brand": "Toyota",
        "model": "Corolla",
        "cost": 20000,
        "status": "Available"
    },
    {
        "id": 2,
        "brand": "Honda",
        "model": "Civic",
        "cost": 22000,
        "status": "Sold"
    }
]

carsDataFrame = pandas.DataFrame(carsArr)
print(carsDataFrame)
