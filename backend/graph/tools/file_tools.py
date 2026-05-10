import os
from langchain_core.tools import tool

# Safety check: Define a workspace directory so the AI doesn't touch your system files
WORKSPACE_DIR = os.path.join(os.getcwd(), "output_repo")
if not os.path.exists(WORKSPACE_DIR):
    os.makedirs(WORKSPACE_DIR)

@tool
def write_file(filename: str, content: str):
    """Writes or overwrites a file with specific content in the workspace."""
    filepath = os.path.join(WORKSPACE_DIR, filename)
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w") as f:
        f.write(content)
    return f"Successfully wrote to {filename}"

@tool
def read_file(filename: str):
    """Reads the content of a file from the workspace."""
    filepath = os.path.join(WORKSPACE_DIR, filename)
    if not os.path.exists(filepath):
        return f"Error: {filename} not found."
    with open(filepath, "r") as f:
        return f.read()

@tool
def delete_file(filename: str):
    """Deletes a file from the workspace."""
    filepath = os.path.join(WORKSPACE_DIR, filename)
    if os.path.exists(filepath):
        os.remove(filepath)
        return f"Successfully deleted {filename}"
    return f"Error: {filename} does not exist."

@tool
def update_file(filename: str, old_content: str, new_content: str):
    """Updates a specific part of a file by replacing old_content with new_content."""
    filepath = os.path.join(WORKSPACE_DIR, filename)
    if not os.path.exists(filepath):
        return f"Error: {filename} not found."
    
    with open(filepath, "r") as f:
        content = f.read()
        
    if old_content not in content:
        return f"Error: Exact old_content string not found in {filename}."
        
    updated_content = content.replace(old_content, new_content)
    
    with open(filepath, "w") as f:
        f.write(updated_content)
        
    return f"Successfully updated {filename}"