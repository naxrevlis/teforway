import config_loader as config_loader
from aiogram import Bot
from fastapi import APIRouter, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

config = config_loader.Config()
router = APIRouter()
bot = Bot(token=config.get(config_loader.TG_TOKEN))


@router.post("/send_message", response_description="Send message")
async def send_message(request: Request, message: str, chat_id: str) -> JSONResponse:
    message = jsonable_encoder(message)
    # TODO: Add security check for message
    try:
        responce = await bot.send_message(chat_id=chat_id, text=message)
        print(responce.text)
        return JSONResponse(status_code=status.HTTP_200_OK, content=message)
    except Exception as e:
        raise JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=str(e))
