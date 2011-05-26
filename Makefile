BIN=main
SRC=ACME/ControlaAr.py

all: permissions
	ln -s -f ${SRC} ${BIN}
  
permissions:
	chmod a+x ${SRC}
  
clean:
	rm -rf ${BIN}
	chmod a-x ${SRC}