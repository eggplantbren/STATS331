FILENAMES = main
PDFS = $(foreach f, $(FILENAMES), $(f).pdf)

# The default build rule
%.pdf: %.tex
	latex $*
	latex $*
	latex $*
	dvipdf $*

default: $(PDFS)

clean:
	rm -f *.aux *.log *.dvi *.pdf

