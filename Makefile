default:
	pdflatex -shell-escape main
	pdflatex -shell-escape main
	pdflatex -shell-escape main

clean:
	rm -f *.aux *.log *.pdf

