build:
	docker build -t codingric/catch-test ./app
	docker push codingric/catch-test

serve: build
	docker run -p 8000:8000 codingric/catch-test