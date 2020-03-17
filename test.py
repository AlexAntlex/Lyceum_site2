from requests import get, post, delete


from requests import get

# Все работы
print(get('http://localhost:5000/api/jobs').json())

# Правильный запрос к одной работе
print(get('http://localhost:5000/api/jobs/1').json())

# Несуществующий id
print(get('http://localhost:5000/api/jobs/9999999999').json())

# Строка в запросе
print(get('http://localhost:5000/api/jobs/pdf').json())

# В базе уже есть такая работа (с таким же id)
print(post('http://localhost:5000/api/jobs',
           json={'id': 1,
                 'team_leader': 1,
                 'job': 'Fly',
                 'work_size': 15,
                 'collaborators': '1, 2',
                 'start_date': 'now',
                 'is_finished': True
                 }).json())

# Нет одного из ключей
print(post('http://localhost:5000/api/jobs',
           json={'id': 13,
                 'team_leader': 1,
                 'job': 'Fly',
                 'work_size': 15,
                 'collaborators': '1, 2',
                 'start_date': 'now',
                 }).json())

# Пустой запрос
print(post('http://localhost:5000/api/jobs',
           json={
                 }).json())

# Корректный запрос
print(post('http://localhost:5000/api/jobs',
           json={'id': 11,
                 'team_leader': 5,
                 'job': 'make a sandwich',
                 'work_size': 1,
                 'collaborators': '',
                 'start_date': 'now',
                 'is_finished': False
                 }).json())

# Корректый запрос
print(delete('http://localhost:5000/api/jobs/10').json())

# Некорректый запрос
print(delete('http://localhost:5000/api/jobs/').json())

# Корректый запрос
print(put('http://localhost:5000/api/jobs/11',
          json={'id': 12,
                'team_leader': 1,
                'job': 'Find Scott',
                'work_size': 1,
                'collaborators': '3',
                'start_date': 'now',
                'is_finished': False
                }).json())

# Некорректый запрос (несуществующий id)
print(put('http://localhost:5000/api/jobs/1234',
          json={'id': 11,
                'team_leader': 1,
                'job': 'Find Scott',
                'work_size': 1,
                'collaborators': '3',
                'start_date': 'now',
                'is_finished': False
                }).json())

# Некорректый запрос (некорректный id)
print(put('http://localhost:5000/api/jobs/quq',
          json={'id': 11,
                'team_leader': 1,
                'job': 'Find Scott',
                'work_size': 1,
                'collaborators': '3',
                'start_date': 'now',
                'is_finished': False
                }).json())

# Корректный запрос (одни пользователь)
print(get('http://127.0.0.1:5000/api/v2/users/1').json())

# Некорректный запрос (несуществующий id)
print(get('http://localhost:5000/api/v2/users/232').json())

# Корректный запрос (все пользователи)
print(get('http://localhost:5000/api/v2/users').json())

# Корректный запрос
print(post('http://localhost:5000/api/v2/users',
           json={'email': 'scott_chief@mars.org',
                 'name': 'Ridley',
                 'surname': 'Scott',
                 'age': 21,
                 'speciality': 'research engineer',
                 'address': 'module_1',
                 'position': 'captain'}).json())

# Корректный запрос (одни пользователь)
print(delete('http://localhost:5000/api/v2/users/4').json())

# Некорректный запрос (несуществующий id)
print(delete('http://localhost:5000/api/v2/users/23456').json())
