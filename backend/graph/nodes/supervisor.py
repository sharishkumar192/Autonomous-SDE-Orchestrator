from langchain_openai import ChatOpenAI
from graph.state import AgentState
from graph.schemas import SupervisorResponse
from utils.logger import log

# Initialize LLM with strict Pydantic output
llm = ChatOpenAI(model="gpt-4o").with_structured_output(SupervisorResponse)

def supervisor_node(state: AgentState) -> dict:
    log.info("Supervisor analyzing project state...")
    
    if state.get("review_count", 0) >= 3:
        log.warning("Loop limit reached. Forcing Finish.")
        return {"next": "FINISH"}

    # Pass the conversation history to the LLM
    response = llm.invoke(state["messages"])
    
    log.success(f"Supervisor Decision: {response.next} | Reasoning: {response.reasoning}")
    return {"next": response.next}