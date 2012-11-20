default:
	pdflatex main
	pdflatex main
	pdflatex main

clean:
	rm -f *.aux *.log *.pdf

