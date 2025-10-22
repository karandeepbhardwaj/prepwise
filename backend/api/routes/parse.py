from fastapi import APIRouter, HTTPException
from backend.models.requests import ParseURLRequest
from backend.models.responses import ParseResponse
from backend.services.parser import parse_job_url

router = APIRouter()

@router.post("/api/parse-url", response_model=ParseResponse)
async def parse_url(request: ParseURLRequest):
    try:
        parsed = await parse_job_url(request.url)
        return ParseResponse(title=parsed.title, company=parsed.company, content=parsed.raw_content)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Failed to parse URL: {str(e)}")
