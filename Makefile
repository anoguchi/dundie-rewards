.PHONY: install virtualenv ipython clean test

install:
	@echo "Installing for dev environment"
	@.venv/bin/python3 -m pip install -e '.[dev]'
	
virtualenv:
	@echo "Creating virtual environment"
	@python3 -m venv .venv

ipython:
	@echo "Starting ipython"
	@.venv/bin/ipython

watch:
	#@.venv/bin/ptw
	@ls **/*.py | entr -c .venv/bin/pytest -s

test:
	@.venv/bin/pytest -s

testci:
	@.venv/bin/pytest -v --junitxml=test-results.xml

clean:					## Clean unused files.
	@find ./ -name "*.pyc" -exec rm -f {} \;
	@find ./ -name "__pycache__" -exec rm -f {} \;
	@find ./ -name "Thumbs.db" -exec rm -f {} \;
	@find ./ -name "*~" -exec rm -f {} \;
	@rm -rf .cache
	@rm -rf .pytest_cache
	@rm -rf .mypy_cache
	@rm -rf build
	@rm -rf dist
	@rm -rf *.egg-info
	@rm -rf htmlcov
	@rm -rf .tox/
	@rm -rf docs/_build
