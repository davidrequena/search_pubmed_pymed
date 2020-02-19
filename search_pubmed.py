#--------------------#
# AUTHOR AND CONTACT #
#--------------------#
# Script made by David Requena [02/17/2020]
# The Rockefeller University. New York, USA.
# Contact: drequena@rockefeller.edu / d.requena.a@gmail.com

#-------------#
# DESCRIPTION #
#-------------#
# This code asks the user for a query to be searched in PubMed. This can include Field Tags:
# https://www.ncbi.nlm.nih.gov/books/NBK3827/#pubmedhelp.Search_Field_Descriptions_and
# Then, it retrieves the PubMed ID (PMID), publication date, the title,
# list of authors (separated by semicolon), journal name, DOI, keywords and abstract.
# And finally saves the info in a table (in MS Excel .xlsx format) in the current directory.

#------------#
# REQUISITES #
#------------#
# You need to have installed Python 3: https://www.python.org/downloads/
# And the following modules:
# 1. pandas -> can be installed by writting in the Terminal: pip install pandas
# 2. pymed -> can be installed by writting in the Terminal: pip install pymed
# 3. openpyxl -> can be installed by writting in the Terminal: pip install openpyxl

#-------#
# USAGE #
#-------#
# Just doble-click on the script to execute it. This can also be called from the Terminal.
# Then, the program will ask you to:
#
# First, provide a query. Here you have two equivalent examples:
#
#     Example 1: (Fowlpox OR FPV) AND (Reticuloendotheliosis OR REV)
#     Example 2: (Fowlpox[All Fields] OR FPV[All Fields]) AND (Reticuloendotheliosis[All Fields] OR REV[All Fields])
#
# Second, provide an e-mail address (optional). You can just say no.
#
# I'm including an example of the output table.

#---------#
# CREDITS #
#---------#
# I used the following links as references:
# https://stackoverflow.com/questions/57053378/
# https://www.kaggle.com/summerkrankin/pubmed-download-als

import pandas as pd
from pymed import PubMed
import time


# User inputs:
query = input("Provide a query for PubMed (can include field tags): ")
my_email = input("Provide your e-mail address (optional): ")
max_results = input("Maximum number of results: ")

# Consult PubMed:
pubmed = PubMed(tool="PubMedSearcher", email = my_email)
results = pubmed.query(query, max_results = int(max_results))

# Create an empty Dataframe with just the column names:
articles_df = pd.DataFrame(columns = ['PMID',
                                      'Publication_date',
                                      'Title',
                                      'Authors',
                                      'Journal',
                                      'DOI',
                                      'Keywords',
                                      'Abstract'])

# Now, for each article, fill the dataframe with the info collected:
for article in results:

    # Handle some exceptions in case of missing information:
    try:
        string_keywords = '; '.join([k for k in article.keywords if k is not None])
    except:
        string_keywords = "" # If there are no keywords

    try:
        string_journal = article.journal
    except:
        string_journal = "" # If there is no journal name

    try:
        string_abstract = article.abstract
    except:
        string_abstract = "" # If there is no abstract


    # Extract the first and last name of authors and put them in a nice format,
    # filtering out the empty slots:
    string_authors = '; '.join([a['firstname'] + ' ' + a['lastname'] for a in article.authors
                                if a['firstname'] is not None and a['firstname'] is not None])

    # Collect the article info
    articles_df = articles_df.append({'PMID': article.pubmed_id.partition('\n')[0],
                                      'Publication_date': article.publication_date,
                                      'Title': article.title,
                                      'Authors': string_authors,
                                      'Journal': string_journal,
                                      'DOI': article.doi,
                                      'Keywords': string_keywords,
                                      'Abstract': string_abstract}, ignore_index=True)

# Print the top 5 rows of the dataframe:
print("First 5 results:")
print(articles_df.head(5))

# Export the list of articles as an Excel file with a timestamp
output_file = 'table_of_articles_' + time.strftime("%m%d%Y-%H%M%S") + '.xlsx'
print("A table named " + output_file + " with the search results has been saved in the current directory.")
articles_df.to_excel(output_file)
