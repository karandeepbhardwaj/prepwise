from backend.chains.guide_assembler import assemble_guide

async def generate_guide(title: str, content: str, company: str = ""):
    return await assemble_guide(title=title, content=content, company=company)
