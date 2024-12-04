import os


class DirectoryContent:

    def __init__(self, initial_path=os.path.abspath('.')):
        self.initial_path = initial_path

    def get_files_list(self):
        file_list = []
        for i in os.listdir(self.initial_path):
            full_path = os.path.join(self.initial_path, i)
            if os.path.isfile(full_path):
                file_list.append(i)

        return file_list

    def get_dirs_list(self):
        directory_list = []
        for i in os.listdir(self.initial_path):
            full_path = os.path.join(self.initial_path, i)
            if os.path.isdir(full_path):
                directory_list.append(i)

        return directory_list

    def main(self):
        result_files = self.get_files_list()
        result_directory = self.get_dirs_list()

        print(f'your path: {self.initial_path}\n'
              f'all files in this path: {result_files} \n'
              f'all directory in this path: {result_directory}')

        print(os.listdir(self.initial_path))


if __name__ == "__main__":
    directory = DirectoryContent(initial_path=os.path.abspath('C:\\Users\\efimf\\py_files'))
    directory.main()
