.PHONY: run
run:
	echo 'll'
	echo 'kk'
	black .
	isort .
	flake8 .
