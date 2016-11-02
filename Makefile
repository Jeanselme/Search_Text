PIP=pip3
PYTHON=python3.5

TESTS_PY=$(wildcard ./Tests/*/[^__]*.py)
# goes from ./tests/myPython.py to tests.myPython
TESTS=$(subst /,.,$(subst ./,, $(subst .py$,, $(TESTS_PY))))

init:
	sudo ${PIP} install -r requirements.txt

test:
	for file_test in ${TESTS} ; do \
	    echo "==> Testing $$file_test" ;\
		$(PYTHON) -m unittest $$file_test ;\
	done