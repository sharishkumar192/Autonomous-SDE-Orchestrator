from enum import Enum

class ToolName(str, Enum):
    """Enumeration of all available LangGraph tools."""
    WRITE_FILE = "write_file"
    READ_FILE = "read_file"
    UPDATE_FILE = "update_file"
    DELETE_FILE = "delete_file"