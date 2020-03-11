dev:
	pip install -U -r requirements.txt

format:
	black .
	isort -y

test:
	black . --check
	isort -y . --check-only
	py.test . --flake8 --cov=.