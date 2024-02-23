import requests

user_id = 12345
url = 'https://www.kinopoisk.ru/lists/movies/top250/'
r = requests.get(url)
with open('test.html', 'w') as output_file:
    output_file.write(r.text)
