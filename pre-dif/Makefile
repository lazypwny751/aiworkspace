# Diferansiyel Denklemler türev/integral özet notları için Makefile

XETEX=xelatex
MAIN=src/main

all: pdf

pdf:
	$(XETEX) $(MAIN).tex
	$(XETEX) $(MAIN).tex

clean:
	rm -f $(MAIN).aux $(MAIN).log $(MAIN).out $(MAIN).toc
	rm -f src/*.aux src/*.log src/*.out src/*.toc
	rm -f *.aux *.log *.out *.toc *.pdf

.PHONY: all pdf clean