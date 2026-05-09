from langchain_openai import ChatOpenAI
from graph.state import AgentState
from graph.schemas import ArchitectBlueprint
from utils.logger import log

llm = ChatOpenAI(model="gpt-4o").with_structured_output(ArchitectBlueprint)

def architect_node(state: AgentState) -> dict:
    log.info("Architect generating system blueprint...")
    
    # Analyze user requirement from messages
    blueprint = llm.invoke(state["messages"])
    
    log.success(f"Architect produced plan for {len(blueprint.files_to_create)} files.")
    return {
        "architect_plan": blueprint.model_dump_json(), # Store as JSON string in state
        "next": "Supervisor"
    }   