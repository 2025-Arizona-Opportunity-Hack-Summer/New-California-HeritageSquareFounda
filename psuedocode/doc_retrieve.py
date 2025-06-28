# doc_retrieve.py
# Purpose: Retrieve documents based on provided tag and/or keyword

# TODO: global variable for valid_tags across multiple files?
# imported from doc_tag.py
valid_tags = ["Accounting", "Curation", "Development", 
              "Employee Resources", "Board of Directors", "Marketing", 
              "Operations", "Programming", "Research", 
              "Images - Historic", "Images - General"]

# Input: tag, year
# Output: list of document names and locations tagged with the appropiate tag and date
tag = ""
year = 2020

# Type checking for inputs

# Check type of tag var
if not isinstance(tag, str):
    # return and ask user to reprompt with appropiate tag
    print("tag is not of type str")
# Check type of year var
if not isinstance(year, int):
    # return and ask user to reprompt with appropiate year
    print("year is not of type int")

# Check if input tag is a valid tag
if tag not in valid_tags:
    # return and ask user to reprompt with appropiate tag
    print("tag not in valid_tags")

# Get current year
current = 2025

# Check if year is in the valid range (1980-Current). 
# current+1 allows for future year planning.
if not 1980 <= year <= current+1:
    # return and ask user to reprompt with appropiate year
    print(f"year is not in valid range 1980 - {current+1}")

# Provided inputs are valid and we can now retrieve documents
matching = [] # output

# Navigate to appropiate folder
target_folder = []
# target_folder = drive.find(tag)

# Check if each document in the target folder meets year criteria
for file in target_folder:
    # if file.year == year:
    # matching.append(file)
    print("file fetching")

# return matching
# TODO: Link doc_retrieve.py with AI agent command so it can retrieve files upon a query.




