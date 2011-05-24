# Makefile simples para gerar um html do cv usando markdown

MKD = markdown

all: html

html: cv.mkd
	$(MKD) cv.mkd > cv.html

clean: cv.mkd
	-rm cv.html