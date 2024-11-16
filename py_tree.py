import os


class TestClass:

    def __init__(self, initial_path):
        self.initial_path = initial_path

    def check_directory(self):
        test_dict = {}
        return_list = os.listdir(self.initial_path)
        # print(content)

        for i in return_list:
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