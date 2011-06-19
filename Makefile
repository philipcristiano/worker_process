PYTHON=bin/python
NOSETESTS=bin/nosetests

test:
	$(NOSETESTS) tests

.PHONY: develop
develop:
	$(PYTHON) setup.py develop

.PHONY: dist
dist:
	$(PYTHON) setup.py sdist

.PHONY: requirements
requirements:
	bin/pip install -r requirements.pip
	bin/easy_install nose-machineout

.PHONY: virtualenv
virtualenv:
	virtualenv --no-site-packages --distribute .

.PHONY: install
install:
	$(PYTHON) setup.py install

.PHONY: upload
upload:
	$(PYTHON) setup.py sdist upload
