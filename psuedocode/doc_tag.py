# doc_tag.py
# Purpose: Assign appropiate tag to a document in Google Drive.


# REFERENCE: https://developers.google.com/workspace/drive/api/guides/search-files
# Fetch each untagged document from Google Drive API

documents = []
untagged = []
untagged_lst = []

'''
Development - contributed revenue gen
Employee Resources - HR 
'''
valid_tags = ["Accounting", "Curation", "Development", 
              "Employee Resources", "Board of Directors", "Marketing", 
              "Operations", "Programming", "Research", 
              "Images - Historic", "Images - General"]


# Filter documents for untagged elements
for file in documents:
    # if file does not have tag
    untagged.append(file)

# REFERENCE: https://ai.google.dev/api?lang=python
# Determine the appropiate tag for the document using Google Gemini API

for file in untagged:
    # Call Gemini API with prompt + document contents OR attaching actual document (RAG)
    # relevant_tag = Gemini API output
    # check that relevant_tag is in valid_tags
    # if success, continue as normal
    # if fail, print error msg and attempt to retag document
    # file.tag(relevant_tag)
    # untagged_lst.append(file.name)
    print("tagging done")

# Pass list of now tagged documents into doc_organize.py

