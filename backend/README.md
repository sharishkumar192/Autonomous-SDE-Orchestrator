# ARA Backend Service (Autonomous-SDE-Orchestrator)

The core engine of the multi-agent system, featuring a Supervisor-led orchestration graph, Pydantic-validated agents, and structured logging.

## 📂 Project Structure

```text
backend/
├── graph/                  # Core Orchestration Logic
│   ├── nodes/              # Individual Agent Personas (Supervisor, Coder, etc.)
│   ├── tools/              # Physical I/O actions (File Writer/Reader)
│   ├── schemas.py          # Pydantic models for LLM structured output
│   ├── state.py            # TypedDict definition for Shared Graph State
│   └── workflow.py         # StateGraph compilation and routing logic
├── prompts/                # Markdown-based personas for easy editing
├── utils/                  # Shared utilities (Rich Logging via Loguru)
├── logs/                   # Auto-generated runtime log files
├── main.py                 # FastAPI Gateway entry point
├── pyproject.toml          # Project metadata and dependencies (uv)
└── uv.lock                 # Strict dependency lockfile
````

## 🚀 Local Development Setup

### 1. Environment Setup

We use `uv` for lightning-fast virtual environment and dependency management.

```bash
# Navigate to the backend
cd backend

# Sync the environment (creates .venv and installs deps from uv.lock)
uv sync
```

### 2. Configuration

Create a `.env` file in this directory based on the `.env.example`.

### 3. Usage & Execution

#### Running the API

Start the FastAPI server with hot-reloading for local development:

```bash
uv run uvicorn main:app --reload
```

- **API Gateway:** `http://127.0.0.1:8000`

- **Interactive Documentation:** `http://127.0.0.1:8000/docs`

#### Debugging the Graph

To verify the routing logic and generate a visual flow diagram of the agents:

```bash
uv run python -m graph.workflow
```

_This generates an `architecture_flow.png` in the backend root._

#### Viewing Logs

Runtime logs are color-coded in the terminal and saved to: **[app.log](./backend/logs/app.log)**