from pydantic import BaseModel
from backend.models.guide import PrepGuide

class PrepareResponse(BaseModel):
    success: bool
    message: str
    guide: PrepGuide | None = None

class ParseResponse(BaseModel):
    title: str
    company: str
    content: str
