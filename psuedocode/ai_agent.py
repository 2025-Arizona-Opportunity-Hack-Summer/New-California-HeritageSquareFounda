# ai_agent.py

valid_commands = ["TAG", "ORGANIZE", "RETRIEVE", "GENERATE", "RESEARCH"]

from doc_tag import tag_documents
from doc_organize import organize_documents
from doc_retrieve import retrieve_documents

def parse_prompt(user_prompt):
    agent_instr = {
        "command": "",
        "instr": ""
    }

    for cmd in valid_commands:
        if cmd in user_prompt.upper():
            agent_instr["command"] = cmd
            agent_instr["instr"] = user_prompt.upper().replace(cmd, "", 1).strip()
            break

    return agent_instr

def command_agent(command, instr):
    if command == "TAG":
        tag_documents()
    elif command == "ORGANIZE":
        organize_documents()
    elif command == "RETRIEVE":
        # Example input parsing from user instructions (like "tag=Accounting year=2020")
        parts = instr.split()
        tag = ""
        year = 2020
        for part in parts:
            if part.lower().startswith("tag="):
                tag = part.split("=")[1]
            elif part.lower().startswith("year="):
                try:
                    year = int(part.split("=")[1])
                except:
                    pass
        retrieve_documents(tag, year)
    else:
        print("❌ Unsupported command for command_agent.")
    print(f"✅ {command} command executed.")

def query_agent(command, instr):
    gemini_prompt = gen_gemini_prompt(command, instr)
    # Here you would send gemini_prompt to an actual LLM or Gemini API
    # For now, simulate response
    fake_response = f"🧠 Simulated Gemini response for {command}: {instr}"
    print(fake_response)
    print("✅ query completed.")

def gen_gemini_prompt(command, instr):
    return f"Perform a {command} operation with these instructions:\n{instr}"

def main(user_prompt):
    parsed = parse_prompt(user_prompt)
    command = parsed["command"]
    instr = parsed["instr"]

    if command in ["TAG", "ORGANIZE", "RETRIEVE"]:
        command_agent(command, instr)
    elif command in ["GENERATE", "RESEARCH"]:
        query_agent(command, instr)
    else:
        print("❌ Invalid command. Try TAG, ORGANIZE, RETRIEVE, GENERATE, or RESEARCH.")

if __name__ == "__main__":
    with open("summary.txt", "r") as f:
        user_input = f.read().strip()
    print(f"📝 Loaded input from summary.txt:\n{user_input}\n")
    main(user_input)
