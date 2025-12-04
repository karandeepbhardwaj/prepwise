from jinja2 import Environment, FileSystemLoader
from backend.models.guide import PrepGuide

env = Environment(loader=FileSystemLoader("backend/templates"))

def render_guide_email(guide: PrepGuide) -> str:
    template = env.get_template("email_guide.html")
    return template.render(guide=guide)
