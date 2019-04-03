dev:
	pip install -U -r requirements.txt

test:
	flake8 .
	py.test --cov=. .