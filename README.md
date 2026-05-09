# Autonomous-SDE-Orchestrator

**Autonomous-SDE-Orchestrator** is a production-grade, multi-agent system built with **LangGraph** and **Python**. It automates the end-to-end Software Development Lifecycle (SDLC) by coordinating specialized AI agents to design, implement, and audit codebases autonomously.

The system moves beyond simple linear chains, utilizing a **Supervisor-led Directed Acyclic Graph (DAG)** to manage complex feedback loops and maintain a persistent "shared memory" of the project state.

---

## 🏗️ System Architecture

The project is built on a "Hub-and-Spoke" model where a central Supervisor orchestrates three specialized sub-agents. Every agent communicates through a shared **State (The Notepad)**, which is persisted to a database after every transition.

### Agent Personas
*   **Lead Orchestrator (Supervisor):** The decision-making brain. It reviews the current state and routes the workflow to the next appropriate agent using structured JSON output.
*   **Systems Architect:** Responsible for technical blueprints. It defines class structures, API endpoints, and library dependencies in Markdown format.
*   **Autonomous Coder:** The executioner. It utilizes a suite of **File-System Tools** to physically write, update, and organize Python files on the local disk.
*   **Security Reviewer:** The auditor. It reads the physical files, performs static analysis, and provides a structured "Bug Report" back to the Supervisor if corrections are needed.



---

## ⚙️ Key Engineering Features

*   **Atomic State Persistence:** Integrated with **PostgreSQL Checkpointing**. The system can be interrupted or crash mid-execution and "hydrate" back to the exact state without re-running previous agent calls.
*   **Iterative Self-Correction Loop:** Implements a sophisticated feedback loop between the Coder and Reviewer. The system autonomously fixes its own bugs before delivering the final code.
*   **Infinite-Loop Protection:** A state-managed `review_count` variable acts as a circuit breaker, preventing expensive and infinite feedback loops between agents.
*   **Structured Tool Calling:** Uses Pydantic-validated models to ensure agents interact with the file system safely and predictably.
*   **Persona Decoupling:** Agent instructions are stored in external `.md` files, allowing for rapid iteration on agent "logic" without touching the core orchestration code.

---

## 📂 Project Directory Structure

```text
backend/
├── main.py                 # FastAPI Gateway entry point
├── graph/
│   ├── state.py            # TypedDict definition (The Shared Notepad)
│   ├── workflow.py         # LangGraph Graph compilation & Routing logic
│   ├── nodes/              # Individual Agent logic and API wrappers
│   │   ├── supervisor.py
│   │   ├── architect.py
│   │   ├── coder.py
│   │   └── reviewer.py
│   └── tools/              # Physical I/O Python functions
│       ├── file_writer.py
│       └── file_reader.py
├── prompts/                # External Agent Personas (Markdown)
│   ├── supervisor.md
│   ├── architect.md
│   ├── coder.md
│   └── reviewer.md
├── database/               # Postgres Persistence & Checkpointer setup
├── requirements.txt
└── .env.example            # Environment configuration
