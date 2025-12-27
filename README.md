# PrepWise

[![CI](https://github.com/karandeepbhardwaj/prepwise/actions/workflows/ci.yml/badge.svg)](https://github.com/karandeepbhardwaj/prepwise/actions/workflows/ci.yml)
[![Python](https://img.shields.io/badge/Python-3.12+-3776AB?logo=python&logoColor=white)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

AI-powered interview preparation guide generator. Enter a job posting, get a comprehensive guide delivered to your inbox.

## Features

- Parse job descriptions from URLs (LinkedIn, Indeed, Greenhouse, Lever)
- AI-generated interview questions (behavioral, technical, situational)
- STAR-method answer frameworks for behavioral questions
- Technical concepts study guide
- Personalized questions to ask the interviewer
- Professional HTML email delivery
- React frontend with real-time progress
- Rate limiting and input validation

## Tech Stack

- **Backend**: Python 3.12, FastAPI, LangChain, Pydantic v2
- **Frontend**: React 19, Vite, TypeScript
- **AI**: OpenAI GPT-4o (via LangChain)
- **Email**: Resend
- **Parsing**: BeautifulSoup4, httpx

## Getting Started

```sh
cp .env.example .env
# Edit .env with your API keys

# Backend
pip install -e .
uvicorn backend.main:app --reload

# Frontend
cd frontend && npm install && npm run dev
```

## Environment Variables

| Variable | Description |
|----------|-------------|
| `OPENAI_API_KEY` | OpenAI API key |
| `RESEND_API_KEY` | Resend API key for email |
| `ALLOWED_ORIGINS` | CORS allowed origins |
| `OPENAI_MODEL` | Model to use (default: gpt-4o) |
| `RATE_LIMIT` | Rate limit per IP (default: 10/minute) |

## API

API docs at http://localhost:8000/docs

## License

MIT
