#-------------------------------------------------------------------------
# AUTHOR: Ryan Hoang
# FILENAME: index.py
# SPECIFICATION: Create inverted index from the following a document collection
#                and print the result in the given format
# FOR: CS 4250 - Assignment #1
# TIME SPENT: 45 minutes
#-------------------------------------------------------------------------

# Importing Python libraries
import pandas as pd
import string

# Reading the document collection
data = pd.read_csv("collection.csv")

# Defining the dictionary used for lemmatization
# --> add your Python code here
lemmas = {
    "homes" : "home",
    "home" : "home",
    "sales" : "sale",
    "sale" : "sale",
    "increases" : "increase",
    "increasing" : "increase",
    "increased" : "increase",
    "increase" : "increase",
    "rising" : "rise",
    "rises" : "rise",
    "rose" : "rise",
    "rise" : "rise"
}

# Creating the data structure that will store the inverted index
invertedIndex = {}

# Processing each document in the collection
for i, row in data.iterrows():

    docID = row["Document"]
    text = row["Text"]

    # Applying surface-level normalization
    # --> add your Python code here
    normalized_text = text.lower()
    normalized_text = normalized_text.translate(str.maketrans('', '', string.punctuation))

    # Tokenizing the document
    # --> add your Python code here
    tokens = normalized_text.split()

    # Applying lemmatization
    # --> add your Python code here
    lemmatized_text = [lemmas.get(token, token) for token in tokens]

    # Building the inverted index
    # --> add your Python code here
    for term in lemmatized_text:
        if term not in invertedIndex:
            invertedIndex[term] = set()
        invertedIndex[term].add(docID)


# Printing the inverted index with terms ordered alphabetically
# Expected format:
# term1 : ['Doc1', 'Doc2']
# term2 : ['Doc3']
# --> add your Python code here
for term in sorted(invertedIndex.keys()):
    print(f"{term}: {invertedIndex[term]}")