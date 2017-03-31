TEXNAME=recursion

all:
	rm -rf *.aux *.log *.out *.snm
	pdflatex $(TEXNAME).tex
	pdflatex $(TEXNAME).tex

compileLive:
	when-changed $(TEXNAME).tex -c make
