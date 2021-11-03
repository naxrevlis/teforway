import config_loader as config_loader
import uvicorn
from fastapi import FastAPI
from routes import router as sender_router

config = config_loader.Config()

app = FastAPI(title="Telegram Sender")
app.include_router(sender_router, prefix="/api/v1")


if __name__ == "__main__":
    uvicorn.run("main:app", host=config.get(config_loader.WEB_HOST), port=config.get(config_loader.WEB_PORT))
