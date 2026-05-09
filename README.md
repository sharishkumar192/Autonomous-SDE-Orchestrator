# Autonomous-SDE-Orchestrator

**Autonomous-SDE-Orchestrator** is a production-grade, multi-agent system built with **LangGraph** and **Python**. It automates the end-to-end Software Development Lifecycle (SDLC) by coordinating specialized AI agents to design, implement, and audit codebases autonomously.

The system utilizes a **Supervisor-led Directed Acyclic Graph (DAG)** to manage complex feedback loops and maintain a persistent "shared memory" of the project state.

---

## 🏗️ System Architecture

The project is built on a "Hub-and-Spoke" model where a central Supervisor orchestrates three specialized sub-agents. Every agent communicates through a shared **State (The Notepad)**, providing a unified source of truth for the entire development process.

### Agent Personas

- **Lead Orchestrator (Supervisor):** The decision-making brain that reviews the current state and routes the workflow to the next appropriate agent using structured JSON output.
    
- **Systems Architect:** Responsible for technical blueprints, defining class structures, API endpoints, and library dependencies.
    
- **Autonomous Coder:** The executioner that utilizes file-system tools to physically write and organize Python files on the local disk.
    
- **Security Reviewer:** The gatekeeper that performs static analysis and provides structured feedback or bug reports if corrections are needed.
    

---

## 📂 Repository Layout

This project is organized as a monorepo to maintain a clear separation of concerns between the orchestration logic and the future user interface:

- **[./backend](./backend):** The core engine. Contains the FastAPI gateway, LangGraph workflow logic, agent nodes, and Pydantic schemas.
    
- **[./frontend](./frontend):** (In Development) The dashboard for real-time monitoring of agent communications and project progress.
  
## 🚀 Quick Start

To set up the orchestrator and run your first autonomous build, follow the detailed technical instructions in the **Backend Manual**:

1. Navigate to the `/backend` directory.
    
2. Follow the setup steps in the **[Backend README.md](./backend/README.md)**.

---

## 🛠️ Security & Governance

This repository enforces strict **Code Ownership** and branch protection rules.

- **Primary Maintainer:** [Harish Kumar Santhanam](https://www.google.com/search?q=https://github.com/sharishkumar192).
    
- **Workflow:** All code contributions require a Pull Request and mandatory approval from the Code Owner before merging.