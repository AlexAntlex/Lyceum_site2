from requests import get

# Все работы
print(get('http://localhost:5000/api/jobs').json())

# Правильный запрос к одной работе
print(get('http://localhost:5000/api/jobs/1').json())

# Несуществующий id
print(get('http://localhost:5000/api/jobs/9999999999').json())

# Строка в запросе
print(get('http://localhost:5000/api/jobs/pdf').status_code)

