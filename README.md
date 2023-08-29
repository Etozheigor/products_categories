# Products App
### О проекте
Products App - проект для создания продуктов и их категорий. После регистрации в сервисе пользователь может создавать различные продукты и относить их к различным категориям. Редактировать и удалять продукты и категории может только администратор.
Доступна фильтрация по продуктам:
- цена от и до
- название
- название категории
- опубликован ли продукт
- удален ли продукт

### Технологии
- Python
- Django
- DRF
- Djoser
- Docker
- PostgreSQL

### Как запустить проект
- Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:Etozheigor/products_categories.git
```

```
cd products_categories
```

- Активировать виртуальное окружение и установить зависимости:

```
poetry shell
poetry install
```

- перейти в папку products_app/products_app, создать файл .env и заполнить его по шаблону (можно использовать
файл .env.example, заполнив необходимые данные и просто переименовав его в .env) :


шаблон заполнения файла:

```
SECRET_KEY= # секретный ключ Джанго-проекта
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres # имя базы данных
POSTGRES_USER= # логин для подключения к базе данных (установите свой)
POSTGRES_PASSWORD= # пароль для подключения к БД (установите свой)
DB_HOST=localhost
DB_PORT=5432
```


База данных Postgres запускается в контейнере Docker:

- Перейти в папку с файлом docker-compose.yml и запустить контейнер:

```
docker-compose up
```
- Перейти в папку bookmarks_app, выполнить миграции и запустить проект

```
cd products_app
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Проект будет доступен локально по адресу:

```
http://localhost/
```

Документация к Api находится по адресу:

```
http://localhost/swagger/
```

### Эндпоинты проекта:
- Регистрация пользователя:
```
http://localhost/api/v1/users/
```
- Вход/выход из системы (получение токена)
```
http://localhost/api/v1/auth/jwt/create/
http://localhost/api/v1/auth/jwt/refresh/
http://localhost/api/v1/auth/jwt/verify/
```
- Добавление/получение/изменение продуктов:
```
http://localhost/api/v1/products/
```
- Добавление/получение/изменение категорий:
```
http://localhost/api/v1/categories/
```
