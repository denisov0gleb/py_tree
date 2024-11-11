import os

path = 'C:\\Users\\efimf\\py_files\\school_assignments'
list_of_paths = path.split('\\')

path_string = ''
for index, i in enumerate(list_of_paths):
    if index == 0:
        path_string += i
    else:
        path_string += '\\' + i

        print(*os.listdir(path_string), end='\n\n')
print(list_of_paths)

