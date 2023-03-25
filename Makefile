test:
	PYTHONPATH=. pytest tests/ --cache-clear

coverage:
	PYTHONPATH=. pytest -vv --cov=tests/ --cache-clear