from uvicorn import config
import config_loader as config_loader
import uvicorn
from fastapi import FastAPI
import routes

app = FastAPI(title="Telegram Sender")
app.include_router(routes.router)
app.add_route("send")


if __name__=='__main__':
    uvicorn.run(app, port=config.get(config_loader.WEB_PORT, host=config.get(config_loader.WEB_HOST)))