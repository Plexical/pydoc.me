VENV=~/src/ext/python/virtualenv
PYTHON=python3
PROJECT=`pwd`
BIN=$(PROJECT)/bin
PIP=$(BIN)/pip
VPYTHON=$(BIN)/python
VERSION=`$(VPYTHON) -c "import pymod; print(pymod.vstr())"`
PKGNAME=pymod.me-$(VERSION).tar.gz

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
	$(VPYTHON) -m pymod --serve

.PHONY: clean-dist
clean-dist:
	rm -rf dist/*

.PHONY: dist
dist: clean-dist
	$(VPYTHON) setup.py sdist

.PHONY: config-stage
config-stage:
	scp conf/stage/index.py wf:~/webapps/pymod_stage/htdocs/index.py
	scp conf/stage/gitignore wf:~/webapps/pymod_stage/.gitignore

.PHONY: push-stage
push-stage: dist
	scp dist/$(PKGNAME) wf:~/webapps/pymod_stage
	rsync -arv static/ wf:~/webapps/pymod_stage_static/

.PHONY: deploy-stage
deploy-stage: config-stage push-stage
	ssh wf "cd ~/webapps/pymod_stage && ./bin/pip install --upgrade $(PKGNAME)"
	make restart-stage

.PHONY: restart-stage
restart-stage:
	ssh wf "~/webapps/pymod_stage/apache2/bin/restart"

.PHONY: restart-live
restart-live:
	ssh wf "~/webapps/pymod_live/apache2/bin/restart"

.PHONY: config-live
config-live:
	scp conf/live/index.py wf:~/webapps/pymod_live/htdocs/index.py
	scp conf/live/gitignore wf:~/webapps/pymod_live/.gitignore

.PHONY: push-live
push-live: dist
	scp dist/pymod.me-*.tar.gz wf:~/webapps/pymod_live
	rsync -arv static/ wf:~/webapps/pymod_live_static/

.PHONY: deploy-live
deploy-live: config-live push-live
	ssh wf "cd ~/webapps/pymod_live && ./bin/pip install --upgrade $(PKGNAME)"
	make restart-live

.PHONY: rebuild
rebuild: clean all
