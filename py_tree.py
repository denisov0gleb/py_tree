import os


initial_path = os.path.abspath('.')
dirs_list= initial_path.split('\\')

path_string = ''
for index, dir_name in enumerate(dirs_list):
    if index == 0:
        path_string += dir_name
    else:
        path_string += '\\' + dir_name

        print(*os.listdir(path_string), end='\n\n')
print(dirs_list)
