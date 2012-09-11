default:
	latex main
	latex main
	latex main
	dvipdf main

clean:
	rm -f *.aux *.log *.dvi *.pdf

