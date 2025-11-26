from fastapi import APIRouter, HTTPException
from backend.models.requests import PrepareRequest
from backend.models.responses import PrepareResponse
from backend.chains.guide_assembler import assemble_guide
from backend.services.parser import parse_job_url
from backend.services.email_sender import send_guide_email
from backend.services.template_renderer import render_guide_email

router = APIRouter()

@router.post("/api/prepare", response_model=PrepareResponse)
async def prepare_for_interview(request: PrepareRequest):
    try:
        content = request.responsibilities
        company = ""
        title = request.position_title

        if request.job_url:
            parsed = await parse_job_url(request.job_url)
            content = f"{content}\n\n{parsed.raw_content}" if content else parsed.raw_content
            company = parsed.company
            if not title and parsed.title:
                title = parsed.title

        if not title:
            raise HTTPException(status_code=400, detail="Position title is required")
        if not content:
            raise HTTPException(status_code=400, detail="Job description or URL is required")

        guide = await assemble_guide(title=title, content=content, company=company)
        html = render_guide_email(guide)
        await send_guide_email(to=request.email, subject=f"Interview Prep Guide: {title}", html=html)

        return PrepareResponse(success=True, message=f"Guide sent to {request.email}", guide=guide)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to generate guide: {str(e)}")
