def test_extract_title():
    from backend.services.parser import _extract_title
    from bs4 import BeautifulSoup
    html = "<html><body><h1>Senior Engineer</h1></body></html>"
    soup = BeautifulSoup(html, "html.parser")
    assert _extract_title(soup) == "Senior Engineer"
