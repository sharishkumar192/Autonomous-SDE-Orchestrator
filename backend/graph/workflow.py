from langgraph.graph import StateGraph, START, END
from graph.state import AgentState
from graph.nodes.supervisor import supervisor_node
from graph.nodes.architect import architect_node
from graph.nodes.coder import coder_node
from graph.nodes.reviewer import reviewer_node

def build_graph():
    workflow = StateGraph(AgentState)
    
    # Add actual nodes
    workflow.add_node("Supervisor", supervisor_node)
    workflow.add_node("Architect", architect_node)
    workflow.add_node("Coder", coder_node)
    workflow.add_node("Reviewer", reviewer_node)
    
    # Define edges (unchanged)
    workflow.add_edge(START, "Supervisor")
    
    workflow.add_conditional_edges(
        "Supervisor",
        lambda x: x["next"],
        {
            "Architect": "Architect",
            "Coder": "Coder",
            "Reviewer": "Reviewer",
            "FINISH": END
        }
    )
    
    workflow.add_edge("Architect", "Supervisor")
    workflow.add_edge("Coder", "Supervisor")
    workflow.add_edge("Reviewer", "Supervisor")
    
    return workflow.compile()

def save_graph_image(app, filename="architecture_flow.png"):
    """Generates a visual PNG of the LangGraph state machine."""
    try:
        png_bytes = app.get_graph().draw_mermaid_png()
        with open(filename, "wb") as f:
            f.write(png_bytes)
        print(f"Graph visualization successfully saved to {filename}")
    except Exception as e:
        print(f"Failed to generate graph image. Ensure you have network access (uses Mermaid API). Error: {e}")

# Instantiate the app
app = build_graph()

# Generate the image when this file is executed directly
if __name__ == "__main__":
    save_graph_image(app)