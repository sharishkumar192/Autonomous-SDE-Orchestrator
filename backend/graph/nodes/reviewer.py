import os
from graph.state import AgentState

def reviewer_node(state: AgentState) -> dict:
    print("--- NODE: REVIEWER ---")
    
    # Increment the loop guard
    current_reviews = state.get("review_count", 0)
    
    # Logic: Analyze active_files. If bugs found, tell Supervisor to go back to Coder.
    # If perfect, go to FINISH.
    
    return {
        "review_count": current_reviews + 1,
        "next": "Supervisor"
    }