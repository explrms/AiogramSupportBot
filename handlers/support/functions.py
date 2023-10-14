from aiogram import types
from pydantic import BaseModel

from config import SUPPORT_CHAT_ID
from db_logic.base import SupportTickets
from loader import dp


class SupportRequest(BaseModel):
    user_id: int
    username: str | None
    message_id: int

    async def send_support_request(self):
        _close_support_request_kb = types.InlineKeyboardMarkup()
        _close_support_request_kb.add(
            types.InlineKeyboardButton(
                text="Закрыть тикет", callback_data="close_ticket"
            )
        )
        message_thread_id = await self._create_forum_topic()
        await dp.bot.send_message(
            chat_id=SUPPORT_CHAT_ID,
            message_thread_id=message_thread_id,
            text=f"Новое обращение в тех. поддержку от пользователя {self.user_id} @{self.username}",
            reply_markup=_close_support_request_kb,
        )
        await dp.bot.forward_message(
            chat_id=SUPPORT_CHAT_ID,
            message_thread_id=message_thread_id,
            from_chat_id=self.user_id,
            message_id=self.message_id,
        )
        SupportTickets().create_ticket(self.user_id, message_thread_id)

    async def _create_forum_topic(self):
        return (
            await dp.bot.create_forum_topic(
                chat_id=SUPPORT_CHAT_ID,
                name=f"Заявка от {self.username or self.user_id}",
            )
        ).message_thread_id
