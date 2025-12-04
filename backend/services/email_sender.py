import resend
from backend.config import settings

async def send_guide_email(to: str, subject: str, html: str) -> dict:
    resend.api_key = settings.resend_api_key
    params = resend.Emails.SendParams(from_="PrepWise <noreply@prepwise.dev>", to=[to], subject=subject, html=html)
    return resend.Emails.send(params)
