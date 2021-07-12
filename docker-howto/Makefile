build:
	docker build -t getting-started:v1.0 .

start:
	docker run --name getting-started -dp 8080:8080 getting-started:v1.0

stop:
	docker stop getting-started

test:
	curl localhost:8080