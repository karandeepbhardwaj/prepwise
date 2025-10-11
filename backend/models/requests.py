from pydantic import BaseModel, EmailStr

class PrepareRequest(BaseModel):
    position_title: str
    responsibilities: str = ""
    job_url: str | None = None
    email: EmailStr

class ParseURLRequest(BaseModel):
    url: str

class ParsedJobDescription(BaseModel):
    title: str = ""
    company: str = ""
    raw_content: str = ""
