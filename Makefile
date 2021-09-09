.PHONY: build
build:
	docker build ./chateslav -f chateslav/Dockerfile -t chateslav

.PHONY: start
start:
	docker run -it -p 8000:8000 chateslav