Mendeley outputs bibtex .bib files in a certain format. That format includes
the file that you store it in on your local computer, annotations you've made,
etc. That is inconvenient for two reasons:
- it's embarrassing and maybe dangerous (I'm thinking my annotations are private).
- it's big, which is a problem if you want to import into Overleaf (1mb limit).

This is a crummy little script that tries to shrink that file by taking out all
that stuff you don't need. To run:

./shorten_bibtex.py --input_file=(file) > output.bib
