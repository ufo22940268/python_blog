.PHONY : clear-cli
clear-cli:
	clear

.PHONY : all
all: clear-cli
	python main.py 1>&2

.PHONY : test
test: clear-cli
	python test.py

.PHONY : update-db
update-db : clear-cli
	python db_tools.py update

.PHONY : create-db
create-db : clear-cli
	python db_tools.py create

.PHONY : update
update : update
	python tools.py. update
