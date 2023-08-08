from aiogram.types import Message
from aiogram.filters import BaseFilter
from data.config import ADMINS

class IsAdmin(BaseFilter):
    
    def __init__(self) -> None:
        self.admins = ADMINS
        
    async def __call__(self, message: Message) -> bool:
        cid: str = message.from_user.id
        return cid in self.admins
