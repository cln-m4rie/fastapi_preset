default: help

format:  ## format all python codes
	autoflake --in-place --remove-unused-variables --remove-all-unused-imports --ignore-init-module-imports --recursive . && \
	isort -rc && \
	black .

dev:
	uvicorn app.server:app --reload

help:  ## Show all of tasks
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
