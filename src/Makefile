.PHONY: start build run down 


down:
	docker compose down

run: down 
	docker compose up postgres redis -d
	sleep 2
	alembic upgrade head
	uvicorn src.main:app --reload

start:
	uvicorn src.main:app --reload

build: down
	docker compose up -d --build

