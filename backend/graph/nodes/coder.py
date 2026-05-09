import os
from graph.state import AgentState
from graph.tools.file_tools import write_file

def coder_node(state: AgentState) -> dict:
    print("--- NODE: CODER ---")
    # Logic: The Coder takes the architect_plan and executes tool calls.
    # We simulate a tool call here
    write_file.invoke({"filename": "main.py", "content": "print('Hello World')"})
    
    return {
        "active_files": ["main.py"],
        "next": "Supervisor"
    }