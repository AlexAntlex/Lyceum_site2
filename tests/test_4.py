from requests import get, post, delete, put

# Корректные запросы
# одни пользователь (GET)
print(get('http://127.0.0.1:5000/api/v2/users/1').json())

# все пользователи (GET)
print(get('http://localhost:5000/api/v2/users').json())

# (DELETE)
print(delete('http://localhost:5000/api/v2/users/4').json())

# (POST)
print(post('http://localhost:5000/api/v2/users',
           json={'email': 'scott_chief@mars.org',
                 'name': 'Ridley',
                 'surname': 'Scott',
                 'age': 21,
                 'speciality': 'research engineer',
                 'address': 'module_1',
                 'position': 'captain'}).json())

# (PUT)
print(put('http://localhost:5000/api/v2/users/4',
          json={'email': 'scott_chief@mars.org',
                'name': 'Ridley',
                'surname': 'Scott',
                'age': 21,
                'speciality': 'research engineer',
                'address': 'module_1',
                'position': 'captain'}).json())


# Некорректные запросы
# несуществующий id (GET)
print(get('http://localhost:5000/api/v2/users/232').json())

# несуществующий id (DELETE)
print(delete('http://localhost:5000/api/v2/users/23456').json())

# несуществующий id (PUT)
print(put('http://localhost:5000/api/v2/users/1532545',
          json={'email': 'scott_chief@mars.org',
                'name': 'Ridley',
                'surname': 'Scott',
                'age': 21,
                'speciality': 'research engineer',
                'address': 'module_1',
                'position': 'captain'}).json())

# некорректный id (GET)
print(get('http://localhost:5000/api/v2/users/uwu').status_code)

# некорректный id (DELETE)
print(delete('http://localhost:5000/api/v2/users/er').status_code)

# некорректный id (PUT)
print(put('http://localhost:5000/api/v2/users/aaaa',
          json={'email': 'scott_chief@mars.org',
                'name': 'Ridley',
                'surname': 'Scott',
                'age': 21,
                'speciality': 'research engineer',
                'address': 'module_1',
                'position': 'captain'}).status_code)

# некорректный id (POST)
print(post('http://localhost:5000/api/v2/users/qwe',
           json={'email': 'scott_chief@mars.org',
                 'name': 'Ridley',
                 'surname': 'Scott',
                 'age': 21,
                 'speciality': 'research engineer',
                 'address': 'module_1',
                 'position': 'captain'}).status_code)

# пустой запрос (POST)
print(post('http://localhost:5000/api/v2/users',
           json={}).json())

# пустой запрос (PUT)
print(put('http://localhost:5000/api/v2/users/1',
          json={}).json())

# отсутсвующие ключи (PUT)
print(put('http://localhost:5000/api/v2/users/1',
          json={'email': 'scott_chief@mars.org',
                'name': 'Ridley',
                'age': 21,
                'speciality': 'research engineer',
                'position': 'captain'}).json())

# отсутсвующие ключи (POST)
print(post('http://localhost:5000/api/v2/users',
           json={'email': 'scott_chief@mars.org',
                 'surname': 'Scott',
                 'age': 21,
                 'address': 'module_1',
                 'position': 'captain'}).json())