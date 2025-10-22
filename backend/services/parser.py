import httpx
from bs4 import BeautifulSoup
from backend.models.requests import ParsedJobDescription

async def parse_job_url(url: str) -> ParsedJobDescription:
    async with httpx.AsyncClient(follow_redirects=True, timeout=15.0) as client:
        response = await client.get(url, headers={"User-Agent": "Mozilla/5.0"})
        response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    for element in soup(["script", "style", "nav", "footer", "header"]):
        element.decompose()

    content = _try_selectors(soup) or soup.get_text(separator="\n", strip=True)
    title = _extract_title(soup)
    company = _extract_company(soup)

    return ParsedJobDescription(title=title, company=company, raw_content=content[:5000])

def _try_selectors(soup: BeautifulSoup) -> str | None:
    selectors = [".description__text", ".jobsearch-JobComponent", "#content .body", ".job-description", ".posting-page"]
    for selector in selectors:
        element = soup.select_one(selector)
        if element:
            return element.get_text(separator="\n", strip=True)
    return None

def _extract_title(soup: BeautifulSoup) -> str:
    for selector in [".job-title", "h1", ".posting-headline h2"]:
        el = soup.select_one(selector)
        if el:
            return el.get_text(strip=True)
    return ""

def _extract_company(soup: BeautifulSoup) -> str:
    for selector in [".company-name", ".posting-categories .sort-by-time"]:
        el = soup.select_one(selector)
        if el:
            return el.get_text(strip=True)
    return ""
