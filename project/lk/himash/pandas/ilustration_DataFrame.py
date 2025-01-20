import pandas as pandas

cars = {
    "brand": ['Toyota', 'Honda', 'Ferari'],
    "model": ['Prius', 'Civic', 'La-ferari']
}
# create table of data
cars_pd_res = pandas.DataFrame(cars)
print(cars_pd_res)

# refer to the row index:
print(cars_pd_res.loc[0])

#  1=1st row, 2nd = 2nd row
print(cars_pd_res.loc[[0, 1]])

cars_res = pandas.DataFrame(cars, index=['C0001', 'C0002', 'C0003'])
print(cars_res)
print(cars_res.loc['C0001'])