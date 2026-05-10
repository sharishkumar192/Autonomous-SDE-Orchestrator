from pydantic import BaseModel, Field
from typing import List, Literal, Optional

class SupervisorResponse(BaseModel):
    """The brain of the system: Decides who works next."""
    reasoning: str = Field(description="Why this agent was chosen.")
    next: Literal["Architect", "Coder", "Reviewer", "FINISH"]

class ArchitectBlueprint(BaseModel):
    """The technical plan for the project."""
    summary: str = Field(description="High-level overview of the solution.")
    files_to_create: List[str] = Field(description="List of filenames required.")
    libraries: List[str] = Field(description="Third-party packages to install.")
    core_logic: str = Field(description="Detailed logic implementation details.")

class ReviewReport(BaseModel):
    """The quality audit of the code."""
    is_passed: bool = Field(description="True if code is ready for production.")
    bugs: List[str] = Field(description="List of issues found, empty if passed.")
    feedback: str = Field(description="Direct instructions for the Coder to fix issues.")

class RequestBody(BaseModel):
    prompt: str