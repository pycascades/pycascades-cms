.PHONY: help
help: ## Shows a list of all defined targets and their help messages
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: build
build: ## Build the Docker image
	docker-compose -p pycascades build

.PHONY: up
up: build ## Bring the container up
	docker-compose -p pycascades up -d

.PHONY: start
start: ## Start the full set of containers
	docker-compose -p pycascades start

.PHONY: stop
stop: ## Stop the container
	docker-compose -p pycascades stop

.PHONY: enter
enter: ## Enter the running container
	docker-compose -p pycascades exec app /bin/bash
