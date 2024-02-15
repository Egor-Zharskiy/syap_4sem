import pickle
import sys


def find_even_elements(array):
    even_elements = []
    for row in array:
        for el in row:
            if el % 2 == 0:
                even_elements.append(el)
    return even_elements


try:
    i, j = map(int, input('введите размеры двумерного массива: ').split())
except ValueError:
    print('Введите числовые данные в надлежащем фомате')
    sys.exit()

print(f"Размеры Массива: {i}, {j}")
array = []
for a in range(i):
    row = []
    for b in range(j):
        try:
            el = int(input('введите число: '))
            row.append(el)
        except ValueError:
            print('неверный формат ввода')
            sys.exit()
    array.append(row)

print(array)

with open('data.bin', 'wb') as file:
    pickle.dump(array, file)

with open('data.bin', 'rb') as file:
    new_arr = pickle.load(file)

res = find_even_elements(new_arr)

with open('result.txt', 'w') as text_file:
    for element in res:
        text_file.write(f'{element}\n')
