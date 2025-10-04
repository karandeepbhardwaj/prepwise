from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.middleware import SlowAPIMiddleware
from backend.config import settings
from backend.api.routes import health, parse, prepare

limiter = Limiter(key_func=get_remote_address, default_limits=[settings.rate_limit])

app = FastAPI(title="PrepWise", description="AI-powered interview preparation guide generator", version="1.0.0")
app.state.limiter = limiter
app.add_middleware(SlowAPIMiddleware)
app.add_middleware(CORSMiddleware, allow_origins=settings.allowed_origins.split(","), allow_methods=["*"], allow_headers=["*"])

app.include_router(health.router)
app.include_router(parse.router)
app.include_router(prepare.router)
