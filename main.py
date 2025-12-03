import requests
import json

# a) Создаем JSON файл, заполняя данными с сайта (fetch через API)
url = 'https://jsonplaceholder.typicode.com/todos'
response = requests.get(url)
if response.status_code == 200:
    todos = response.json()
    with open('todos.json', 'w', encoding='utf-8') as f:
        json.dump(todos, f, ensure_ascii=False, indent=4)
    print("Файл 'todos.json' создан и заполнен данными.")
else:
    print("Ошибка при получении данных:", response.status_code)

# b) Читаем файл в Python-список
with open('todos.json', 'r', encoding='utf-8') as f:
    todo_list = json.load(f)
print("Список загружен, количество элементов:", len(todo_list))

# c) Записываем каждый элемент (todo) в отдельный JSON-файл
# Предполагаем, что "слов" - это опечатка, и имеется в виду каждый "todo" объект, так как titles - фразы, а не отдельные слова
for i, todo in enumerate(todo_list, start=1):
    filename = f'todo_{i}.json'
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(todo, f, ensure_ascii=False, indent=4)
print("Создано", len(todo_list), "отдельных JSON-файлов (todo_1.json, todo_2.json, ...)")
