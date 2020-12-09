lint:
	flake8 . && pydocstyle src/


test:
	docker-compose run --rm web python manage.py cov
