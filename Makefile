.PHONY: all test

all: test

test:
	python -m unittest discover -v
