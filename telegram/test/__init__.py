#!/bin/python3

from boolpy.telegram.api import (logger,
                                 NextManager,
                                 TelegramError)
import os
import time
import asyncio

from boolpy.telegram import Client
from boolpy.telegram.types import *
from boolpy.json_manager import JsonManager
from typing import Any, Optional, List, Union

markdown_escapes = {
    '_':'\_',
    '*':'\*',
    '[':'\[',
    ']':'\]',
    '(':'\(',
    ')':'\)',
    '~':'\~',
    '`':'\`',
    '>':'\>',
    '#':'\#',
    '+':'\+',
    '-':'\-',
    '=':'\=',
    '|':'\|',
    '{':'\{',
    '}':'\}',
    '.':'\.',
    '!':'\!'
}

def restart_tor():
    if os.system('service tor status') == 0:
        return os.system('sudo service tor restart')

track_error = """\
Parameter 'track' must be None or a JsonManager instance, got %s"""

delete_history_error = """\
To delete history, class attribute 'track' cannot be None."""

class Test(Client):
    def __init__(
        self,
        token: str,
        proxy: Optional[str] = None,
        track: Optional[JsonManager] = None,
        parse_mode: Optional[str] = None,
        protect_content: Optional[bool] = None
    ):
        if (track is not None
            and type(track) is not JsonManager):

            raise TypeError(track_error % track.__class__.__name__)

        self.track = track

        super().__init__(token,
                         proxy,
                         parse_mode,
                         protect_content)


    def track_message(self, message: Message) -> dict:
        cid = message.chat.id
        mid = message.message_id
        data = self.track.get(cid)
        data['mid'] += [mid]
        if not data['time']:
            data['time'] = time.time()

        return data
 

    async def send_message(
        self, chat_id: int | str, text: str, message_thread_id: int | None = None, parse_mode: str | None = None, entities: List[MessageEntity] | None = None,
        disable_web_page_preview: bool | None = None, disable_notification: bool | None = None, protect_content: bool | None = None, reply_to_message_id: int | None = None,
        allow_sending_without_reply: bool | None = None, reply_markup: InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply | None = None,
        track: bool=True
    ) -> Message:
        message = await super().send_message(
            chat_id, text, message_thread_id, parse_mode, entities, disable_web_page_preview,
            disable_notification, protect_content, reply_to_message_id, allow_sending_without_reply, reply_markup
        )
        if type(message) is Message:
            if self.track is not None and track is True:
                self.track_message(message)
        return message

    async def delete_history(self, cid: Union[int, str]) -> int:

        if self.track is None:
            raise TypeError(delete_history_error)

        data = self.track.get(cid)
        messages_history = data['mid']
        data.update({'mid': [], 'time': None, 'query': None})

        deleted = 0
        try:
            for mid in messages_history:
                try:
                    await super().delete_message(cid, mid)
                    deleted += 1

                except TelegramError:
                    pass

                await asyncio.sleep(1)

        except:
            restored_data = self.track.get(cid)
            restored_data['mid'] += messages_history
            self.track.updates[cid] = restored_data
            logger.warning(f'{cid} history deletion was'
                           + ' interrupted. Json was restored.')
            raise

        return deleted



    async def check_mids(self,
                         my_id: Union[int, str],
                         hours_to_sleep: int = 3) -> None:
        while True:
            start_time = time.time()
            users = self.track.merge()
            text = ""
            for cid in users:
                data = users[cid]
                if 'time' in data and data['time']:
                    usr = data['usr']
                    first_log = data['time']
                    remaining_hours = 48 - (round((start_time-first_log) / 3600))
                    if remaining_hours <= 12:
                        if remaining_hours == 1:
                            text += '{} hours'.format(remaining_hours)
                        else:
                            remaining_min = 2880 - (round((start_time-first_log) / 60))
                            text += '{} minutes'.format(remaining_min)
                        text += f" to clean {usr}'s chat 📝️\n"
            if text: await self.send_message(my_id, text)
            diff_time = time.time()-start_time
            await asyncio.sleep(3600*hours_to_sleep-diff_time)
