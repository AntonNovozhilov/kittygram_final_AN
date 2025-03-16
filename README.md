## Что может это проект:
- Добавлять , редактировать , удалять , просматривать котов.
- Добавлять , редактировать уже сущществующие достижения для котов.

## Как работать с проектом.
1. Скопируйте репозиторий к себе на компьютер с помощью команды 
`git clone git@github.com:AntonNovozhilov/kittygram_final.git`

2. Создайте файл .env и заполните своими данные, данные которые необходимо заполнить можете посмотреть в корневой папке в файле .env.example

3. Создайте Docker images

```
cd frontend
docker build -t <Ваш ник на dockerhub>/kittygram_frontend .
cd ../backend
docker build -t <Ваш ник на dockerhub>/kittygram_backend .
cd ../nginx
docker build -t <Ваш ник на dockerhub>/kittygram_gateway .
```

4. Загрузите образы на Dockerhub

пример команды 
`docker push <Ваш ник на dockerhub>/kittygram_frontend`

5. Подключитесь к удаленному серверу 
`ssh -i путь_до_файла_с_SSH_ключом/название_файла_с_SSH_ключом имя_пользователя@ip_адрес_сервера`

6. Создайте на сервере директорию 
`mkdir название директории`

7. Установите Docker compose 
```
sudo apt update
sudo apt install curl
curl -fSL https://get.docker.com -o get-docker.sh
sudo sh ./get-docker.sh
sudo apt-get install docker-compose-plugin
```

8. Скопируйте на сервер docker-compose.production.yml

```
scp -i path_to_SSH/SSH_name docker-compose.production.yml username@server_ip:/home/username/kittygram/docker-compose.production.yml
* ath_to_SSH — путь к файлу с SSH-ключом;
* SSH_name — имя файла с SSH-ключом (без расширения);
* username — ваше имя пользователя на сервере;
* server_ip — IP вашего сервера.
```

9. Запустите docker compose в режиме демона
`sudo docker compose -f docker-compose.production.yml up -d`

10. Выполните миграции , соберите статику, скориуйте ее в директорию бекенда
```
sudo docker compose -f docker-compose.production.yml exec backend python manage.py migrate
sudo docker compose -f docker-compose.production.yml exec backend python manage.py collectstatic
sudo docker compose -f docker-compose.production.yml exec backend cp -r /app/collected_static/. /backend_static/static/
```

11. На сервере в главной директории откройте конфг nginx через nano
`sudo nano /etc/nginx/sites-enabled/default`

12. Замените секцию location 

```
location / {
    proxy_set_header Host $http_host;
    proxy_pass http://127.0.0.1:9000;
}
```

13. перезапустите nginx 
`sudo service nginx reload`

14. Настройте CI и CD 
Файл workflows находится в диреткори /.github/workflows/

Для запуска вам нужно на гите в action установить секреты 
DOCKER_USERNAME                # имя пользователя в DockerHub
DOCKER_PASSWORD                # пароль пользователя в DockerHub
HOST                           # ip_address сервера
USER                           # имя пользователя
SSH_KEY                        # приватный ssh-ключ (cat ~/.ssh/id_rsa)
SSH_PASSPHRASE                 # кодовая фраза (пароль) для ssh-ключа

TELEGRAM_TO                    # id телеграм-аккаунта (можно узнать у @userinfobot, команда /start)
TELEGRAM_TOKEN                 # токен бота (получить токен можно у @BotFather, /token, имя бота)

![CI status push main](https://github.com/AntonNovozhilov/kittygram_final/actions/workflows/WORKFLOW-FILE/badge.svg?branch=main&event=push)

[Автор](https://github.com/AntonNovozhilov)
