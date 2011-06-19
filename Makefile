NOSETESTS = nosetests -m '([Dd]escribe|[Ww]hen|[Ss]hould|[Tt]est)' -e DingusTestCase

unit-test:
	$(NOSETESTS) tests/unit/*.py

acceptance-test:
	$(NOSETESTS) tests/acceptance/*.py

develop:
	bin/python setup.py develop

.PHONY: dist
dist:
	bin/python setup.py sdist

virtualenv:
	virtualenv --no-site-packages --distribute .

create:
	bin/plug create --package=dist/plug-0.1.0.tar.gz

install:
	sudo bin/plug install --plug=plug-0.1.0.tar.gz.plug
