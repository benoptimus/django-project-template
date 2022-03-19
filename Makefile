build:
	docker-compose build

up:
	docker-compose up -d
shell:
	docker-compose exec backend /bin/sh

nginx:
	docker-compose exec nginx /bin/bash
