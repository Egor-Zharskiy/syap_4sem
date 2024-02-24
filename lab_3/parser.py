import re
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from collections import Counter
import string


def plot_char_frequency(html_response, target_word):
    # response = requests.get(url)

    if html_response.status_code == 200:

        soup = BeautifulSoup(html_response.text, 'html.parser')

        text = soup.get_text()
        translator = str.maketrans('', '', string.punctuation)
        text = text.translate(translator).lower()

        char_counter = Counter(text)

        labels, values = zip(*char_counter.items())

        sorted_indices = sorted(range(len(labels)), key=lambda k: labels[k])
        labels = [labels[i] for i in sorted_indices]
        values = [values[i] for i in sorted_indices]

        plt.bar(labels, values)
        plt.xlabel('Буквы')
        plt.ylabel('Частота встречаемости')
        plt.title(f'Гистограмма частоты встречаемости букв в слове "{target_word}" на странице')
        plt.show()

    else:
        print(f"Ошибка при запросе: {html_response.status_code}")


def plot_word_length_histogram(html_response):
    if html_response.status_code == 200:
        soup = BeautifulSoup(html_response.text, 'html.parser')

        text = soup.get_text()
        words = text.split()
        word_lengths = [len(word) for word in words]

        plt.hist(word_lengths, bins=range(1, max(word_lengths) + 2), edgecolor='black')
        plt.xlabel('Длина слова')
        plt.ylabel('Частота встречаемости')
        plt.title('Гистограмма встречаемости длин слов на странице')
        plt.xticks(range(1, 26))
        plt.xlim(1, 26)
        plt.show()

    else:
        print(f"Ошибка при запросе: {html_response.status_code}")


def get_response(page_url):
    html_response = requests.get(page_url)
    return html_response


def find_all_links(page_url):
    soup = BeautifulSoup(get_response(page_url).text, 'html.parser')
    links = []
    for a_tag in soup.find_all("a"):
        links.append(a_tag)

    return len(links)


def find_words(html_response):
    soup = BeautifulSoup(html_response.text, 'html.parser')
    text = soup.get_text()
    words = [word.lower() for word in re.findall(r'\b\w+\b', text)]
    return words


def count_word(html_response, word):
    words = find_words(html_response)
    print(words)
    count = words.count(word)
    for el in words:
        if word in el:
            count += 1
    return count


url = input('Введите url-адрес анализируемой страницы: ')
response = get_response(url)
print(f'Количество всех ссылок на странице: {find_all_links(url)}')
find_words(response)

symbol = input('введите символ или слово для проверки частоты его встречаемости: ')
print(f'Число встречи "{symbol}": ', count_word(response, symbol))
plot_char_frequency(response, symbol)

plot_word_length_histogram(response)
# https://baskino.org/
