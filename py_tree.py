import os


class TestClass:

    def __init__(self, initial_path):
        self.initial_path = initial_path

    def defining_folders(self):
        # self.initial_path = os.path.abspath('.')
        # self.dirs_list = self.initial_path.split('\\')
        return_list = os.listdir(self.initial_path)

        return return_list

        # print(self.initial_path) #Test_prints
        # print(self.return_list)

    def check_directory(self):
        test_dict = {}
        content = self.defining_folders()
        # print(content)

        for i in content:
            if os.path.isfile(i):
                test_dict[i] = 'It is file'

            if os.path.isdir(i):
                test_dict[i] = 'It is directory'

        return test_dict

    def main(self):
        if __name__ == "__main__":
            final_result = self.check_directory()
            print(final_result)


test = TestClass(initial_path=os.path.abspath('.'))
test.main()