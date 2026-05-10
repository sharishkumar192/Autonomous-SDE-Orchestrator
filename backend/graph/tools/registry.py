from utils.enums import ToolName
from graph.tools.file_tools import write_file, update_file, read_file, delete_file

# ---------------------------------------------------------
# Global Tool Registry
# Any node in the graph can import this to dynamically execute tools.
# ---------------------------------------------------------
TOOL_REGISTRY = {
    ToolName.WRITE_FILE: write_file,
    ToolName.UPDATE_FILE: update_file,
    ToolName.READ_FILE: read_file,
    ToolName.DELETE_FILE: delete_file
}

def get_tool(tool_name: ToolName):
    """Safely fetch a tool from the registry."""
    return TOOL_REGISTRY.get(tool_name)