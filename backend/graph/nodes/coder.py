import os
from langchain_core.messages import AIMessage, SystemMessage
from graph.state import AgentState
from tests.mock_engine import get_mock_response
from utils.logger import log 
from utils.enums import ToolName
from graph.tools.registry import get_tool

def get_system_prompt() -> str:
    prompt_path = os.path.join(os.path.dirname(__file__), "../../prompts/coder.md")
    with open(prompt_path, "r") as f:
        return f.read()

def coder_node(state: AgentState) -> dict:
    log.info("--- NODE: CODER ---")
        
    # --- REAL LOGIC (COMMENTED OUT) ---
    # Logic: The Coder takes the architect_plan and executes tool calls.
    # write_file.invoke({"filename": "main.py", "content": "print('Hello World')"})
    
    # --- MOCK LOGIC ---
    mock_data = get_mock_response("coder")
    
    # 1. Execute simulated tool calls dynamically
    tool_calls = mock_data.get("tool_calls", [])
    for call in tool_calls:
        raw_tool_name = call.get("tool")
        args = call.get("args", {})
        
        try:
            tool_enum = ToolName(raw_tool_name)
            target_tool = get_tool(tool_enum) # <-- Decoupled fetch
            
            if target_tool:
                target_tool.invoke(args)
                log.info(f"🛠️ Tool Executed: {tool_enum.value} -> {args.get('filename', 'Unknown File')}")
            else:
                log.error(f"❌ Tool registered in Enum but missing from Registry: {tool_enum.value}")
                
        except ValueError:
            log.warning(f"⚠️ Unknown tool requested and ignored: {raw_tool_name}")
            
    # 2. Append to LangChain Message State
    message_content = mock_data.get("message", "Executed tools based on blueprint.")
    
    sys_msg = SystemMessage(content=get_system_prompt())
    ai_msg = AIMessage(content=message_content, name="Coder")
            
    return {
        "messages": [sys_msg, ai_msg],
        "active_files": state.get("active_files", []) + mock_data.get("files_created", []),
        "next": "Supervisor"
    }