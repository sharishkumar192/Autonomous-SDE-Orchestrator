import os
from langchain_openai import ChatOpenAI
from langchain_core.messages import AIMessage, SystemMessage
from graph.state import AgentState
from graph.schemas import SupervisorResponse
from utils.logger import log
from tests.mock_engine import get_mock_response

# Initialize LLM with strict Pydantic output
# llm = ChatOpenAI(model="gpt-4o").with_structured_output(SupervisorResponse)

def get_system_prompt() -> str:
    """Reads the supervisor prompt from the markdown file."""
    # Adjust path if your prompts folder is located elsewhere
    prompt_path = os.path.join(os.path.dirname(__file__), "../../prompts/supervisor.md")
    with open(prompt_path, "r") as f:
        return f.read()

def supervisor_node(state: AgentState) -> dict:
    log.info("Supervisor analyzing project state...")
    
    if state.get("review_count", 0) >= 3:
        log.warning("Loop limit reached. Forcing Finish.")
        return {"next": "FINISH"}

    # Pass the conversation history to the LLM
    # response = llm.invoke(state["messages"])

    # --- MOCK LOGIC ---
    mock_data = get_mock_response("supervisor")
    response = SupervisorResponse(**mock_data) # Hydrate Pydantic model
    
    log.success(f"Supervisor Decision: {response.next} | Reasoning: {response.reasoning}")
    
    # Construct state history
    sys_msg = SystemMessage(content=get_system_prompt())
    ai_msg = AIMessage(
        content=f"Decision: Route to {response.next}\nReasoning: {response.reasoning}", 
        name="Supervisor"
    )
    
    return {
        "next": response.next,
        "messages": [sys_msg, ai_msg]
    }