# latex-templates  
This repository will develop digitally accessible lecture slides resources. 

The beamer.cls style is out. It will not work anymore. The [ltx-talk.cls](https://ctan.org/pkg/ltx-talk) is what is supposed to be used. It is considered still experimental so there is not a lot of resources out there. 

Currently, a beamer presentation (as a pdf) can be converted to html via pdf2htmlEX which can be installed on the command line. Do not turn on any of the tagging features when compiling the tex file. Do use the alternative text for the graphics. Ally will flag the html file as not having alternative text for links because latex does not do that, but Ally still gives a very good at 90%+. However, (1) best practice would recommend to just make the links verbose, and (2) the converted html file can be edited to just add the alternative text for the links manually. This is a workaround of course but not that bad. 

Ideally, the text file should be able to be compiled directly just like for the syllabus and the other documents. There is no direct one-to-one conversion of beamer to ltx-talk. 

ltx-talk is already included in the 2026 tex-live installation.

[Examples](https://www.texdev.net/ltx-talk/examples/)

So far, going line by line and just searching how to obtain a similar look and feel to beamer is the current practice. 


## ltx-talk issues
ltx-talk leaves a lot to be desired in terms of the flexible customiztion that beamer offers. With so much incompatibility, the workaround is to figure out how to 'hard code' the desired result, which is not really the purpose of latex. The debate is whether converting beamer to html and just adding alternative text to the links would be more efficient. However, alternative text is still needed for images. 

The slides are just not going to look as good as beamer. 

- The caption package is incompatible. A workaround has been included. For some reason, the colon cannot be omitted and replaced by something else; e.g., Figure 1. for Figure 1: 
- allowframebreaks does not work. No alternatives have been found yet. 
- Using the \section environment to print a frame renders \printnoidxglossaries incompatible. A workaround has been included. 
- Inexplicably, the frametitle does not automatically linewrap because ltx-talk assumes that presentation titles are designed to be short. This is incorrect when applying an assertion-evidence design methodology in preparing slides. A linewrap has been coded in the preamble. However, when the linewrap occurs, the header does not automatically expand to accomodate the text. In the preamble, both can be toggled. Currently, a two line frametitle is set in the preamble. The frametitle is not quite vertically aligned but close enough. 
- \frametitle{} must be used
- bibtex does not work. No custom bst files. Only blblatex can be used. There is the same issue with \section and \printbibliography as there is with \printnoidxglossaries, but there is no workaround yet.


The slides here were compiled with pdflatex and given 100% in Ally on Canvas. Checking the pdf tags showed the links were correctly tagged. 


Prof. R. A. Borrelli  
University of Idaho  
Nuclear Engineering  
