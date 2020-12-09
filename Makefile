lint:
	flake8 . && pydocstyle src/


test:
	docker-compose run --rm web python manage.py cov


run:
	docker-compose up -d --build
