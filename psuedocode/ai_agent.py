# ai_agent.py
# Purpose: Leverage helper files doc_tag/retrieve/organize.py to answer user prompts.

'''
TAG
Tags all unsorted documents in Google Drive.

ORGANIZE
Organizes all documents into respective folders.

RETRIEVE
Retrieves all documents of a specific tag and/or year.

GENERATE X
Generates a document of type X using user-provided prompt.

RESEARCH X
Retrieve all documents relating to user-provided prompt.

TODO: Add more specialized commands for GENERATE/RESEARCH queries

'''

valid_commands = ["TAG", "ORGANIZE", "RETRIEVE", "GENERATE", "RESEARCH"]
def parse_prompt(user_prompt):
    agent_instr = {
                "command": "",
                "instr": ""
                }
    # Query fine-tuned Gemini model with user prompt
    # Get output in the form of (command, instructions)
    return agent_instr

# Use for TAG, ORGANIZE, RETRIEVE commands
def command_agent(command):
    # Run appropiate command using helper.py files
    print("command done")

# Use for GENERATE, RESEARCH commands (tasks which require creative thinking)
def query_agent(command, instr):
    gemini_prompt = gen_gemini_prompt(command, instr)
    # Pass gemini prompt into AI agent and output the appropiate stuff
    print("query completed")

def gen_gemini_prompt(command, instr):
    gemini_prompt = ""
    # Create formatted prompt for Gemini model
    return gemini_prompt