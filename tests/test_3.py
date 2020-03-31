from requests import get, put

# Корректый запрос
print(put('http://localhost:5000/api/jobs/1',
          json={'id': 15,
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
                }).status_code)

# Проверка всех работ
print(get('http://localhost:5000/api/jobs').json())
