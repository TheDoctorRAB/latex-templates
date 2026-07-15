# latex-templates  
This repository will develop digitally accessible lecture slides resources. 

The beamer.cls style is out. It will not work anymore. The [ltx-talk.cls](https://ctan.org/pkg/ltx-talk) is what is supposed to be used. It is considered still experimental so there is not a lot of resources out there. 

Currently, a beamer presentation (as a pdf) can be converted to html via pdf2htmlEX which can be installed on the command line. Do not turn on any of the tagging features when compiling the tex file. Do use the alternative text for the graphics. Ally will flag the html file as not having alternative text for links because latex does not do that, but Ally still gives a very good at 90%+. However, (1) best practice would recommend to just make the links verbose, and (2) the converted html file can be edited to just add the alternative text for the links manually. This is a workaround of course but not that bad. 

Ideally, the text file should be able to be compiled directly just like for the syllabus and the other documents. There does not seem to be a direct one-to-one conversion of beamer to ltx-talk. 

ltx-talk is already included in the 2026 tex-live installation.

[Examples](https://www.texdev.net/ltx-talk/examples/)


So far, going line by line and just searching how to convert is the current practice. 

## ltx-talk issues
ltx-talk leaves a lot to be desired in terms of the flexible customiztion that beamer offers. The slides are just not going to look that good. The captions package does not work. 


Figure and table captions cannot easily be customized. Allowframebreaks also does not work, so printing acronyms is effectively useless. There is


Prof. R. A. Borrelli  
University of Idaho  
Nuclear Engineering  
