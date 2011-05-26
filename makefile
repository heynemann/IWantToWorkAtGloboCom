# Makefile simples para executar o projeto

PYTHON = python

all: test

test:
	cd acme_corp && $(PYTHON) core.py

sincrono:
	cd acme_corp && $(PYTHON) core.py sincrono

painel:
	cd acme_corp && $(PYTHON) acmectl.py