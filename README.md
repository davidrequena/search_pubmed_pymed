# search_pubmed
Searches for articles in PubMed using an user input, and outputs an Excel table with the results.


### AUTHOR AND CONTACT
Script made by David Requena [02/17/2020]

The Rockefeller University. New York, USA.

Contact: drequena@rockefeller.edu / d.requena.a@gmail.com


### DESCRIPTION
This code asks the user for a query to be searched in PubMed. This can include Field Tags:
https://www.ncbi.nlm.nih.gov/books/NBK3827/#pubmedhelp.Search_Field_Descriptions_and

Then, it retrieves the PubMed ID (PMID), publication date, the title,
list of authors (separated by semicolon), journal name, DOI, keywords and abstract.
And finally saves the info in a table (in MS Excel .xlsx format) in the current directory.


### REQUISITES
You need to have installed Python 3 (https://www.python.org/downloads/) and the following modules:

1. pandas -> can be installed by writting in the Terminal: pip install pandas
2. pymed -> can be installed by writting in the Terminal: pip install pymed
3. openpyxl -> can be installed by writting in the Terminal: pip install openpyxl


### USAGE
Just doble-click on the script to execute it. This can also be called from the Terminal.
Then, the program will ask you to:

First, provide a query. Here you have two equivalent examples:

    Example 1: (Fowlpox OR FPV) AND (Reticuloendotheliosis OR REV)
    Example 2: (Fowlpox[All Fields] OR FPV[All Fields]) AND (Reticuloendotheliosis[All Fields] OR REV[All Fields])

Second, provide an e-mail address (optional). You can just say no.

Third, the maximum number of results desired.

I'm including an example of the output table.

### CREDITS
I used the following links as references:

1. https://stackoverflow.com/questions/57053378/
2. https://www.kaggle.com/summerkrankin/pubmed-download-als
