import os

def create_file(directory_path, file_count, file_extension):
    for i in range(0, file_count):
        file_name = f'qu{i+1}.{file_extension}'
        file_path = os.path.join(directory_path, file_name)

        with open(file_path, 'w'):
            pass

directory_path = input('Enter directory path: ')
file_count = int(input('Enter file count: '))
file_extension = input('Enter file extension: ')

create_file(directory_path, file_count, file_extension)
