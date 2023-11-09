# User Defined Functions
# It's can reuse

print('user define function ==================')
def calculate(height, width):
    perimeter = 2 * (height + width)
    area = height + width
    print('Perimeter : ', perimeter)
    print('Area : ', area)
calculate(3, 5)

print('user define function with default args ==================')
def fetchMarks(student='Student name not found', mark=0):
    print('Student name : ', student)
    print('Mark : ', mark)
fetchMarks()

print('user define function combine params list/tuple ==================')
def fetchMarks(student, mark, *teachers):
    print('Student name : ', student)
    print('Mark : ', mark)
    print('Teacher : ', teachers) # Able to use loop
fetchMarks('Dasith', 34, 'Teacher_01','Teacher_02','Teacher_03')

print('user define function combine params dictionary ==================')
def fetchMarks(student, mark, **teachers):
    print('Student name : ', student)
    print('Mark : ', mark)
    print('Teacher : ', teachers) # Able to use loop
fetchMarks('Dasith', 34, Teacher_01=1,Teacher_02=2,Teacher_03=3)