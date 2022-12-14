# ANBOX74 - всякая всячина!

### Установка и запуск проекта

Клонируем репозиторий и переходим в корень проекта
```
git clone https://github.com/AlexKhlybov/anbox74.git
cd ./anbox74
```

Устанавливаем окружение
```
python3 -m venv venv
```

Активируем окружение
```
source ./venv/bin/activate  # MacOs, Linux
venv\Scripts\activate  #Windows
```

Устанавливаем зависимости
```
pip install -r requirements.txt
```

Выполнение миграций
```
python3 manage.py migrate
```

Заполнение БД тестовыми данными (у всех созданных пользователей пароль - 1)
```
python3 manage.py dbimport
```

Запускаем проект и радуемся
```
python3 manage.py runserver
```