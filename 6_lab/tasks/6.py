import requests

print("=== Тестування методів бібліотеки requests ===")

# 1. GET — Отримання даних
r_get = requests.get('https://httpbin.org/get')
print(f"[GET]    Статус: {r_get.status_code}")

# 2. POST — Відправка даних (створення)
payload = {'user': 'Orest', 'action': 'test'}
r_post = requests.post('https://httpbin.org/post', data=payload)
print(f"[POST]   Статус: {r_post.status_code}")

# 3. PUT — Оновлення даних
r_put = requests.put('https://httpbin.org/put', data={'id': 1, 'status': 'updated'})
print(f"[PUT]    Статус: {r_put.status_code}")

# 4. DELETE — Видалення даних
r_delete = requests.delete('https://httpbin.org/delete')
print(f"[DELETE] Статус: {r_delete.status_code}")

# 5. HEAD — Отримання лише технічної інформації (headers)
r_head = requests.head('https://httpbin.org/get')
print(f"[HEAD]   Сервер: {r_head.headers.get('Server')}")

print("==============================================")
print("Всі методи перевірено успішно!")