import os


class DirectoryContent:

    def __init__(self, initial_path):
        self.initial_path = initial_path

        self.return_list = os.listdir(self.initial_path)
        print(self.return_list)

    def check_directory(self):
        test_dict = {}

        for i in self.return_list:
            if os.path.isfile(i):
                test_dict[i] = 'It is file'

            elif os.path.isdir(i):
                test_dict[i] = 'It is directory'

        return test_dict

    def get_files_liest(self):
        files_list = []

        for i in self.return_list:
            if os.path.isfile(i):
                files_list.append(i)

        return files_list

    def get_dirs_list(self):
        ders_list = []

        for i in self.return_list:
            if os.path.isdir(i):
                ders_list.append(i)

        return ders_list

    def main(self):
        final_result = self.check_directory()
        print(final_result)
        print(self.get_files_liest())
        print(self.get_dirs_list())




if __name__ == "__main__":
    directory = DirectoryContent(initial_path=os.path.abspath('.'))
    directory.main()