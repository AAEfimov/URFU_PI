

### Реализованы следующие типы запросов:
#### Получение главной страницы
```
curl -X 'GET' \
  'http://127.0.0.1:8000/' \
  -H 'accept: application/json'
```
#### Возвращает приветственное сообщение
```
curl -X 'GET' \
  'http://127.0.0.1:8000/api' \
  -H 'accept: application/json'
```
#### Получить ранее сгенерированную картинку по UUID
```
curl -X 'GET' \
  'http://127.0.0.1:8000/api/images/get/$UUID' \
  -H 'accept: application/json'
```
#### Получить список всех сгенерированных картинок
```
curl -X 'GET' \
  'http://127.0.0.1:8000/api/images' \
  -H 'accept: application/json'
```
#### Удалить картинку с сервера по её UUID
```
curl -X 'DELETE' \
  'http://127.0.0.1:8000/api/images/delete/123' \
  -H 'accept: application/json'
```
#### Сгенерировать новое изображение
```
curl -X 'POST' \
    'http://127.0.0.1:8000/api/generate'   \
    -H 'accept: application/json'   \
    -H 'Content-Type: application/json'   \
    -d '{"img" : "IMG_URL", "text" : "text"}'
```

