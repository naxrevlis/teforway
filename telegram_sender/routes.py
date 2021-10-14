from typing import Dict
from fastapi import APIRouter
import config_loader as config_loader
import random


config = config_loader.Config()

router = APIRouter()


@router.post("/", tags=["send"])
async def send_message(message: str) -> Dict:
    return {
        "status_code": 200,
        "message": message
        }