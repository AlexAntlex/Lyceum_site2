from requests import get, post


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
                 'collaborators': '-',
                 'start_date': 'now',
                 'is_finished': False
                 }).json())

# Проверка всех работ
print(get('http://localhost:5000/api/jobs').json())