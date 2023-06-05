.PHONY: build tag push all
TAG=$(shell git rev-parse HEAD | head -c8)

build tag:
	export TAG=$(TAG) && \
	docker-compose build --no-cache

push:
	docker-compose push

all: build push
