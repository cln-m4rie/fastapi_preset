default: | help

develop: ## install with develop
	pip install --force-reinstall -e .[dev]
	python setup.py develop

format: ## auto format
	autoflake --in-place --remove-all-unused-imports --remove-unused-variables --recursive fastapi_preset && \
		isort -rc fastapi_preset && \
		black --line-length 119 fastapi_preset

help:  ## Show all of tasks
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
