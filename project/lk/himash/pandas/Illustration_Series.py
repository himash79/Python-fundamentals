import pandas as pandas

# Series is like a column in a table, one-dimensional array holding data of any type
cars_models = ['Prius', 'Civic', 'La-ferari']
cars_pd_res2 = pandas.Series(cars_models)
print(cars_pd_res2)

# Able to pick one
print(cars_pd_res2[0])

# create custom index for table
cars_models_with_cus_index = pandas.Series(cars_models, index=[1, 2, 3])
print(cars_models_with_cus_index)
print(cars_models_with_cus_index[2])

# read dictionary
cars_dictionary = {'Toyota': 'Prius', 'Honda': 'Civic', 'Ferari': 'La-ferari'}
cars_dictionary_res = pandas.Series(cars_dictionary)
print(cars_dictionary_res)

# read dictionary with customer fields
cars_dictionary_custom_res = pandas.Series(cars_dictionary, index=['Toyota', 'Ferari'])
print(cars_dictionary_custom_res)