PYTHON := $(shell which python3 || which python)

check:
	@if [ -z "$(PYTHON)" ]; then \
		echo "Python is not installed."; \
		exit 1; \
	else \
		echo "Python found: $(PYTHON)"; \
	fi
	@if ! $(PYTHON) -c "import sys; assert sys.version_info >= (3,0)"; then \
		echo "Python 3.x is required."; \
		exit 1; \
	else \
		echo "Python version is compatible."; \
	fi

encrypt: check
	python3 encrypt.py

decrypt: check
	python3 decrypt.py


run: check encrypt decrypt

clean:
	find . -type f -name '*.pyc' -delete

.PHONY: check encrypt decrypt run clean