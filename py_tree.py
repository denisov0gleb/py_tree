import os


def defining_folders():
    initial_path = os.path.abspath('.')
    dirs_list = initial_path.split('\\')
    return_list = os.listdir(initial_path)

    return return_list
    # print(dirs_list) #Test_prints
    # print(initial_path)
    # print(return_list)


def check_directory():
    test_dict = {}
    content = defining_folders()
    # print(content)

    for i in content:
        if os.path.isfile(i):
            test_dict[i] = 'It is file'

        if os.path.isdir(i):
            test_dict[i] = 'It is directory'

    return test_dict


if __name__ == "__main__":
    final_result = check_directory()
    print(final_result)
