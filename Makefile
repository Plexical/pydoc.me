VENV=~/src/ext/python/virtualenv
PYTHON=python3
PROJECT=~/src/oss/pymod.me
BIN=$(PROJECT)/bin
PIP=$(BIN)/pip
VPYTHON=$(BIN)/python

all: env

$(PIP):
	$(PYTHON) $(VENV)/virtualenv.py $(PROJECT)

deps: $(PIP)
	$(VPYTHON) setup.py develop
	$(PIP) install -r development.txt

env: deps

.PHONY: clean
clean:
	rm -rf bin include lib .Python pip-selfcheck.json

.PHONY: rebuild
rebuild: clean all
