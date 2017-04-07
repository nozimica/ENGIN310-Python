TEXNAME=recursion

all:
	rm -rf *.aux *.log *.out *.snm
	xelatex $(TEXNAME).tex
	xelatex $(TEXNAME).tex

compileLive:
	when-changed $(TEXNAME).tex -c make
