# latex-templates
## bst files for bibliographies

**standard.bst** can be used for a generic journal paper format and meant to be paired with the journal paper template in this repository. References are listed in the bibliography alphabetically. Citations are meant to be as (Borrelli, 2020) in the text. Use with the natbib package. All of the authors are listed in the biblography, last name first.

**neup.bst** should be used for a white paper or preproposal, where space is limited. Pair with the white paper template in this repository. References are listed in the order of appearance. Citations are meant to be as [1] in the text to save space. Use with the natbib package. Only first author is listed in the bibliography, last name first, then with 'et al.'

**nsf.bst** is the same as _neup.bst_ in that it gives numbered citations in the referenced order, but the citation provides the full author information because NSF does not have page limits for the References Cited document. Also use with natbib.

**ans-transactions.bst** is for ANS conference papers. Use with the [ans.cls](https://www.ans.org/pubs/transactions/). _ans-transactions.bst_ is a modified form of what ANS provides. The author list was modified to the abbreviated 'et al.' format in _neup.bst_ but maintains the ANS required fonts; e.g., all capitals and initials. 
