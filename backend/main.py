import os
from dotenv import load_dotenv

# 1. LOAD ENVIRONMENT
load_dotenv()

# 2. INITIALIZE LOGGING (Must happen before other project imports)
from utils.logger import log

# 3. API KEY SANITY CHECK
if not os.getenv("OPENAI_API_KEY"):
    log.critical("❌ OPENAI_API_KEY missing from environment.")
else:
    log.success("✅ OpenAI API Key loaded successfully.")

# 4. PROJECT IMPORTS
from graph.schemas import RequestBody
from graph.workflow import app as agent_app
from fastapi import FastAPI, HTTPException

app = FastAPI(title="Autonomous SDE Orchestrator")

@app.post("/run")
async def run_orchestrator(request: RequestBody):
    log.info(f"New Request Received: {request.prompt[:50]}...")
    try:
        initial_state = {
            "messages": [("user", request.prompt)],
            "next": "",
            "review_count": 0,
            "active_files": [],
            "architect_plan": ""
        }
        
        final_state = agent_app.invoke(initial_state)
        
        log.success("Workflow completed successfully.")
        return {
            "status": "success",
            "files_created": final_state.get("active_files")
        }
    except Exception as e:
        log.error(f"Workflow Failed: {str(e)}")
        raise HTTPException(status_code=500, detail="Orchestration Error")