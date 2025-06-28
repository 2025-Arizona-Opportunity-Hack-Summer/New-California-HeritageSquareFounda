# doc_organize.py
# Purpose: Organize documents into respective Google Drive folders based on tag.

# TODO: import from doc_tag.py
untagged = []
untagged_lst = []
valid_tags = []

# reassign var names for clarity
just_tagged = untagged # paths to just tagged files
just_tagged_lst = untagged_lst # names of just tagged files

# REFERENCE: https://developers.google.com/workspace/drive/api/guides/folder#create-folder
# Check that an associated folder exists for each tag
for tag in valid_tags:
    # if tag is not in Google Drive:
    #   folder.create(tag)
    print("tag folder checked")

# Add each just tagged file to its respective folder
for file in just_tagged:
    # target_folder = drive.find(file.tag)
    # target_folder.add(file)
    print("added file")

print("Organization complete")

# TODO: Link doc_organize.py with AI agent command so it can automatically organize all files every X days.