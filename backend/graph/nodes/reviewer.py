import os
from langchain_core.messages import AIMessage, SystemMessage
from graph.state import AgentState
from graph.schemas import ReviewReport
from tests.mock_engine import get_mock_response
from utils.logger import log

def get_system_prompt() -> str:
    prompt_path = os.path.join(os.path.dirname(__file__), "../../prompts/reviewer.md")
    with open(prompt_path, "r") as f:
        return f.read()

def reviewer_node(state: AgentState) -> dict:
    print("--- NODE: REVIEWER ---")
    
    # Increment the loop guard
    current_reviews = state.get("review_count", 0)
    
    # --- REAL LOGIC (COMMENTED OUT) ---
    # Logic: Analyze active_files. If bugs found, tell Supervisor to go back to Coder.
    # If perfect, go to FINISH.
    
    # --- MOCK LOGIC ---
    mock_data = get_mock_response("reviewer")
    report = ReviewReport(**mock_data)
    
    log.info(f"Review passed? {report.is_passed} | Bugs: {report.bugs}")
    
    # Construct state history
    sys_msg = SystemMessage(content=get_system_prompt())
    
    # Format a readable response for the message history
    review_status = "PASSED" if report.is_passed else "FAILED"
    ai_content = f"Status: {review_status}\nFeedback: {report.feedback}\nBugs Found: {', '.join(report.bugs) if report.bugs else 'None'}"
    ai_msg = AIMessage(content=ai_content, name="Reviewer")
    
    return {
        "review_count": current_reviews + 1,
        "latest_review": report, 
        "next": "Supervisor",
        "messages": [sys_msg, ai_msg]
    }