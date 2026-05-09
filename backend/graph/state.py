from typing import Annotated, Sequence, TypedDict, Optional
from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages
from graph.schemas import ArchitectBlueprint, ReviewReport

class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], add_messages]
    next: str
    review_count: int
    active_files: list[str]
    # Now using structured Pydantic models
    architect_plan: Optional[ArchitectBlueprint]
    latest_review: Optional[ReviewReport]