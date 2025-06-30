
# doc_retrieve.py
# Purpose: Retrieve documents based on provided tag and/or year

# TODO: global variable for valid_tags across multiple files?
valid_tags = [
    "Accounting", "Curation", "Development", 
    "Employee Resources", "Board of Directors", "Marketing", 
    "Operations", "Programming", "Research", 
    "Images - Historic", "Images - General"
]

def retrieve_documents(tag: str = "", year: int = 2020):
    current = 2025
    matching = []

    # --- Type Checking ---
    if not isinstance(tag, str):
        print("❌ Tag must be a string.")
        return []
    
    if not isinstance(year, int):
        print("❌ Year must be an integer.")
        return []
    
    if tag not in valid_tags:
        print(f"❌ '{tag}' is not a valid tag. Valid options are:\n{', '.join(valid_tags)}")
        return []
    
    if not (1980 <= year <= current + 1):
        print(f"❌ Year {year} is out of range. Must be between 1980 and {current + 1}.")
        return []

    # --- Simulated File Search ---
    print(f"🔍 Searching for documents tagged '{tag}' from year {year}...")

    # Simulate search (Replace with actual Drive/file system lookup)
    fake_drive = [
        {"name": "budget_2020.pdf", "tag": "Accounting", "year": 2020},
        {"name": "curation_plan_2023.docx", "tag": "Curation", "year": 2023},
        {"name": "staff_memo_2020.pdf", "tag": "Employee Resources", "year": 2020},
    ]

    for file in fake_drive:
        if file["tag"] == tag and file["year"] == year:
            matching.append(file)

    if matching:
        print(f"✅ Found {len(matching)} matching document(s):")
        for doc in matching:
            print(f"📄 {doc['name']} ({doc['tag']}, {doc['year']})")
    else:
        print("❌ No matching documents found.")

    return matching
