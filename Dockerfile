FROM python:3.12-slim AS backend
WORKDIR /app
COPY pyproject.toml .
RUN pip install --no-cache-dir .
COPY backend/ backend/

FROM node:20-alpine AS frontend
WORKDIR /app/frontend
COPY frontend/package.json .
RUN npm ci
COPY frontend/ .
RUN npm run build

FROM python:3.12-slim
WORKDIR /app
COPY --from=backend /app .
COPY --from=frontend /app/frontend/dist ./frontend/dist
RUN pip install --no-cache-dir .
EXPOSE 8000
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]
