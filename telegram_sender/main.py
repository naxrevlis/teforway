import config_loader as config_loader
import routes
import uvicorn
from fastapi import FastAPI
from uvicorn import config

app = FastAPI(title="Telegram Sender")
app.include_router(routes.router)


if __name__ == "__main__":
    uvicorn.run(app, port=config.get(config_loader.WEB_PORT, host=config.get(config_loader.WEB_HOST)))
