# Класс Файл. Имя файла, размер, дата создания, количество
# обращений. Создать список объектов. Вывести: список файлов, упорядоченных
# по алфавиту, список файлов, размер которых превышает заданный, список
# файлов, число обращений к которым превышает заданное

import PySimpleGUI as sg


class File:
    def __init__(self, file_name, size, creation_date, access_count):
        self.file_name = file_name
        self.size = size
        self.creation_date = creation_date
        self.access_count = access_count

    def __str__(self):
        return f"File: {self.file_name}, Size: {self.size} KB, " \
               f"Creation Date: {self.creation_date}, Access Count: {self.access_count}"

    @staticmethod
    def create_file_list():
        files = [
            File("document.txt", 100, "2022-01-01", 10),
            File("image.jpg", 500, "2022-02-15", 5),
            File("presentation.ppt", 200, "2022-03-20", 15),
            File("data.xlsx", 300, "2022-04-10", 8),
            File("video.mp4", 800, "2022-05-25", 12),
        ]
        return files

    @staticmethod
    def print_sorted_by_name(files):
        sorted_files = sorted(files, key=lambda x: x.file_name)
        print("Files sorted by name:")
        for file in sorted_files:
            print(file)

    @staticmethod
    def print_large_files(files, threshold_size):
        large_files = [file for file in files if file.size > threshold_size]
        print(f"Files larger than {threshold_size} KB:")
        for file in large_files:
            print(file)

    @staticmethod
    def print_high_access_count_files(files, threshold_access_count):
        high_access_count_files = [file for file in files if file.access_count > threshold_access_count]
        print(f"Files with access count exceeding {threshold_access_count}:")
        for file in high_access_count_files:
            print(file)


def create_layout():
    layout = [
        [sg.Text("Welcome to the File Viewer!")],
        [sg.Button("List Files", key="-LIST-")],
        [sg.Button("Large Files", key="-LARGE-")],
        [sg.Button("High Access Count Files", key="-ACCESS-")],
        [sg.Button('Sort Files', key='-SORT-')],
        [sg.Output(size=(700, 200), key="-OUTPUT-", font=("Arial", 12))]
    ]
    return layout


if __name__ == "__main__":
    window = sg.Window("File Viewer", create_layout(), size=(800, 600))
    files_list = File.create_file_list()
    while True:
        print('_________________________')
        event, values = window.read()

        if event == sg.WINDOW_CLOSED:
            break
        elif event == "-LIST-":

            for file in files_list:
                print(file)
        elif event == '-SORT-':
            File.print_sorted_by_name(files_list)

        elif event == '-LARGE-':
            File.print_large_files(files_list, 100)

        elif event == '-ACCESS-':
            File.print_high_access_count_files(files_list, 5)

