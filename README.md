# easy_bot
Приложение для сохранения сообщений

# Задание
Написать docker compose, в котором работают: web приложение, на FastApi. У приложения должно быть несколько ендпоинтов: 1) GET 'api/v1/messages/' показывает спосиок всех сообщений; 2) POST 'api/v1/message/' позволяет написать сообщение; Веб сервер должен быть Nginx. mongo как бд для сообщений. Телеграм бот (aiogram3), который показывает сообщения и позволяет создать сообщение самому. Будет плюсом: 1) Добавление кэширования при помощи Redis (кеш стирается, когда появляется новое сообщение) 2) Развертывание на удалённом сервере и добавление ssl через certbot. 3) Реализовать код так, чтобы было видно, кто написал сообщение. 4) Добавление пагинации.

## Что сделано из списка:
- docker compose
- веб-приложение
- Прикручена БД mongodb
- Телеграм бот показывает список сообщений и позволяет добавить новое. Если сообщение сохраняется с бота - автор указывается по username юзера тг. Если через веб приложение напрямую - автор анонимен

# Запуск вручную
Для приложения необходим файл .env c содержимым

DATABASE_URL=...
BOT_TOKEN=...
WEBHOOK_URL=https://...

Установить requirements.txt
pip install -r easy_bot/requirements.txt

Установить MongoDB https://www.mongodb.com/docs/manual/installation/

Запустить демон МонгоДБ

Запустить приложение easy_bot/main.py

Кайфовать
