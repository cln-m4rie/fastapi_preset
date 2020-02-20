format:  ## format all python codes
	autoflake --in-place --remove-unused-variables --remove-all-unused-imports --ignore-init-module-imports --recursive . && \
	isort -rc && \
	black .

dev:
	uvicorn server:app --reload
