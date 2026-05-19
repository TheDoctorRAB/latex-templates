# latex-templates
Latex templates for pdf tagging under Title II compliance.

Update texlive to the latest version.

Compile with pdflatex.

show-pdf-tags --xml filename.pdf to see the tagging.

Latex has to be less customized to meet compliance.

Do not even load titlsec,titletoc.  
Currently have not figured out how to cusomtize sections. 

With tagging=on, and loading enumitem.sty, latex-lab-enumitem is automatically loaded by the kernal.  
There are new parameters that have to be used instead of topsep=0ex,itemsep=1ex.  
[latex-lab-enumitem](https://www.tug.org/texlive//Contents/live/texmf-dist/doc/latex-dev/latex-lab/latex-lab-enumitem.pdf)  
See the sample files for examples. 

With using series= and resume=, load enumext.sty and use topsep=0ex,itemsep=0ex.  
enumext does not take leftmargin=X  
Comment out enumitem.sty  
Do not load enumitem.sty and enumext.sty together.

The white-paper directory has an example accessible file with longtable.

The Ally checker in Canvas was used to verify accessibility. 


Prof. R. A. Borrelli  
University of Idaho  
Nuclear Engineering  
