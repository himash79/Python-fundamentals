# File handling :
import os

file = open('../resources/log.txt', 'r')
print('Read file')
print(file.read())
print('Read file line by line')
print(file.readline(), end='')
print(file.readline(), end='')
print('Read file as a list')
print(file.readlines())

print('write file')
wfile = open('../resources/log_w.txt', 'w')
wfile.write('Hello my word ')
wfile.write('Have a great one \n')
wfile.write('Nice to meet you ')
wfile.write('Nice to meet you ')
wfile.close()

print('write file with append mode')
afile = open('../resources/log_w.txt', 'a')
afile.write('Hello ')
afile.write('my world')
afile.close()

print('Read image')
rImg = open('../resources/Capture.PNG', 'rb')
print(rImg.read())

print('Remove file')
os.remove('../resources/log_bkup.txt')

print('Rename file')
os.rename('../resources/log_w.txt', '../resources/log_w_new.txt')

print('File path exists')
print(os.path.exists('../resources/log_w_new.txt'))

print('File absolute path')
print(os.path.abspath('../resources/log_w_new.txt'))

print('Read file alternative and doesnt need close the file')
with open('../resources/log.txt', 'r') as file2:
    print(file2.read())
print('close file')
file.close()