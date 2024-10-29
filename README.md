Домашняя работа 23.1 Права доступа


Для запуска проекта откройте PGAdmin и создайте новую БД указанную в файле config/settings.py, переменная DATABASES(значение NAME). Так же измените другие значения в этой переменной для успешного запуска проекта(PASSWORD - в любом случае, а остальные - если они у вас отличаются).


Еще для запуска проекта установите зависимости указанные в файле pyproject.toml


Для создания суперпользователя введите в терминале: python manage.py csu
Почта и пароль суперпользователя указаны в файле users/managment/cammands/csu.py


Данные сохранены в трёх json-файлах.
Для загрузки данных в БД введите в терминале три команды:

python manage.py loaddata data.json

python manage.py loaddata users.json

python manage.py loaddata groups.json


Проект настроен на регистрацию почты Яндекс.
Для регистрации измените в файле config/settings следующие переменные:

EMAIL_HOST_USER = <ваша почта>

EMAIL_HOST_PASSWORD = <ваш пароль приложения>


Для перенастройки на регистрацию в Маил.ру измените в файле config/settings следующие переменные:

EMAIL_HOST = 'smtp.mail.ru'

EMAIL_PORT = 2525

EMAIL_HOST_USER = <ваша почта>

EMAIL_HOST_PASSWORD = <ваш пароль приложения>


Для перенастройки на регистрацию в Гугл измените в файле config/settings следующие переменные:

EMAIL_HOST = 'smtp.gmail.com'

EMAIL_PORT = 587

EMAIL_HOST_USER = <ваша почта>

EMAIL_HOST_PASSWORD = <ваш пароль приложения>


Если возникнут проблемы с отправкой письма на почту. Есть уже созданый пользователь добавленный в группу модераторов и хранящийся в файле users.json 

Почта: admin@sky.com

Пароль: 123qwerty
