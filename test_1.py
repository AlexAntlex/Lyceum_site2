from requests import get, post, delete

# Корректный запрос (одна работа)
print(get('http://127.0.0.1:5000/api/v2/jobs/1').json())

# Некорректный запрос (несуществующий id)
print(get('http://localhost:5000/api/v2/jobs/232').json())

# Корректный запрос (все работы)
print(get('http://localhost:5000/api/v2/jobs').json())

# Корректный запрос
print(post('http://localhost:5000/api/v2/jobs',
           json={'team_leader': 1,
                 'job': 'feed the parrot',
                 'work_size': 2,
                 'collaborators': '3',
                 'start_date': 'now',
                 'is_finished': False,
                 }).json())

# Корректный запрос (один запрос)
print(delete('http://localhost:5000/api/v2/jobs/4').json())

# Некорректный запрос (несуществующий id)
print(delete('http://localhost:5000/api/v2/jobs/23456').json())
