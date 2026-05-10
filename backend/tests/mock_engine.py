import json
import os
from utils.logger import log

def get_mock_response(node_name: str) -> dict:
    """Reads the mock JSON and pops the next response for the given agent."""
    mock_file = "tests/mock_data.json"
    
    if not os.path.exists(mock_file):
        log.error(f"Mock file not found at {mock_file}")
        return {}

    with open(mock_file, "r") as f:
        data = json.load(f)

    agent_key = node_name.lower()
    if agent_key in data and len(data[agent_key]) > 0:
        response = data[agent_key].pop(0)
        
        # Write back to the file so the next node run gets the updated queue
        with open(mock_file, "w") as f:
            json.dump(data, f, indent=2)
            
        return response
    
    log.error(f"No mock data left in queue for {node_name}!")
    return {}