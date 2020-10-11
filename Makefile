build:
	docker-compose build --parallel
bash:
	docker-compose run --rm api bash

makemigrations:
	docker-compose run --rm api python manage.py makemigrations

showmigrations:
	docker-compose run --rm api python manage.py showmigrations

migrate:
	docker-compose run --rm api python manage.py migrate

runserver:
	docker-compose up

createsuperuser:
	docker-compose run --rm api python manage.py createsuperuser

shell:
	docker-compose run --rm api python manage.py shell_plus --print-sql

test:
	docker-compose run --rm api python manage.py test
