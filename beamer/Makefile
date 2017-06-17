################################################################################
### Parameters:

# export TEXINPUTS:=.:./texmf:~/texmf:${TEXINPUTS}
export TEXMFHOME:=.:./texmf:~/texmf:${TEXMFHOME}

TEXNAME=presentacion
TEXCOMM=xelatex -halt-on-error -shell-escape
#TEXCOMM=pdflatex -halt-on-error
PANDOC=$(HOME)/.cabal/bin/pandoc -f markdown -t beamer --filter overlay_filter --slide-level=2

MD_INFILES := $(wildcard tex/*.md.tex)
MD_OUTFILES := $(MD_INFILES:.md.tex=.tex)

SRC_FILES := $(wildcard ../scripts/*[^8].py)
SRC_OUTFILES := $(SRC_FILES:.py=.utf8.py)

################################################################################
### Rules:

default: $(TEXNAME).pdf

%.tex: %.md.tex
	$(PANDOC) $? -o $@

%.utf8.py: %.py
	/usr/bin/iconv -f cp1252 -t utf8 $? -o $@

$(TEXNAME).pdf: $(TEXNAME).tex $(MD_OUTFILES) engin310.sty common.macros.tex $(SRC_OUTFILES)
	# biber $(TEXNAME) --output_format bibtex
	$(TEXCOMM) -no-pdf $(TEXNAME).tex && rm -f $(TEXNAME).xdv
	# bibtex $(TEXNAME)
	$(TEXCOMM) -interaction=batchmode $(TEXNAME).tex
	# $(TEXCOMM) $(TEXNAME).tex

clean:
	rm -f *.aux *.blg *.log *.toc *.lot *.lof *.bbl *.nav *.out *.snm *.vrb *.xdv tex/*.aux $(MD_OUTFILES)

complete: clean
	$(TEXCOMM) $(TEXNAME).tex
	$(TEXCOMM) $(TEXNAME).tex

handout:
	cp -f $(TEXNAME).tex $(TEXNAME)-handout.tex
	sed -i 's:documentclass\[\(.*\)\]{beamer}:documentclass[\1,handout]{beamer}:' $(TEXNAME)-handout.tex
	$(TEXCOMM) $(TEXNAME)-handout.tex
	$(TEXCOMM) $(TEXNAME)-handout.tex
	$(TEXCOMM) $(TEXNAME)-handout.tex
	gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dNOPAUSE -dQUIET -dBATCH \
		-sOutputFile=$(TEXNAME)-handout-reduc.pdf $(TEXNAME)-handout.pdf
	#mv -f $(TEXNAME)-handout-reduc.pdf $(TEXNAME)-handout.pdf

reduce:
	gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dNOPAUSE -dQUIET -dBATCH \
		-sOutputFile=$(TEXNAME)-reduc.pdf $(TEXNAME).pdf

compileLive:
	when-changed tex/*.md.tex engin310.sty common.macros.tex $(TEXNAME).tex -c make

