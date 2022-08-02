Инструкция по запуску :

    $ mkdir somedir/

    $ cd somedir

    $ git clone https://github.com/alexgreyshark/test-compas.git

    $ cd test-compas/compas

    $ docker-compose up -d

    $ docker-compose exec web python manage.py migrate

Если на последнем этапе ошибка: не видно модель User, то:
    
    $ docker-compose exec web python manage.py makemigrations user_selection

    $ docker-compose exec web python manage.py migrate user_selection

    $ docker-compose exec web python manage.py migrate


Далее открыть http://localhost:8000/

Создание суперопользователя

    $ docker-compose exec web python manage.py createsuperuser

Создание пользователей с помощью Django command

    $ docker-compose exec web python manage.py create_users

Открыть http://localhost:8000/admin для проверки того, что есть в БД
либо http://localhost:8000/api/users/