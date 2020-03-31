from requests import get, post, delete, put

# Корректные запросы
# одна работа (GET)
print(get('http://127.0.0.1:5000/api/v2/jobs/1').json())

# все работы
print(get('http://localhost:5000/api/v2/jobs').json())

# (DELETE)
print(delete('http://localhost:5000/api/v2/jobs/2').json())

# (POST)
print(post('http://localhost:5000/api/v2/jobs',
           json={'team_leader': 1,
                 'job': 'feed the parrot',
                 'work_size': 2,
                 'collaborators': '3',
                 'start_date': 'now',
                 'is_finished': False,
                 }).json())

# (PUT)
print(put('http://localhost:5000/api/v2/jobs/1',
          json={'team_leader': 1,
                'job': 'Find Scott',
                'work_size': 1,
                'collaborators': '3',
                'start_date': 'now',
                'is_finished': False
                }).json())


# Некорректные запросы
# некорректный id (GET)
print(get('http://localhost:5000/api/v2/jobs/uvu').status_code)

# некорректный id (DELETE)
print(delete('http://localhost:5000/api/v2/jobs/ere').status_code)

# несуществующий id (GET)
print(get('http://localhost:5000/api/v2/jobs/232').json())

# несуществующий id (DELETE)
print(delete('http://localhost:5000/api/v2/jobs/23456').json())

# пустой запрос (PUT)
print(put('http://localhost:5000/api/v2/jobs/1',
          json={}).json())

# несуществующий id (PUT)
print(put('http://localhost:5000/api/v2/jobs/123455',
          json={'team_leader': 1,
                'job': 'Find Scott',
                'work_size': 1,
                'collaborators': '3',
                'start_date': 'now',
                'is_finished': False
                }).json())

# некорректный id (PUT)
print(put('http://localhost:5000/api/v2/jobs/eeeeee',
          json={'team_leader': 1,
                'job': 'Find Scott',
                'work_size': 1,
                'collaborators': '3',
                'start_date': 'now',
                'is_finished': False
                }).status_code)

# отсутсвующие ключи (PUT)
print(put('http://localhost:5000/api/v2/jobs/123455',
          json={'team_leader': 1,
                'job': 'Find Scott',
                'work_size': 1,
                'collaborators': '3',
                'start_date': 'now',
                }).json())

# отсутсвующие ключи (POST)
print(post('http://localhost:5000/api/v2/jobs',
           json={'team_leader': 1,
                 'job': 'feed the parrot',
                 'collaborators': '3',
                 'start_date': 'now',
                 }).json())