.PHONY: help

help: ## Help
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

init: ## Initialize Application
	@echo "Setting up the Application"
	@pip install -r requirements.txt
	@cp .env.sample .env
	@export PYTHONPATH=$PYTHONPATH:$PWD
	@docker-compose up -d
	@alembic upgrade head
