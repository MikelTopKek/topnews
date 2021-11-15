You need **git**, **Docker** and **Docker-compose** to run this project.

Core technologies used:
* Django REST framework
* Postgres

Available commands to:
> build project:
> make build_backend

> run project:
> make start_backend

> stop project:
> make stop_backend

> down project:
> make down_backend

> to run tests
> make run_test

Work with project:
* Create file env/.env.local and env/.env.test from env/.env.example
* Change USE_S3 var if you want to upload your logo`s and avatars to AWS S3 bucket
* Go to backend/ folder
* Build and run project
* All functions are available in swagger. 
* Sign up your user
* Take Bearer access token from /login
* Press Authorize button and insert token like in the example: "Bearer <your-token>" 
* Enjoy!

Create superuser:
* Superuser already created in data migration (/rest_api/migrations/0001_init_db_data.py)
> Login: admin 
> 
> Password: password
* If you want to create another - go to web container 
> docker exec -it backend_web_1 /bin/bash
* run python manage.py createsuperuser
* write your login and password

Django admin: http://localhost:8000/admin/

Django swagger: http://localhost:8000/swagger/

#### If you have troubles with postgres, just run command
> docker system prune --all
#### If you have conflicts with postgres on your ubuntu you can stop it
> sudo systemctl stop postgresql
#### If you have problems with db while testing add recursive read/write permissions to backend/data/ directory