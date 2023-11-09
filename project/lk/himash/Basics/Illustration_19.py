# Positional Arguments :
# method arguments must have order which means when method call somewhere else arguments
# must have same order as method declaration.
# keyword Arguments :
# when method calling provides parameter name same as method declaration parameter name and related values.
# Then arguments can access related arguments if there change position.
# Default Arguments :
# When declaring  the function provide method arguments values as default values.
# method declaration 1st argument doesn't must be default argument.
# Variable Length Arguments :
# when method declaration reach uncounted arguments (list/tuple/dictionary) then need to provide these type of
# arguments.

print('Positional Arguments ============================= ')
def fetchDetails(id, name):
    print(f'The user ID is {id} and username is {name}')
fetchDetails(1, 'Dasith')

print('Keyword Arguments ============================= ')
def fetchDetails(id, name):
    print(f'The user ID is {id} and username is {name}')
fetchDetails(name='Dasith', id=1)

print('Default Arguments ============================= ')
def fetchDetails(id, name='Not found'):
    print(f'The user ID is {id} and username is {name}')
fetchDetails(1)

print('Variable length Arguments (tuple/list) ============================= ')
def fetchDetails(*marks):
    total = 0
    for mark in marks:
        total += mark
    print(f'Total marks {total}')
fetchDetails(10,20,30,40,50)

print('Variable length Arguments (dictionary) ============================= ')
def fetchDetails(**marks):
    total = 0
    for name,mark in marks.items():
        print(f'{name} granted {mark} marks')
        total += mark
    print(f'Total student marks {total}')
fetchDetails(Dasith=10,Ushan=20,Kavi=30,Damith=40,Thimi=50)