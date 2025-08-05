from pydantic import BaseModel
from typing import Optional


class StoryRequest(BaseModel):
    genre: str
    characters: str  # comma-separated names or description
    sections: int  # number of paragraphs


class StoryResponse(BaseModel):
    summary: str
    paragraphs: list[str]
    images: Optional[list[str]] = None
