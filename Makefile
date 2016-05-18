VENV=~/src/ext/python/virtualenv
PYTHON=python3
PROJECT=~/src/oss/pymod.me
BIN=$(PROJECT)/bin
PIP=$(BIN)/pip

all: env

$(PIP):
	$(PYTHON) $(VENV)/virtualenv.py $(PROJECT)

env: $(PIP)

.PHONY: clean
clean:
	rm -rf bin include lib .Python pip-selfcheck.json
