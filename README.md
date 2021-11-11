You need **git**, **Docker** and **Docker-compose** to run this project.

Core technologies used:
* Django REST framework
* Postgres

Available commands to:
> build:
> make build_backend

> run:
> make start_backend

> stop:
> make stop_backend

> down:
> make down_backend

Work with project:
* Create file env/.env.local from env/.env.example
* Change USE_S3 var if you want to upload your logo`s and avatars to AWS S3 bucket
* Go to backend/ folder
* Build and run project
* All functions are available in swagger. 
* Sign up your user
* Take Bearer access token from /token
* Press Authorize button and insert token like in the example: "Bearer <your-token>" 
* Enjoy!

Create superuser:
* Go to web container 
> docker exec -it backend_web_1 /bin/bash
* run python manage.py createsuperuser
* write your logpass

Django admin: http://localhost:8000/admin/

Django swagger: http://localhost:8000/swagger/

#### If you have troubles with postgres, just run command
> docker system prune --all
#### If you have conflicts with postgres on your ubuntu you can stop it
> sudo systemctl stop postgresql