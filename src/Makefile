COMMIT_SHA = $(shell git rev-parse --short @)

build:

	docker build \
		-t codingric/catch-test \
		-t codingric/catch-test:${COMMIT_SHA} \
		--build-arg opts="GOOS=linux" \
		./app

	# Compile for Raspberry Pi4 (running k3s)
	docker build \
		--build-arg opts="GOARCH=arm GOARM=7 GOOS=linux" \
		-t codingric/catch-test:armv7 \
		-t codingric/catch-test:armv7-${COMMIT_SHA} \
		./app

distribute:
	docker push codingric/catch-test
	docker push codingric/catch-test:${COMMIT_SHA}
	docker push codingric/catch-test:armv7
	docker push codingric/catch-test:armv7-${COMMIT_SHA}

serve:
	docker run -p 8000:8000 codingric/catch-test

deploy-pi:
	sed -e "s^codingric/catch-test:[-a-z0-9]*^codingric/catch-test:armv7-${COMMIT_SHA}^" k8s/deployment.yaml | \
		kubectl apply -f -

deploy:
	sed -e "s^codingric/catch-test:[-a-z0-9]*^codingric/catch-test:${COMMIT_SHA}^" k8s/deployment.yaml | \
		kubectl apply -f -

tests:
	docker-compose run tests \
	&& docker-compose down