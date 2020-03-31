from requests import get, delete

# Корректый запрос
print(delete('http://localhost:5000/api/jobs/1').json())

# Некорректый запрос (несуществующий id)
print(delete('http://localhost:5000/api/jobs/111111111111').json())

# Некорректый запрос (некорректный id)
print(delete('http://localhost:5000/api/jobs/ау').status_code)

# Некорректый запрос (отсутствие id)
print(delete('http://localhost:5000/api/jobs/').status_code)

# Проверка всех работ
print(get('http://localhost:5000/api/jobs').json())