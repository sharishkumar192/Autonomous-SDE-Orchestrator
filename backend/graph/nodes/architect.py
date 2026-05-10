import os
import json
from langchain_openai import ChatOpenAI
from langchain_core.messages import AIMessage, SystemMessage
from graph.state import AgentState
from graph.schemas import ArchitectBlueprint
from utils.logger import log
from tests.mock_engine import get_mock_response

# llm = ChatOpenAI(model="gpt-4o").with_structured_output(ArchitectBlueprint)

def get_system_prompt() -> str:
    prompt_path = os.path.join(os.path.dirname(__file__), "../../prompts/architect.md")
    with open(prompt_path, "r") as f:
        return f.read()

def architect_node(state: AgentState) -> dict:
    log.info("Architect generating system blueprint...")
    
    # --- REAL LLM LOGIC (COMMENTED OUT) ---
    # blueprint = llm.invoke(state["messages"])

    # --- MOCK LOGIC ---
    mock_data = get_mock_response("architect")
    blueprint = ArchitectBlueprint(**mock_data)
    
    log.success(f"Architect produced plan for {len(blueprint.files_to_create)} files.")
    
    # Construct state history
    sys_msg = SystemMessage(content=get_system_prompt())
    ai_msg = AIMessage(
        content=f"Blueprint Generated:\n{json.dumps(blueprint.model_dump(), indent=2)}", 
        name="Architect"
    )
    
    return {
        "architect_plan": blueprint, # Store Pydantic model in state
        "next": "Supervisor",
        "messages": [sys_msg, ai_msg]
    }