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

.PHONY: run
run:
	$(VPYTHON) pymod

.PHONY: dist
dist:
	$(VPYTHON) setup.py sdist

.PHONY: config-stage
config-stage:
	scp conf/stage/index.py wf:~/webapps/pymod_stage/htdocs/index.py

.PHONY: push-stage
push-stage: dist
	scp dist/pymod.me-*.tar.gz wf:~/webapps/pymod_stage

.PHONY: deploy-stage
deploy-stage: config-stage push-stage
	ssh wf "cd ~/webapps/pymod_stage && ./bin/pip install --upgrade pymod.me-*.tar.gz"
	make restart-stage

.PHONY: restart-stage
restart-stage:
	ssh wf "~/webapps/pymod_stage/apache2/bin/restart"

.PHONY: rebuild
rebuild: clean all
