import re
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from collections import Counter
import string


def plot_char_frequency(url, target_word):
    # Отправляем GET-запрос к указанному URL
    response = requests.get(url)

    # Проверяем успешность запроса
    if response.status_code == 200:
        # Используем BeautifulSoup для парсинга HTML-кода страницы
        soup = BeautifulSoup(response.text, 'html.parser')

        # Извлекаем текст из HTML-кода
        text = soup.get_text()

        # Удаляем знаки препинания и лишние пробелы
        translator = str.maketrans('', '', string.punctuation)
        text = text.translate(translator).lower()

        # Считаем частоту каждой буквы в тексте
        char_counter = Counter(text)

        # Извлекаем данные для построения гистограммы
        labels, values = zip(*char_counter.items())

        # Сортируем данные
        sorted_indices = sorted(range(len(labels)), key=lambda k: labels[k])
        labels = [labels[i] for i in sorted_indices]
        values = [values[i] for i in sorted_indices]

        # Построение гистограммы
        plt.bar(labels, values)
        plt.xlabel('Буквы')
        plt.ylabel('Частота встречаемости')
        plt.title(f'Гистограмма частоты встречаемости букв в слове "{target_word}" на странице')
        plt.show()

    else:
        print(f"Ошибка при запросе: {response.status_code}")


def plot_word_length_histogram(url):
    # Отправляем GET-запрос к указанному URL
    response = requests.get(url)

    # Проверяем успешность запроса
    if response.status_code == 200:
        # Используем BeautifulSoup для парсинга HTML-кода страницы
        soup = BeautifulSoup(response.text, 'html.parser')

        # Извлекаем текст из HTML-кода
        text = soup.get_text()

        # Разбиваем текст на слова
        words = text.split()

        # Считаем длину каждого слова
        word_lengths = [len(word) for word in words]

        # Построение гистограммы
        plt.hist(word_lengths, bins=range(1, max(word_lengths) + 2), edgecolor='black')
        plt.xlabel('Длина слова')
        plt.ylabel('Частота встречаемости')
        plt.title('Гистограмма встречаемости длин слов на странице')
        plt.xticks(range(1, 26))
        plt.xlim(1, 26)
        plt.show()

    else:
        print(f"Ошибка при запросе: {response.status_code}")


def get_html(url):
    response = requests.get(url)
    # print(response.text)
    return response.text


def find_all_links(url):
    soup = BeautifulSoup(get_html(url), 'html.parser')
    links = []
    for a_tag in soup.find_all("a"):
        links.append(a_tag)

    # print(links)
    print(len(links))
    # links = soup.find_all('href')
    # print(links, 'links')


def find_words(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    text = soup.get_text()
    words = [word.lower() for word in re.findall(r'\b\w+\b', text)]
    return words


def count_word(url, word):
    words = find_words(url)
    print(words)
    count = words.count(word)
    for el in words:
        if word in el:
            count += 1
    return count


url = input('Введите url-адрес анализируемой страницы: ')

find_all_links(url)
find_words(url)

symbol = input('введите символ или слово для проверки частоты его встречаемости: ')
print(f'Число встречи "{symbol}": ', count_word(url, symbol))
plot_char_frequency(url, symbol)

plot_word_length_histogram(url)
# https://baskino.org/
