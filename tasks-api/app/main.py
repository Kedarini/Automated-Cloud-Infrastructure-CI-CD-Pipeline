from app.api.routes import tasks
from app.core.config import get_settings
from fastapi import FastAPI

settings = get_settings()
app = FastAPI(title=settings.app_name, debug=settings.debug)

app.include_router(tasks.router, prefix="/tasks", tags=["tasks"])


@app.get("/health")
async def health() -> dict:
    return {"status": "ok"}
