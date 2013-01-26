.PHONY : all
all:
	python main.py 1>&2

.PHONY : test
test:
	python test.py

