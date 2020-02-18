# search_pubmed
Searches for articles in PubMed using an user input, and outputs an Excel table with the results.


### AUTHOR AND CONTACT
Script made by David Requena [02/17/2020]

The Rockefeller University. New York, USA.

Contact: drequena@rockefeller.edu / d.requena.a@gmail.com


### DESCRIPTION
This code asks the user for a query to be searched in PubMed. This can include Field Tags:
https://www.ncbi.nlm.nih.gov/books/NBK3827/#pubmedhelp.Search_Field_Descriptions_and

Then, it retrieves the PubMed ID (PMID), publication date, the list of authors (separated by semicolon),
the journal name, DOI, Keywords and Abstract.
And finally saves the info in a table (MS Excel .xlsx format) in the current directory.


### REQUISITES
You need to have installed Python 3 and the following modules:

pandas (pip install pandas)

pymed (pip install pymed)

openpyxl (pip install openpyxl)


### CREDITS
I used the following links as references:

https://stackoverflow.com/questions/57053378/

https://www.kaggle.com/summerkrankin/pubmed-download-als
