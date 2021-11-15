current_dir = $(shell pwd)

start_backend:
	docker-compose -f docker-compose.yml up ;

stop_backend:
	docker-compose -f docker-compose.yml stop;

build_backend:
	docker-compose -f docker-compose.yml build;

down_backend:
	docker-compose -f docker-compose.yml down;

run_test:
	docker-compose -f docker-compose-test.yml up --build --abort-on-container-exit;
