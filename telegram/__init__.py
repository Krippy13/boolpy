#!/bin/python3

from boolpy.telegram.api import (logger,
                                 TelegramApi,
                                 NextManager,
                                 TelegramError)
import asyncio
from aiohttp import ClientError
from boolpy.telegram.types import *
from typing import Any, Optional, List, Union

# $ # $ # $ # $ # $ # $ # $ # $ # $

class Client(TelegramApi):
    def __init__(
        self,
        token: str,
        proxy: Optional[str] = None,
        parse_mode: Optional[str] = None,
        protect_content: Optional[bool] = None
    ):
        super().__init__(token, proxy)

        self.parse_mode = parse_mode
        self.protect_content = protect_content

        self.offset = None
        self._message_managers = []
        self._edited_message_managers = []
        self._channel_post_managers = []
        self._edited_channel_post_managers = []
        self._callback_query_managers = []
        self._inline_query_managers = []
        self._chosen_inline_result_managers = []
        self._shipping_query_managers = []
        self._pre_checkout_query_managers = []
        self._poll_managers = []
        self._poll_answer_managers = []
        self._my_chat_member_managers = []
        self._chat_member_managers = []
        self._chat_join_request_managers = []

    async def get_updates(
        self, offset: Optional[int] = None, limit: Optional[int] = None,
        timeout: Optional[int] = None, allowed_updates: Optional[List[str]] = None
    ) -> List[Update]:
        params={}
        if offset is not None: params['offset'] = offset
        if limit is not None: params['limit'] = limit
        if timeout is not None: params['timeout'] = timeout
        if allowed_updates is not None: params['allowed_updates'] = allowed_updates
        result = await super().get_updates(params)
        return [Update.dese(update) for update in result]

    async def log_out(self) -> True:
        result = await super().log_out()
        return result

    async def close(self) -> True:
        result = await super().close()
        return result

    async def get_me(self) -> User:
        result = await super().get_me()
        return User.dese(result)

    async def delete_message(self, chat_id: Union[int, str], message_id: int) -> True:
        params = {}
        params['chat_id'] = chat_id
        params['message_id'] = message_id
        result = await super().delete_message(params)
        return result

    async def send_message(
        self, chat_id: Union[int, str], text: str, message_thread_id: Optional[int] = None,
        parse_mode: Optional[str] = None, entities: Optional[List[MessageEntity]] = None, disable_web_page_preview: Optional[bool] = None,
        disable_notification: Optional[bool] = None, protect_content: Optional[bool] = None, reply_to_message_id: Optional[int] = None,
        allow_sending_without_reply: Optional[bool] = None, reply_markup:  Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply, None] = None
    ) -> Message:
        params={}
        params['chat_id'] = chat_id
        params['text'] = text
        if message_thread_id is not None: params['message_thread_id'] = message_thread_id
        if parse_mode is not None: params['parse_mode'] = parse_mode
        if entities is not None: params['entities'] = entities
        if disable_web_page_preview is not None: params['disable_web_page_preview'] = disable_web_page_preview
        if disable_notification is not None: params['disable_notification'] = disable_notification
        if protect_content is not None: params['protect_content'] = protect_content
        if reply_to_message_id is not None: params['reply_to_message_id'] = reply_to_message_id
        if allow_sending_without_reply is not None: params['allow_sending_without_reply'] = allow_sending_without_reply
        if reply_markup is not None: params['reply_markup'] = reply_markup
        result = await super().send_message(params)
        return Message.dese(result)

    async def forward_message(
        self, chat_id: Union[int, str], from_chat_id: Union[int, str], message_id: int,
        message_thread_id: Optional[int] = None, disable_notification: Optional[bool] = None, protect_content: Optional[bool] = None
    ) -> Message:
        params = {}
        params['chat_id'] = chat_id
        params['from_chat_id'] = from_chat_id
        params['message_id'] = message_id
        if message_thread_id is not None: params['message_thread_id'] = message_thread_id
        if disable_notification is not None: params['disable_notification'] = disable_notification
        if protect_content is not None: params['protect_content'] = protect_content
        result = await super().forward_message(params)
        return Message.dese(result)

    async def copy_message(
        self, chat_id: Union[int, str], from_chat_id: Union[int, str], message_id: int,
        message_thread_id: Optional[int] = None, caption: Optional[str] = None,
        parse_mode: Optional[str] = None, caption_entities: Optional[List[MessageEntity]] = None,
        disable_notification: Optional[bool] = None, protect_content: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None, allow_sending_without_reply: Optional[bool] = None,
        reply_markup: Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply, None] = None
    ) -> MessageId:
        params = {}
        params['chat_id'] = chat_id
        params['from_chat_id'] = from_chat_id
        params['message_id'] = message_id
        if message_thread_id is not None: params['message_thread_id'] = message_thread_id
        if caption is not None: params['caption'] = caption
        if parse_mode is not None: params['parse_mode'] = parse_mode
        if caption_entities is not None: params['caption_entities'] = caption_entities
        if disable_notification is not None: params['disable_notification'] = disable_notification
        if protect_content is not None: params['protect_content'] = protect_content
        if reply_to_message_id is not None: params['reply_to_message_id'] = reply_to_message_id
        if allow_sending_without_reply is not None: params['allow_sending_without_reply'] = allow_sending_without_reply
        if reply_markup is not None: params['reply_markup'] = reply_markup
        result = await super().copy_message(params)
        return MessageId.dese(result)

    async def send_photo(
        self, chat_id: int|str, photo: InputFile|str, message_thread_id: int|None=None,
        caption: str|None=None, parse_mode: str|None=None, caption_entities: List[MessageEntity]|None=None,
        has_spoiler: bool|None=None, disable_notification: bool|None=None, protect_content: bool|None=None,
        reply_to_message_id: bool|None=None, allow_sending_without_reply: bool|None=None,
        reply_markup: Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply, None]=None
    ) -> Message:
        params = {}
        params['chat_id'] = chat_id
        params['photo'] = photo
        if message_thread_id is not None: params['message_thread_id'] = message_thread_id
        if caption is not None: params['caption'] = caption
        if parse_mode is not None: params['parse_mode'] = parse_mode
        if caption_entities is not None: params['caption_entities'] = caption_entities
        if has_spoiler is not None: params['has_spoiler'] = has_spoiler
        if disable_notification is not None: params['disable_notification'] = disable_notification
        if protect_content is not None: params['protect_content'] = protect_content
        if reply_to_message_id is not None: params['reply_to_message_id'] = reply_to_message_id
        if allow_sending_without_reply is not None: params['allow_sending_without_reply'] = allow_sending_without_reply
        if reply_markup is not None: params['reply_markup'] = reply_markup
        result = await super().send_photo(params)
        return Message.dese(result)

    async def send_audio(
        self, chat_id: int|str, audio: InputFile|str, message_thread_id: int|None=None, caption: str|None=None,
        parse_mode: str|None=None, caption_entities: List[MessageEntity]|None=None, duration: int|None=None,
        performer: str|None=None, title: str|None=None, thumbnail: Union[None, InputFile, str]=None, disable_notification: bool|None=None,
        protect_content: bool|None=None, reply_to_message_id: int|None=None, allow_sending_without_reply: bool|None=None,
        reply_markup: Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply, None]=None
    ) -> Message:
        params = {}
        params['chat_id'] = chat_id
        params['audio'] = audio
        if message_thread_id is not None: params['message_thread_id'] = message_thread_id
        if caption is not None: params['caption'] = caption
        if parse_mode is not None: params['parse_mode'] = parse_mode
        if caption_entities is not None: params['caption_entities'] = caption_entities
        if duration is not None: params['duration'] = duration
        if performer is not None: params['performer'] = performer
        if title is not None: params['title'] = title
        if thumbnail is not None: params['thumbnail'] = thumbnail
        if disable_notification is not None: params['disable_notification'] = disable_notification
        if protect_content is not None: params['protect_content'] = protect_content
        if reply_to_message_id is not None: params['reply_to_message_id'] = reply_to_message_id
        if allow_sending_without_reply is not None: params['allow_sending_without_reply'] = allow_sending_without_reply
        if reply_markup is not None: params['reply_markup'] = reply_markup
        result = await super().send_audio(params)
        return Message.dese(result)

    async def send_document(
        self, chat_id: int|str, document: InputFile|str, message_thread_id: int|None=None,
        thumbnail: Union[None, InputFile, str]=None, caption: str|None=None, parse_mode: str|None=None,
        caption_entities: List[MessageEntity]|None=None, disable_content_type_detection: bool|None=None,
        disable_notification: bool|None=None, protect_content: bool|None=None, reply_to_message_id: int|None=None,
        allow_sending_without_reply: bool|None=None, reply_markup: Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply, None]=None
    ) -> Message:
        params = {}
        params['chat_id'] = chat_id
        params['document'] = document
        if message_thread_id is not None: params['message_thread_id'] = message_thread_id
        if thumbnail is not None: params['thumbnail'] = thumbnail
        if caption is not None: params['caption'] = caption
        if parse_mode is not None: params['parse_mode'] = parse_mode
        if caption_entities is not None: params['caption_entities'] = caption_entities
        if disable_content_type_detection is not None: params['disable_content_type_detection'] = disable_content_type_detection
        if disable_notification is not None: params['disable_notification'] = disable_notification
        if protect_content is not None: params['protect_content'] = protect_content
        if reply_to_message_id is not None: params['reply_to_message_id'] = reply_to_message_id
        if allow_sending_without_reply is not None: params['allow_sending_without_reply'] = allow_sending_without_reply
        if reply_markup is not None: params['reply_markup'] = reply_markup
        result = await super().send_document(params)
        return Message.dese(result)

    async def send_video(
        self, chat_id: int|str, video: InputFile|str, message_thread_id: int|None=None, duration: int|None=None,
        width: int|None=None, height: int|None=None, thumbnail: Union[None, InputFile, str]=None, caption: str|None=None,
        parse_mode: str|None=None, caption_entities: List[MessageEntity]|None=None, has_spoiler: bool|None=None,
        supports_streaming: bool|None=None, disable_notification: bool|None=None, protect_content: bool|None=None, reply_to_message_id: int|None=None,
        allow_sending_without_reply: bool|None=None, reply_markup: Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply, None]=None
    ) -> Message:
        params = {}
        params['chat_id'] = chat_id
        params['video'] = video
        if message_thread_id is not None: params['message_thread_id'] = message_thread_id
        if duration is not None: params['duration'] = duration
        if width is not None: params['width'] = width
        if height is not None: params['height'] = height
        if thumbnail is not None: params['thumbnail'] = thumbnail
        if caption is not None: params['caption'] = caption
        if parse_mode is not None: params['parse_mode'] = parse_mode
        if caption_entities is not None: params['caption_entities'] = caption_entities
        if has_spoiler is not None: params['has_spoiler'] = has_spoiler
        if supports_streaming is not None: params['supports_streaming'] = supports_streaming
        if disable_notification is not None: params['disable_notification'] = disable_notification
        if protect_content is not None: params['protect_content'] = protect_content
        if reply_to_message_id is not None: params['reply_to_message_id'] = reply_to_message_id
        if allow_sending_without_reply is not None: params['allow_sending_without_reply'] = allow_sending_without_reply
        if reply_markup is not None: params['reply_markup'] = reply_markup
        result = await super().send_video(params)
        return Message.dese(result)

    async def send_animation(
        self, chat_id: int|str, animation: InputFile|str, message_thread_id: int|None=None, duration: int|None=None,
        width: int|None=None, height: int|None=None, thumbnail: Union[None, InputFile, str]=None, caption: str|None=None,
        parse_mode: str|None=None, caption_entities: List[MessageEntity]|None=None, has_spoiler: bool|None=None,
        disable_notification: bool|None=None, protect_content: bool|None=None, reply_to_message_id: int|None=None,
        allow_sending_without_reply: bool|None=None, reply_markup: Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply, None]=None
    ) -> Message:
        params = {}
        params['chat_id'] = chat_id
        params['animation'] = animation
        if message_thread_id is not None: params['message_thread_id'] = message_thread_id
        if duration is not None: params['duration'] = duration
        if width is not None: params['width'] = width
        if height is not None: params['height'] = height
        if thumbnail is not None: params['thumbnail'] = thumbnail
        if caption is not None: params['caption'] = caption
        if parse_mode is not None: params['parse_mode'] = parse_mode
        if caption_entities is not None: params['caption_entities'] = caption_entities
        if has_spoiler is not None: params['has_spoiler'] = has_spoiler
        if disable_notification is not None: params['disable_notification'] = disable_notification
        if protect_content is not None: params['protect_content'] = protect_content
        if reply_to_message_id is not None: params['reply_to_message_id'] = reply_to_message_id
        if allow_sending_without_reply is not None: params['allow_sending_without_reply'] = allow_sending_without_reply
        if reply_markup is not None: params['reply_markup'] = reply_markup
        result = await super().send_animation(params)
        return Message.dese(result)

    async def send_voice(
        self, chat_id: int|str, voice: InputFile|str, message_thread_id: int|None=None, caption: str|None=None,
        parse_mode: str|None=None, caption_entities: List[MessageEntity]|None=None, duration: int|None=None,
        disable_notification: bool|None=None, protect_content: bool|None=None, reply_to_message_id: int|None=None,
        allow_sending_without_reply: bool|None=None, reply_markup: Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply, None]=None
    ) -> Message:
        params = {}
        params['chat_id'] = chat_id
        params['voice'] = voice
        if message_thread_id is not None: params['message_thread_id'] = message_thread_id
        if caption is not None: params['caption'] = caption
        if parse_mode is not None: params['parse_mode'] = parse_mode
        if caption_entities is not None: params['caption_entities'] = caption_entities
        if duration is not None: params['duration'] = duration
        if disable_notification is not None: params['disable_notification'] = disable_notification
        if protect_content is not None: params['protect_content'] = protect_content
        if reply_to_message_id is not None: params['reply_to_message_id'] = reply_to_message_id
        if allow_sending_without_reply is not None: params['allow_sending_without_reply'] = allow_sending_without_reply
        if reply_markup is not None: params['reply_markup'] = reply_markup
        result = await super().send_voice(params)
        return Message.dese(result)

    async def send_video_note(
        self, chat_id: int|str, video_note: InputFile|str, message_thread_id: int|None=None, duration: int|None=None,
        length: int|None=None, thumbnail: Union[None, InputFile, str]=None, disable_notification: bool|None=None,
        protect_content: bool|None=None, reply_to_message_id: int|None=None, allow_sending_without_reply: bool|None=None,
        reply_markup: Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply, None]=None
    ) -> Message:
        params = {}
        params['chat_id'] = chat_id
        params['video_note'] = video_note
        if message_thread_id is not None: params['message_thread_id'] = message_thread_id
        if duration is not None: params['duration'] = duration
        if length is not None: params['length'] = length
        if thumbnail is not None: params['thumbnail'] = thumbnail
        if disable_notification is not None: params['disable_notification'] = disable_notification
        if protect_content is not None: params['protect_content'] = protect_content
        if reply_to_message_id is not None: params['reply_to_message_id'] = reply_to_message_id
        if allow_sending_without_reply is not None: params['allow_sending_without_reply'] = allow_sending_without_reply
        if reply_markup is not None: params['reply_markup'] = reply_markup
        result = await super().send_video_note(params)
        return Message.dese(result)

    async def send_media_group(
        self, chat_id: int|str, media: List[Union[InputMediaAudio, InputMediaDocument, InputMediaPhoto, InputMediaVideo]],
        message_thread_id: int|None=None, disable_notification: bool|None=None, protect_content: bool|None=None,
        reply_to_message_id: int|None=None,allow_sending_without_reply: bool|None=None
    ) -> List[Message]:
        params = {}
        params['chat_id'] = chat_id
        params['media'] = media
        if message_thread_id is not None: params['message_thread_id'] = message_thread_id
        if disable_notification is not None: params['disable_notification'] = disable_notification
        if protect_content is not None: params['protect_content'] = protect_content
        if reply_to_message_id is not None: params['reply_to_message_id'] = reply_to_message_id
        if allow_sending_without_reply is not None: params['allow_sending_without_reply'] = allow_sending_without_reply
        result = await super().send_media_group(params)
        return [Message.dese(message) for message in result]

    async def send_location(
        self, chat_id: int|str, latitude: float, longitude: float, message_thread_id: int|None=None, horizontal_accuracy: float|None=None,
        live_period: int|None=None, heading: int|None=None, proximity_alert_radius: int|None=None, disable_notification: bool|None=None,
        protect_content: bool|None=None, reply_to_message_id: int|None=None, allow_sending_without_reply: bool|None=None,
        reply_markup: Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply, None]=None
    ) -> Message:
        params = {}
        params['chat_id'] = chat_id
        params['latitude'] = latitude
        params['longitude'] = longitude
        if message_thread_id is not None: params['message_thread_id'] = message_thread_id
        if horizontal_accuracy is not None: params['horizontal_accuracy'] = horizontal_accuracy
        if live_period is not None: params['live_period'] = live_period
        if heading is not None: params['heading'] = heading
        if proximity_alert_radius is not None: params['proximity_alert_radius'] = proximity_alert_radius
        if disable_notification is not None: params['disable_notification'] = disable_notification
        if protect_content is not None: params['protect_content'] = protect_content
        if reply_to_message_id is not None: params['reply_to_message_id'] = reply_to_message_id
        if allow_sending_without_reply is not None: params['allow_sending_without_reply'] = allow_sending_without_reply
        if reply_markup is not None: params['reply_markup'] = reply_markup
        result = await super().send_location(params)
        return Message.dese(result)

    async def send_venue(
        self, chat_id: int|str, latitude: float, longitude: float, title: str, address: str, message_thread_id: int|None=None,
        foursquare_id: str|None=None, foursquare_type: str|None=None, google_place_id: str|None=None, google_place_type: str|None=None,
        disable_notification: bool|None=None, protect_content: bool|None=None, reply_to_message_id: int|None=None, allow_sending_without_reply: bool|None=None,
        reply_markup: Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply, None]=None
    ) -> Message:
        params = {}
        params['chat_id'] = chat_id
        params['latitude'] = latitude
        params['longitude'] = longitude
        params['title'] = title
        params['address'] = address
        if message_thread_id is not None: params['message_thread_id'] = message_thread_id
        if foursquare_id is not None: params['foursquare_id'] = foursquare_id
        if foursquare_type is not None: params['foursquare_type'] = foursquare_type
        if google_place_id is not None: params['google_place_id'] = google_place_id
        if google_place_type is not None: params['google_place_type'] = google_place_type
        if disable_notification is not None: params['disable_notification'] = disable_notification
        if protect_content is not None: params['protect_content'] = protect_content
        if reply_to_message_id is not None: params['reply_to_message_id'] = reply_to_message_id
        if allow_sending_without_reply is not None: params['allow_sending_without_reply'] = allow_sending_without_reply
        if reply_markup is not None: params['reply_markup'] = reply_markup
        result = await super().send_venue(params)
        return Message.dese(result)

    async def send_contact(
        self, chat_id: int|str, phone_number: str, first_name: str, message_thread_id: int|None=None, last_name: str|None=None,
        vcard: str|None=None, disable_notification: bool|None=None, protect_content: bool|None=None, reply_to_message_id: int|None=None,
        allow_sending_without_reply: bool|None=None, reply_markup: Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply, None]=None
    ) -> Message:
        params = {}
        params['chat_id'] = chat_id
        params['phone_number'] = phone_number
        params['first_name'] = first_name
        if message_thread_id is not None: params['message_thread_id'] = message_thread_id
        if last_name is not None: params['last_name'] = last_name
        if vcard is not None: params['vcard'] = vcard
        if disable_notification is not None: params['disable_notification'] = disable_notification
        if protect_content is not None: params['protect_content'] = protect_content
        if reply_to_message_id is not None: params['reply_to_message_id'] = reply_to_message_id
        if allow_sending_without_reply is not None: params['allow_sending_without_reply'] = allow_sending_without_reply
        if reply_markup is not None: params['reply_markup'] = reply_markup
        result = await super().send_contact(params)
        return Message.dese(result)

    async def send_poll(
        self, chat_id: int|str, question: str, options: List[str], message_thread_id: int|None=None, is_anonymous: bool|None=None,
        type: str|None=None, allows_multiple_answers: bool|None=None, correct_option_id: int|None=None, explanation: str|None=None,
        explanation_parse_mode: str|None=None, explanation_entities: List[MessageEntity]|None=None, open_period: int|None=None, close_date: int|None=None,
        is_closed: bool|None=None, disable_notification: bool|None=None, protect_content: bool|None=None, reply_to_message_id: int|None=None,
        allow_sending_without_reply: bool|None=None, reply_markup: Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply, None]=None
    ) -> Message:
        params = {}
        params['chat_id'] = chat_id
        params['question'] = question
        params['options'] = options
        if message_thread_id is not None: params['message_thread_id'] = message_thread_id
        if is_anonymous is not None: params['is_anonymous'] = is_anonymous
        if type is not None: params['type'] = type
        if allows_multiple_answers is not None: params['allows_multiple_answers'] = allows_multiple_answers
        if correct_option_id is not None: params['correct_option_id'] = correct_option_id
        if explanation is not None: params['explanation'] = explanation
        if explanation_parse_mode is not None: params['explanation_parse_mode'] = explanation_parse_mode
        if explanation_entities is not None: params['explanation_entities'] = explanation_entities
        if open_period is not None: params['open_period'] = open_period
        if close_date is not None: params['close_date'] = close_date
        if is_closed is not None: params['is_closed'] = is_closed
        if disable_notification is not None: params['disable_notification'] = disable_notification
        if protect_content is not None: params['protect_content'] = protect_content
        if reply_to_message_id is not None: params['reply_to_message_id'] = reply_to_message_id
        if allow_sending_without_reply is not None: params['allow_sending_without_reply'] = allow_sending_without_reply
        if reply_markup is not None: params['reply_markup'] = reply_markup
        result = await super().send_poll(params)
        return Message.dese(result)

    async def send_dice(
        self, chat_id: int|str, message_thread_id: int|None=None, emoji: str|None=None, disable_notification: bool|None=None,
        protect_content: bool|None=None, reply_to_message_id: int|None=None, allow_sending_without_reply: bool|None=None,
        reply_markup: Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply, None]=None
    ) -> Message:
        params = {}
        params['chat_id'] = chat_id
        if message_thread_id is not None: params['message_thread_id'] = message_thread_id
        if emoji is not None: params['emoji'] = emoji
        if disable_notification is not None: params['disable_notification'] = disable_notification
        if protect_content is not None: params['protect_content'] = protect_content
        if reply_to_message_id is not None: params['reply_to_message_id'] = reply_to_message_id
        if allow_sending_without_reply is not None: params['allow_sending_without_reply'] = allow_sending_without_reply
        if reply_markup is not None: params['reply_markup'] = reply_markup
        result = await super().send_dice(params)
        return Message.dese(result)

    async def send_chat_action(self, chat_id: int|str, action: str, message_thread_id: int|None=None) -> True:
        params = {}
        params['chat_id'] = chat_id
        params['action'] = action
        if message_thread_id is not None: params['message_thread_id'] = message_thread_id
        result = await super().send_chat_action(params)
        return result

    async def get_user_profile_photos(self, user_id: int, offset: int|None=None, limit: int|None=None) -> UserProfilePhotos:
        params = {}
        params['user_id'] = user_id
        if offset is not None: params['offset'] = offset
        if limit is not None: params['limit'] = limit
        result = await super().get_user_profile_photos(params)
        return UserProfilePhotos.dese(result)

    async def get_file(self, file_id: str) -> File:
        params = {}
        params['file_id'] = file_id
        result = await super().get_file(params)
        return File.dese(result)

    async def ban_chat_member(self, chat_id: int|str, user_id: int, until_date: int|None=None, revoke_messages: bool|None=None) -> True:
        params = {}
        params['chat_id'] = chat_id
        params['user_id'] = user_id
        if until_date is not None: params['until_date'] = until_date
        if revoke_messages is not None: params['revoke_messages'] = revoke_messages
        result = await super().ban_chat_member(params)
        return result

    async def unban_chat_member(self, chat_id: int|str, user_id: int, only_if_banned: bool|None=None) -> True:
        params = {}
        params['chat_id'] = chat_id
        params['user_id'] = user_id
        if only_if_banned is not None: params['only_if_banned'] = only_if_banned
        result = await super().unban_chat_member(params)
        return result

    async def restrict_chat_member(
        self, chat_id: int|str, user_id: int, permissions: ChatPermissions,
        use_independent_chat_permissions: bool|None=None, until_date: int|None=None
    ) -> True:
        params = {}
        params['chat_id'] = chat_id
        params['user_id'] = user_id
        params['permissions'] = permissions
        if use_independent_chat_permissions is not None: params['use_independent_chat_permissions'] = use_independent_chat_permissions
        if until_date is not None: params['until_date'] = until_date
        result = await super().restrict_chat_member(params)
        return result

    async def promote_chat_member(
        self, chat_id: int|str, user_id: int, is_anonymous: bool|None=None, can_manage_chat: bool|None=None, can_delete_messages: bool|None=None,
        can_manage_video_chats: bool|None=None, can_restrict_members: bool|None=None, can_promote_members: bool|None=None, can_change_info: bool|None=None,
        can_invite_users: bool|None=None, can_post_messages: bool|None=None, can_edit_messages: bool|None=None, can_pin_messages: bool|None=None,
        can_post_stories: bool|None=None, can_edit_stories: bool|None=None, can_delete_stories: bool|None=None, can_manage_topics: bool|None=None
    ) -> True:
        params = {}
        params['chat_id'] = chat_id
        params['user_id'] = user_id
        if is_anonymous is not None: params['is_anonymous'] = is_anonymous
        if can_manage_chat is not None: params['can_manage_chat'] = can_manage_chat
        if can_delete_messages is not None: params['can_delete_messages'] = can_delete_messages
        if can_manage_video_chats is not None: params['can_manage_video_chats'] = can_manage_video_chats
        if can_restrict_members is not None: params['can_restrict_members'] = can_restrict_members
        if can_promote_members is not None: params['can_promote_members'] = can_promote_members
        if can_change_info is not None: params['can_change_info'] = can_change_info
        if can_invite_users is not None: params['can_invite_users'] = can_invite_users
        if can_post_messages is not None: params['can_post_messages'] = can_post_messages
        if can_edit_messages is not None: params['can_edit_messages'] = can_edit_messages
        if can_pin_messages is not None: params['can_pin_messages'] = can_pin_messages
        if can_post_stories is not None: params['can_post_stories'] = can_post_stories
        if can_edit_stories is not None: params['can_edit_stories'] = can_edit_stories
        if can_delete_stories is not None: params['can_delete_stories'] = can_delete_stories
        if can_manage_topics is not None: params['can_manage_topics'] = can_manage_topics
        result = await super().promote_chat_member(params)
        return result

    async def set_chat_administrator_custom_title(self, chat_id: int|str, user_id: int, custom_title: str) -> True:
        params = {}
        params['chat_id'] = chat_id
        params['user_id'] = user_id
        params['custom_title'] = custom_title
        result = await super().set_chat_administrator_custom_title(params)
        return result

    async def ban_chat_sender_chat(self, chat_id: int|str, sender_chat_id: int) -> True:
        params = {}
        params['chat_id'] = chat_id
        params['sender_chat_id'] = sender_chat_id
        result = await super().ban_chat_sender_chat(params)
        return result

    async def unban_chat_sender_chat(self, chat_id: int|str, sender_chat_id: int) -> True:
        params = {}
        params['chat_id'] = chat_id
        params['sender_chat_id'] = sender_chat_id
        result = await super().unban_chat_sender_chat(params)
        return result

    async def set_chat_permissions(self, chat_id: int|str, permissions: ChatPermissions, use_independent_chat_permissions: bool|None=None) -> True:
        params = {}
        params['chat_id'] = chat_id
        params['permissions'] = permissions
        if use_independent_chat_permissions is not None: params['use_independent_chat_permissions'] = use_independent_chat_permissions
        result = await super().set_chat_permissions(params)
        return result

    async def export_chat_invite_link(self, chat_id: int|str) -> str:
        params = {}
        params['chat_id'] = chat_id
        result = await super().export_chat_invite_link(params)
        return result

    async def create_chat_invite_link(
        self, chat_id: int|str, name: str|None=None, expire_date: int|None=None,
        member_limit: int|None=None, creates_join_request: bool|None=None
    ) -> ChatInviteLink:
        params = {}
        params['chat_id'] = chat_id
        if name is not None: params['name'] = name
        if expire_date is not None: params['expire_date'] = expire_date
        if member_limit is not None: params['member_limit'] = member_limit
        if creates_join_request is not None: params['creates_join_request'] = creates_join_request
        result = await super().create_chat_invite_link(params)
        return ChatInviteLink.dese(result)

    async def edit_chat_invite_link(
        self, chat_id: int|str, invite_link: str, name: str|None=None,
        expire_date: int|None=None, member_limit: int|None=None, creates_join_request: bool|None=None
    ) -> ChatInviteLink:
        params = {}
        params['chat_id'] = chat_id
        params['invite_link'] = invite_link
        if name is not None: params['name'] = name
        if expire_date is not None: params['expire_date'] = expire_date
        if member_limit is not None: params['member_limit'] = member_limit
        if creates_join_request is not None: params['creates_join_request'] = creates_join_request
        result = await super().edit_chat_invite_link(params)
        return ChatInviteLink.dese(result)

    async def revoke_chat_invite_link(self, chat_id: int|str, invite_link: str) -> ChatInviteLink:
        params = {}
        params['chat_id'] = chat_id
        params['invite_link'] = invite_link
        result = await super().revoke_chat_invite_link(params)
        return ChatInviteLink.dese(result)

    async def approve_chat_join_request(self, chat_id: int|str, user_id: int) -> True:
        params = {}
        params['chat_id'] = chat_id
        params['user_id'] = user_id
        result = await super().approve_chat_join_request(params)
        return result

    async def decline_chat_join_request(self, chat_id: int|str, user_id: int) -> True:
        params = {}
        params['chat_id'] = chat_id
        params['user_id'] = user_id
        result = await super().decline_chat_join_request(params)
        return result

    async def set_chat_photo(self, chat_id: int|str, photo: InputFile) -> True:
        params = {}
        params['chat_id'] = chat_id
        params['photo'] = photo
        result = await super().set_chat_photo(params)
        return result

    async def delete_chat_photo(self, chat_id: int|str) -> True:
        params = {}
        params['chat_id'] = chat_id
        result = await super().delete_chat_photo(params)
        return result

    async def set_chat_title(self, chat_id: int|str, title: str) -> True:
        params = {}
        params['chat_id'] = chat_id
        params['title'] = title
        result = await super().set_chat_title(params)
        return result

    async def set_chat_description(self, chat_id: int|str, description: str|None=None) -> True:
        params = {}
        params['chat_id'] = chat_id
        if description is not None: params['description'] = description
        result = await super().set_chat_description(params)
        return result

    async def pin_chat_message(self, chat_id: int|str, message_id: int, disable_notification: bool|None=None) -> True:
        params = {}
        params['chat_id'] = chat_id
        params['message_id'] = message_id
        if disable_notification is not None: params['disable_notification'] = disable_notification
        result = await super().pin_chat_message(params)
        return result

    async def unpin_chat_message(self, chat_id: int|str, message_id: int|None=None) -> True:
        params = {}
        params['chat_id'] = chat_id
        if message_id is not None: params['message_id'] = message_id
        result = await super().unpin_chat_message(params)
        return result

    async def unpin_all_chat_messages(self, chat_id: int|str) -> True:
        params = {}
        params['chat_id'] = chat_id
        result = await super().unpin_all_chat_messages(params)
        return result

    async def leave_chat(self, chat_id: int|str) -> True:
        params = {}
        params['chat_id'] = chat_id
        result = await super().leave_chat(params)
        return result

    async def get_chat(self, chat_id: int|str) -> Chat:
        params = {}
        params['chat_id'] = chat_id
        result = await super().get_chat(params)
        return Chat.dese(result)

    async def get_chat_administrators(self, chat_id: int|str) -> List[ChatMember]:
        params = {}
        params['chat_id'] = chat_id
        result = await super().get_chat_administrators(params)
        return [ChatMember.dese(chat_member) for chat_member in result]

    async def get_chat_member_count(self, chat_id: int|str) -> int:
        params = {}
        params['chat_id'] = chat_id
        result = await super().get_chat_member_count(params)
        return result

    async def get_chat_member(self, chat_id: int|str, user_id: int) -> ChatMember:
        params = {}
        params['chat_id'] = chat_id
        params['user_id'] = user_id
        result = await super().get_chat_member(params)
        return ChatMember.dese(result)

    async def set_chat_sticker_set(self, chat_id: int|str, sticker_set_name: str) -> True:
        params = {}
        params['chat_id'] = chat_id
        params['sticker_set_name'] = sticker_set_name
        result = await super().set_chat_sticker_set(params)
        return result

    async def delete_chat_sticker_set(self, chat_id: int|str) -> True:
        params = {}
        params['chat_id'] = chat_id
        result = await super().delete_chat_sticker_set(params)
        return result

    async def get_forum_topic_icon_stickers(self) -> List[Sticker]:
        result = await super().get_forum_topic_icon_stickers()
        return [Sticker.dese(sticker) for sticker in result]

    async def create_forum_topic(self, chat_id: int|str, name: str, icon_color: int|None=None, icon_custom_emoji_id: str|None=None) -> ForumTopic:
        params = {}
        params['chat_id'] = chat_id
        params['name'] = name
        if icon_color is not None: params['icon_color'] = icon_color
        if icon_custom_emoji_id is not None: params['icon_custom_emoji_id'] = icon_custom_emoji_id
        result = await super().create_forum_topic(params)
        return ForumTopic.dese(result)

    async def edit_forum_topic(self, chat_id: int|str, message_thread_id: int, name: str|None=None, icon_custom_emoji_id: str|None=None) -> True:
        params = {}
        params['chat_id'] = chat_id
        params['message_thread_id'] = message_thread_id
        if name is not None: params['name'] = name
        if icon_custom_emoji_id is not None: params['icon_custom_emoji_id'] = icon_custom_emoji_id
        result = await super().edit_forum_topic(params)
        return result

    async def close_forum_topic(self, chat_id: int|str, message_thread_id: int) -> True:
        params = {}
        params['chat_id'] = chat_id
        params['message_thread_id'] = message_thread_id
        result = await super().close_forum_topic(params)
        return result

    async def reopen_forum_topic(self, chat_id: int|str, message_thread_id: int) -> True:
        params = {}
        params['chat_id'] = chat_id
        params['message_thread_id'] = message_thread_id
        result = await super().reopen_forum_topic(params)
        return result

    async def delete_forum_topic(self, chat_id: int|str, message_thread_id: int) -> True:
        params = {}
        params['chat_id'] = chat_id
        params['message_thread_id'] = message_thread_id
        result = await super().delete_forum_topic(params)
        return result

    async def unpin_all_forum_topic_messages(self, chat_id: int|str, message_thread_id: int) -> True:
        params = {}
        params['chat_id'] = chat_id
        params['message_thread_id'] = message_thread_id
        result = await super().unpin_all_forum_topic_messages(params)
        return result

    async def edit_general_forum_topic(self, chat_id: int|str, name: str) -> True:
        params = {}
        params['chat_id'] = chat_id
        params['name'] = name
        result = await super().edit_general_forum_topic(params)
        return result

    async def close_general_forum_topic(self, chat_id: int|str) -> True:
        params = {}
        params['chat_id'] = chat_id
        result = await super().close_general_forum_topic(params)
        return result

    async def reopen_general_forum_topic(self, chat_id: int|str) -> True:
        params = {}
        params['chat_id'] = chat_id
        result = await super().reopen_general_forum_topic(params)
        return result

    async def hide_general_forum_topic(self, chat_id: int|str) -> True:
        params = {}
        params['chat_id'] = chat_id
        result = await super().hide_general_forum_topic(params)
        return result

    async def unhide_general_forum_topic(self, chat_id: int|str) -> True:
        params = {}
        params['chat_id'] = chat_id
        result = await super().unhide_general_forum_topic(params)
        return result

    async def unpin_all_general_forum_topic_messages(self, chat_id: int|str) -> True:
        params = {}
        params['chat_id'] = chat_id
        result = await super().unpin_all_general_forum_topic_messages(params)
        return result

    async def answer_callback_query(
        self, callback_query_id: str, text: str|None=None,
        show_alert: bool|None=None, url: str|None=None, cache_time: int|None=None
    ) -> True:
        params = {}
        params['callback_query_id'] = callback_query_id
        if text is not None: params['text'] = text
        if show_alert is not None: params['show_alert'] = show_alert
        if url is not None: params['url'] = url
        if cache_time is not None: params['cache_time'] = cache_time
        result = await super().answer_callback_query(params)
        return result

    async def set_my_commands(self, commands: List[BotCommand], scope: BotCommandScope|None=None, language_code: str|None=None) -> True:
        params = {}
        params['commands'] = commands
        if scope is not None: params['scope'] = scope
        if language_code is not None: params['language_code'] = language_code
        result = await super().set_my_commands(params)
        return result

    async def delete_my_commands(self, scope: BotCommandScope|None=None, language_code: str|None=None) -> True:
        params = {}
        if scope is not None: params['scope'] = scope
        if language_code is not None: params['language_code'] = language_code
        result = await super().delete_my_commands(params)
        return result

    async def get_my_commands(self, scope: BotCommandScope|None=None, language_code: str|None=None) -> List[BotCommand]:
        params = {}
        if scope is not None: params['scope'] = scope
        if language_code is not None: params['language_code'] = language_code
        result = await super().get_my_commands(params)
        return [BotCommand.dese(bot_command) for bot_command in result]

    async def set_my_name(self, name: str|None=None, language_code: str|None=None) -> True:
        params = {}
        if name is not None: params['name'] = name
        if language_code is not None: params['language_code'] = language_code
        result = await super().set_my_name(params)
        return result

    async def get_my_name(self, language_code: str|None=None) -> BotName:
        params = {}
        if language_code is not None: params['language_code'] = language_code
        result = await super().get_my_name(params)
        return BotName.dese(result)

    async def set_my_description(self, description: str|None=None, language_code: str|None=None) -> True:
        params = {}
        if description is not None: params['description'] = description
        if language_code is not None: params['language_code'] = language_code
        result = await super().set_my_description(params)
        return result

    async def get_my_description(self, language_code: str|None=None) -> BotDescription:
        params = {}
        if language_code is not None: params['language_code'] = language_code
        result = await super().get_my_description(params)
        return BotDescription.dese(result)

    async def set_my_short_description(self, short_description: str|None=None, language_code: str|None=None) -> True:
        params = {}
        if short_description is not None: params['short_description'] = short_description
        if language_code is not None: params['language_code'] = language_code
        result = await super().set_my_short_description(params)
        return result

    async def get_my_short_description(self, language_code: str|None=None) -> BotShortDescription:
        params = {}
        if language_code is not None: params['language_code'] = language_code
        result = await super().get_my_short_description(params)
        return BotShortDescription.dese(result)

    async def set_chat_menu_button(self, chat_id: int|None=None, menu_button: MenuButton|None=None) -> True:
        params = {}
        if chat_id is not None: params['chat_id'] = chat_id
        if menu_button is not None: params['menu_button'] = menu_button
        result = await super().set_chat_menu_button(params)
        return result

    async def get_chat_menu_button(self, chat_id: int|None=None) -> MenuButton:
        params = {}
        if chat_id is not None: params['chat_id'] = chat_id
        result = await super().get_chat_menu_button(params)
        return MenuButton.dese(result)

    async def set_my_default_administrator_rights(self, rights: ChatAdministratorRights|None=None, for_channels: bool|None=None) -> True:
        params = {}
        if rights is not None: params['rights'] = rights
        if for_channels is not None: params['for_channels'] = for_channels
        result = await super().set_my_default_administrator_rights(params)
        return result

    async def get_my_default_administrator_rights(self, for_channels: bool|None=None) -> ChatAdministratorRights:
        params = {}
        if for_channels is not None: params['for_channels'] = for_channels
        result = await super().get_my_default_administrator_rights(params)
        return ChatAdministratorRights.dese(result)

    async def edit_message_text(
        self, text: str, chat_id: int|str|None=None, message_id: int|None=None, inline_message_id: str|None=None, parse_mode: str|None=None,
        entities: List[MessageEntity]|None=None, disable_web_page_preview: bool|None=None, reply_markup: InlineKeyboardMarkup|None=None
    ) -> Union[Message, True]:
        params = {}
        params['text'] = text
        if chat_id is not None: params['chat_id'] = chat_id
        if message_id is not None: params['message_id'] = message_id
        if inline_message_id is not None: params['inline_message_id'] = inline_message_id
        if parse_mode is not None: params['parse_mode'] = parse_mode
        if entities is not None: params['entities'] = entities
        if disable_web_page_preview is not None: params['disable_web_page_preview'] = disable_web_page_preview
        if reply_markup is not None: params['reply_markup'] = reply_markup
        result = await super().edit_message_text(params)
        # this to prevent errors of inline messages that return "True"
        return Message.dese(result) if result is not True else True

    async def edit_message_caption(
        self, chat_id: int|str|None=None, message_id: int|None=None, inline_message_id: str|None=None, caption: str|None=None,
        parse_mode: str|None=None, caption_entities: List[MessageEntity]|None=None, reply_markup: InlineKeyboardMarkup|None=None
    ) -> Union[Message, True]:
        params = {}
        if chat_id is not None: params['chat_id'] = chat_id
        if message_id is not None: params['message_id'] = message_id
        if inline_message_id is not None: params['inline_message_id'] = inline_message_id
        if caption is not None: params['caption'] = caption
        if parse_mode is not None: params['parse_mode'] = parse_mode
        if caption_entities is not None: params['caption_entities'] = caption_entities
        if reply_markup is not None: params['reply_markup'] = reply_markup
        result = await super().edit_message_caption(params)
        # this to prevent errors of inline messages that return "True"
        return Message.dese(result) if result is not True else True

    async def edit_message_media(
        self, media: InputMedia, chat_id: int|str|None=None, message_id: int|None=None,
        inline_message_id: str|None=None, reply_markup: InlineKeyboardMarkup|None=None
    ) -> Union[Message, True]:
        params = {}
        params['media'] = media
        if chat_id is not None: params['chat_id'] = chat_id
        if message_id is not None: params['message_id'] = message_id
        if inline_message_id is not None: params['inline_message_id'] = inline_message_id
        if reply_markup is not None: params['reply_markup'] = reply_markup
        result = await super().edit_message_media(params)
        # this to prevent errors of inline messages that return "True"
        return Message.dese(result) if result is not True else True

    async def edit_message_live_location(
        self, latitude: float, longitude: float, chat_id: int|str|None=None, message_id: int|None=None,
        inline_message_id: str|None=None, horizontal_accuracy: float|None=None, heading: int|None=None,
        proximity_alert_radius: int|None=None, reply_markup: InlineKeyboardMarkup|None=None
    ) -> Union[Message, True]:
        params = {}
        params['latitude'] = latitude
        params['longitude'] = longitude
        if chat_id is not None: params['chat_id'] = chat_id
        if message_id is not None: params['message_id'] = message_id
        if inline_message_id is not None: params['inline_message_id'] = inline_message_id
        if horizontal_accuracy is not None: params['horizontal_accuracy'] = horizontal_accuracy
        if heading is not None: params['heading'] = heading
        if proximity_alert_radius is not None: params['proximity_alert_radius'] = proximity_alert_radius
        if reply_markup is not None: params['reply_markup'] = reply_markup
        result = await super().edit_message_live_location(params)
        # this to prevent errors of inline messages that return "True"
        return Message.dese(result) if result is not True else True

    async def stop_message_live_location(
        self, chat_id: int|str|None=None, message_id: int|None=None,
        inline_message_id: str|None=None, reply_markup: InlineKeyboardMarkup|None=None
    ) -> Union[Message, True]:
        params = {}
        if chat_id is not None: params['chat_id'] = chat_id
        if message_id is not None: params['message_id'] = message_id
        if inline_message_id is not None: params['inline_message_id'] = inline_message_id
        if reply_markup is not None: params['reply_markup'] = reply_markup
        result = await super().stop_message_live_location(params)
        # this to prevent errors of inline messages that return "True"
        return Message.dese(result) if result is not True else True

    async def edit_message_reply_markup(
        self, chat_id: int|str|None=None, message_id: int|None=None,
        inline_message_id: str|None=None, reply_markup: InlineKeyboardMarkup|None=None
    ) -> Union[Message, True]:
        params = {}
        if chat_id is not None: params['chat_id'] = chat_id
        if message_id is not None: params['message_id'] = message_id
        if inline_message_id is not None: params['inline_message_id'] = inline_message_id
        if reply_markup is not None: params['reply_markup'] = reply_markup
        result = await super().edit_message_reply_markup(params)
        # this to prevent errors of inline messages that return "True"
        return Message.dese(result) if result is not True else True

    async def stop_poll(self, chat_id: int|str, message_id: int, reply_markup: InlineKeyboardMarkup|None=None) -> Poll:
        params = {}
        params['chat_id'] = chat_id
        params['message_id'] = message_id
        if reply_markup is not None: params['reply_markup'] = reply_markup
        result = await super().stop_poll(params)
        return Poll.dese(result)

    async def send_sticker(
        self, chat_id: int|str, sticker: InputFile|str, message_thread_id: int|None=None, emoji: str|None=None, disable_notification: bool|None=None,
        protect_content: bool|None=None, reply_to_message_id: int|None=None, allow_sending_without_reply: bool|None=None,
        reply_markup: Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply, None]=None
    ) -> Message:
        params = {}
        params['chat_id'] = chat_id
        params['sticker'] = sticker
        if message_thread_id is not None: params['message_thread_id'] = message_thread_id
        if emoji is not None: params['emoji'] = emoji
        if disable_notification is not None: params['disable_notification'] = disable_notification
        if protect_content is not None: params['protect_content'] = protect_content
        if reply_to_message_id is not None: params['reply_to_message_id'] = reply_to_message_id
        if allow_sending_without_reply is not None: params['allow_sending_without_reply'] = allow_sending_without_reply
        if reply_markup is not None: params['reply_markup'] = reply_markup
        result = await super().send_sticker(params)
        return Message.dese(result)

    async def get_sticker_set(self, name: str) -> StickerSet:
        params = {}
        params['name'] = name
        result = await super().get_sticker_set(params)
        return StickerSet.dese(result)

    async def get_custom_emoji_stickers(self, custom_emoji_ids: List[str]) -> List[Sticker]:
        params = {}
        params['custom_emoji_ids'] = custom_emoji_ids
        result = await super().get_custom_emoji_stickers(params)
        return [Sticker.dese(sticker) for sticker in result]

    async def upload_sticker_file(self, user_id: int, sticker: InputFile, sticker_format: str) -> File:
        params = {}
        params['user_id'] = user_id
        params['sticker'] = sticker
        params['sticker_format'] = sticker_format
        result = await super().upload_sticker_file(params)
        return File.dese(result)

    async def create_new_sticker_set(
        self, user_id: int, name: str, title: str, stickers: List[InputSticker],
        sticker_format: str, sticker_type: str|None=None, needs_repainting: bool|None=None
    ) -> True:
        params = {}
        params['user_id'] = user_id
        params['name'] = name
        params['title'] = title
        params['stickers'] = stickers
        params['sticker_format'] = sticker_format
        if sticker_type is not None: params['sticker_type'] = sticker_type
        if needs_repainting is not None: params['needs_repainting'] = needs_repainting
        result = await super().create_new_sticker_set(params)
        return result

    async def add_sticker_to_set(self, user_id: int, name: str, sticker: InputSticker) -> True:
        params = {}
        params['user_id'] = user_id
        params['name'] = name
        params['sticker'] = sticker
        result = await super().add_sticker_to_set(params)
        return result

    async def set_sticker_position_in_set(self, sticker: str, position: int) -> True:
        params = {}
        params['sticker'] = sticker
        params['position'] = position
        result = await super().set_sticker_position_in_set(params)
        return result

    async def delete_sticker_from_set(self, sticker: str) -> True:
        params = {}
        params['sticker'] = sticker
        result = await super().delete_sticker_from_set(params)
        return result

    async def set_sticker_emoji_list(self, sticker: str, emoji_list: List[str]) -> True:
        params = {}
        params['sticker'] = sticker
        params['emoji_list'] = emoji_list
        result = await super().set_sticker_emoji_list(params)
        return result

    async def set_sticker_keywords(self, sticker: str, keywords: List[str]|None=None) -> True:
        params = {}
        params['sticker'] = sticker
        if keywords is not None: params['keywords'] = keywords
        result = await super().set_sticker_keywords(params)
        return result

    async def set_sticker_mask_position(self, sticker: str, mask_position: MarkPosition|None=None) -> True:
        params = {}
        params['sticker'] = sticker
        if mask_position is not None: params['mask_position'] = mask_position
        result = await super().set_sticker_mask_position(params)
        return result

    async def set_sticker_set_title(self, name: str, title: str) -> True:
        params = {}
        params['name'] = name
        params['title'] = title
        result = await super().set_sticker_set_title(params)
        return result

    async def set_sticker_set_thumbnail(
        self, name: str, user_id: int,
        thumbnail: Union[None, InputFile, str]=None
    ) -> True:
        params = {}
        params['name'] = name
        params['user_id'] = user_id
        if thumbnail is not None: params['thumbnail'] = thumbnail
        result = await super().set_sticker_set_thumbnail(params)
        return result

    async def set_custom_emoji_sticker_set_thumbnail(self, name: str, custom_emoji_id: str|None=None) -> True:
        params = {}
        params['name'] = name
        if custom_emoji_id is not None: params['custom_emoji_id'] = custom_emoji_id
        result = await super().set_custom_emoji_sticker_set_thumbnail(params)
        return result

    async def delete_sticker_set(self, name: str) -> True:
        params = {}
        params['name'] = name
        result = await super().delete_sticker_set(params)
        return result

    async def answer_inline_query(
        self, inline_query_id: str, results: List[InlineQueryResult], cache_time: int|None=None,
        is_personal: bool|None=None, next_offset: str|None=None, button: InlineQueryResultsButton|None=None
    ) -> True:
        params = {}
        params['inline_query_id'] = inline_query_id
        params['results'] = results
        if cache_time is not None: params['cache_time'] = cache_time
        if is_personal is not None: params['is_personal'] = is_personal
        if next_offset is not None: params['next_offset'] = next_offset
        if button is not None: params['button'] = button
        result = await super().answer_inline_query(params)
        return result

    async def answer_web_app_query(
        self, web_app_query_id: str,
        result: InlineQueryResult
    ) -> SentWebAppMessage:
        params = {}
        params['web_app_query_id'] = web_app_query_id
        params['result'] = result
        result = await super().answer_web_app_query(params)
        return SentWebAppMessage.dese(result)

    async def send_invoice(
        self, chat_id: int|str, title: str, description: str, payload: str, provider_token: str, currency: str, prices: List[LabeledPrice],
        message_thread_id: int|None=None, max_tip_amount: int|None=None, suggested_tip_amounts: List[int]|None=None, start_parameter: str|None=None,
        provider_data: str|None=None, photo_url: str|None=None, photo_size: int|None=None, photo_width: int|None=None, photo_height: int|None=None,
        need_name: bool|None=None, need_phone_number: bool|None=None, need_email: bool|None=None, need_shipping_address: bool|None=None,
        send_phone_number_to_provider: bool|None=None, send_email_to_provider: bool|None=None, is_flexible: bool|None=None,
        disable_notification: bool|None=None, protect_content: bool|None=None, reply_to_message_id: int|None=None,
        allow_sending_without_reply: bool|None=None, reply_markup: InlineKeyboardMarkup|None=None
    ) -> Message:
        params = {}
        params['chat_id'] = chat_id
        params['title'] = title
        params['description'] = description
        params['payload'] = payload
        params['provider_token'] = provider_token
        params['currency'] = currency
        params['prices'] = prices
        if message_thread_id is not None: params['message_thread_id'] = message_thread_id
        if max_tip_amount is not None: params['max_tip_amount'] = max_tip_amount
        if suggested_tip_amounts is not None: params['suggested_tip_amounts'] = suggested_tip_amounts
        if start_parameter is not None: params['start_parameter'] = start_parameter
        if provider_data is not None: params['provider_data'] = provider_data
        if photo_url is not None: params['photo_url'] = photo_url
        if photo_size is not None: params['photo_size'] = photo_size
        if photo_width is not None: params['photo_width'] = photo_width
        if photo_height is not None: params['photo_height'] = photo_height
        if need_name is not None: params['need_name'] = need_name
        if need_phone_number is not None: params['need_phone_number'] = need_phone_number
        if need_email is not None: params['need_email'] = need_email
        if need_shipping_address is not None: params['need_shipping_address'] = need_shipping_address
        if send_phone_number_to_provider is not None: params['send_phone_number_to_provider'] = send_phone_number_to_provider
        if send_email_to_provider is not None: params['send_email_to_provider'] = send_email_to_provider
        if is_flexible is not None: params['is_flexible'] = is_flexible
        if disable_notification is not None: params['disable_notification'] = disable_notification
        if protect_content is not None: params['protect_content'] = protect_content
        if reply_to_message_id is not None: params['reply_to_message_id'] = reply_to_message_id
        if allow_sending_without_reply is not None: params['allow_sending_without_reply'] = allow_sending_without_reply
        if reply_markup is not None: params['reply_markup'] = reply_markup
        result = await super().send_invoice(params)
        return Message.dese(result)

    async def create_invoice_link(
        self, title: str, description: str, payload: str, provider_token: str, currency: str,
        prices: List[LabeledPrice], max_tip_amount: int|None=None, suggested_tip_amounts: List[int]|None=None,
        provider_data: str|None=None, photo_url: str|None=None, photo_size: int|None=None, photo_width: int|None=None,
        photo_height: int|None=None, need_name: bool|None=None, need_phone_number: bool|None=None, need_email: bool|None=None,
        need_shipping_address: bool|None=None, send_phone_number_to_provider: bool|None=None, send_email_to_provider: bool|None=None, is_flexible: bool|None=None
    ) -> str:
        params = {}
        params['title'] = title
        params['description'] = description
        params['payload'] = payload
        params['provider_token'] = provider_token
        params['currency'] = currency
        params['prices'] = prices
        if max_tip_amount is not None: params['max_tip_amount'] = max_tip_amount
        if suggested_tip_amounts is not None: params['suggested_tip_amounts'] = suggested_tip_amounts
        if provider_data is not None: params['provider_data'] = provider_data
        if photo_url is not None: params['photo_url'] = photo_url
        if photo_size is not None: params['photo_size'] = photo_size
        if photo_width is not None: params['photo_width'] = photo_width
        if photo_height is not None: params['photo_height'] = photo_height
        if need_name is not None: params['need_name'] = need_name
        if need_phone_number is not None: params['need_phone_number'] = need_phone_number
        if need_email is not None: params['need_email'] = need_email
        if need_shipping_address is not None: params['need_shipping_address'] = need_shipping_address
        if send_phone_number_to_provider is not None: params['send_phone_number_to_provider'] = send_phone_number_to_provider
        if send_email_to_provider is not None: params['send_email_to_provider'] = send_email_to_provider
        if is_flexible is not None: params['is_flexible'] = is_flexible
        result = await super().create_invoice_link(params)
        return result

    async def answer_shipping_query(
        self, shipping_query_id: str, ok: bool,
        shipping_options: List[ShippingOption]|None=None, error_message: str|None=None
    ) -> True:
        params = {}
        params['shipping_query_id'] = shipping_query_id
        params['ok'] = ok
        if shipping_options is not None: params['shipping_options'] = shipping_options
        if error_message is not None: params['error_message'] = error_message
        result = await super().answer_shipping_query(params)
        return result

    async def answer_pre_checkout_query(
        self, pre_checkout_query_id: str,
        ok: bool, error_message: str|None=None
    ) -> True:
        params = {}
        params['pre_checkout_query_id'] = pre_checkout_query_id
        params['ok'] = ok
        if error_message is not None: params['error_message'] = error_message
        result = await super().answer_pre_checkout_query(params)
        return result

    async def set_passport_data_errors(self, user_id: int, errors: List[PassportElementError]) -> True:
        params = {}
        params['user_id'] = user_id
        params['errors'] = errors
        result = await super().set_passport_data_errors(params)
        return result

    async def send_game(
        self, chat_id: int, game_short_name: str, message_thread_id: int|None=None,
        disable_notification: bool|None=None, protect_content: bool|None=None, reply_to_message_id: int|None=None,
        allow_sending_without_reply: bool|None=None, reply_markup: InlineKeyboardMarkup|None=None
    ) -> Message:
        params = {}
        params['chat_id'] = chat_id
        params['game_short_name'] = game_short_name
        if message_thread_id is not None: params['message_thread_id'] = message_thread_id
        if disable_notification is not None: params['disable_notification'] = disable_notification
        if protect_content is not None: params['protect_content'] = protect_content
        if reply_to_message_id is not None: params['reply_to_message_id'] = reply_to_message_id
        if allow_sending_without_reply is not None: params['allow_sending_without_reply'] = allow_sending_without_reply
        if reply_markup is not None: params['reply_markup'] = reply_markup
        result = await super().send_game(params)
        return Message.dese(result)

    async def set_game_score(
        self, user_id: int, score: int, force: bool|None=None, disable_edit_message: bool|None=None,
        chat_id: int|None=None, message_id: int|None=None, inline_message_id: str|None=None
    ) -> Union[Message, True]:
        params = {}
        params['user_id'] = user_id
        params['score'] = score
        if force is not None: params['force'] = force
        if disable_edit_message is not None: params['disable_edit_message'] = disable_edit_message
        if chat_id is not None: params['chat_id'] = chat_id
        if message_id is not None: params['message_id'] = message_id
        if inline_message_id is not None: params['inline_message_id'] = inline_message_id
        result = await super().set_game_score(params)
        # this to prevent errors of inline messages that return "True"
        return Message.dese(result) if result is not True else True

    async def get_game_high_scores(
        self, user_id: int, chat_id: int|None=None,
        message_id: int|None=None, inline_message_id: str|None=None
    ) -> List[GameHighScore]:
        params = {}
        params['user_id'] = user_id
        if chat_id is not None: params['chat_id'] = chat_id
        if message_id is not None: params['message_id'] = message_id
        if inline_message_id is not None: params['inline_message_id'] = inline_message_id
        result = await super().get_game_high_scores(params)
        return [GameHighScore.dese(score) for score in result]

    def manage_message(self, lambda_=lambda message: True) -> None:
        def deco(func: Any):
            self._message_managers.append({'lambda': lambda_, 'func': func})
        return deco
    def manage_edited_message(self, lambda_=lambda edited_message: True) -> None:
        def deco(func: Any):
            self._edited_message_managers.append({'lambda': lambda_, 'func': func})
        return deco
    def manage_channel_post(self, lambda_=lambda channel_post: True) -> None:
        def deco(func: Any):
            self._channel_post_managers.append({'lambda': lambda_, 'func': func})
        return deco
    def manage_edited_channel_post(self, lambda_=lambda edited_channel_post: True) -> None:
        def deco(func: Any):
            self._edited_channel_post_managers.append({'lambda': lambda_, 'func': func})
        return deco
    def manage_callback_query(self, lambda_=lambda callback_query: True) -> None:
        def deco(func: Any):
            self._callback_query_managers.append({'lambda': lambda_, 'func': func})
        return deco
    def manage_inline_query(self, lambda_=lambda inline_query: True) -> None:
        def deco(func: Any):
            self._inline_query_managers.append({'lambda': lambda_, 'func': func})
        return deco
    def manage_chosen_inline_result(self, lambda_=lambda chosen_inline_result: True) -> None:
        def deco(func: Any):
            self._chosen_inline_result_managers.append({'lambda': lambda_, 'func': func})
        return deco
    def manage_shipping_query(self, lambda_=lambda shipping_query: True) -> None:
        def deco(func: Any):
            self._shipping_query_managers.append({'lambda': lambda_, 'func': func})
        return deco
    def manage_pre_checkout_query(self, lambda_=lambda pre_checkout_query: True) -> None:
        def deco(func: Any):
            self._pre_checkout_query_managers.append({'lambda': lambda_, 'func': func})
        return deco
    def manage_poll(self, lambda_=lambda poll: True) -> None:
        def deco(func: Any):
            self._poll_managers.append({'lambda': lambda_, 'func': func})
        return deco
    def manage_poll_answer(self, lambda_=lambda poll_answer: True) -> None:
        def deco(func: Any):
            self._poll_answer_managers.append({'lambda': lambda_, 'func': func})
        return deco
    def manage_my_chat_member(self, lambda_=lambda my_chat_member: True) -> None:
        def deco(func: Any):
            self._my_chat_member_managers.append({'lambda': lambda_, 'func': func})
        return deco
    def manage_chat_member(self, lambda_=lambda chat_member: True) -> None:
        def deco(func: Any):
            self._chat_member_managers.append({'lambda': lambda_, 'func': func})
        return deco
    def manage_chat_join_request(self, lambda_=lambda chat_join_request: True) -> None:
        def deco(func: Any):
            self._chat_join_request_managers.append({'lambda': lambda_, 'func': func})
        return deco


    async def long_polling(self, timeout: int = 30) -> None:

        try:
            bot = await self.get_me()
        except TelegramError as err:
            raise TelegramError(str(err) + ', probably the token is wrong.')

        logger.info('Hi {}!'.format(bot.username))

        super().start_polling()

        while True:
            offset = self.offset if self.offset is not None else None
            try:
                updates = await self.get_updates(offset=offset, timeout=timeout)

            except (ClientError, TimeoutError):
                if not self.session.closed:
                    await self.session.close()
                await super().fix_polling()

            except:
                if not self.session.closed:
                    await self.session.close()
                raise

            else:
                if updates:
                    self.offset = updates[-1].update_id +1
                    for update in updates:
                        await asyncio.create_task(self.__process_update(update))


    async def __process_update(self, update: Update):
            if hasattr(update, 'message'):
                for rule in self._message_managers:
                    lambda_: Any = rule['lambda']
                    if lambda_(update.message):
                        func = rule['func']
                        try:
                            _return = await func(update.message)
                        except (ClientError, TimeoutError, TelegramError):
                            pass
                        except:
                            if not self.session.closed:
                                await self.session.close()
                            raise
                        else:
                            if not isinstance(_return, NextManager):
                               return

            elif hasattr(update, 'edited_message'):
                for rule in self._edited_message_managers:
                    lambda_: Any = rule['lambda']
                    if lambda_(update.edited_message):
                        func = rule['func']
                        try:
                            _return = await func(update.edited_message)
                        except (ClientError, TimeoutError, TelegramError):
                            pass
                        except:
                            if not self.session.closed:
                                await self.session.close()
                            raise
                        else:
                            if not isinstance(_return, NextManager):
                               return

            elif hasattr(update, 'channel_post'):
                for rule in self._channel_post_managers:
                    lambda_: Any = rule['lambda']
                    if lambda_(update.channel_post):
                        func = rule['func']
                        try:
                            _return = await func(update.channel_post)
                        except (ClientError, TimeoutError, TelegramError):
                            pass
                        except:
                            if not self.session.closed:
                                await self.session.close()
                            raise
                        else:
                            if not isinstance(_return, NextManager):
                               return

            elif hasattr(update, 'edited_channel_post'):
                for rule in self._edited_channel_post_managers:
                    lambda_: Any = rule['lambda']
                    if lambda_(update.edited_channel_post):
                        func = rule['func']
                        try:
                            _return = await func(update.edited_channel_post)
                        except (ClientError, TimeoutError, TelegramError):
                            pass
                        except:
                            if not self.session.closed:
                                await self.session.close()
                            raise
                        else:
                            if not isinstance(_return, NextManager):
                               return

            elif hasattr(update, 'callback_query'):
                for rule in self._callback_query_managers:
                    lambda_: Any = rule['lambda']
                    if lambda_(update.callback_query):
                        func = rule['func']
                        try:
                            _return = await func(update.callback_query)
                        except (ClientError, TimeoutError, TelegramError):
                            pass
                        except:
                            if not self.session.closed:
                                await self.session.close()
                            raise
                        else:
                            if not isinstance(_return, NextManager):
                               return

            elif hasattr(update, 'inline_query'):
                print('its an inline_query update')
                for rule in self._inline_query_managers:
                    lambda_: Any = rule['lambda']
                    if lambda_(update.inline_query):
                        func = rule['func']
                        try:
                            _return = await func(update.inline_query)
                        except (ClientError, TimeoutError, TelegramError):
                            pass
                        except:
                            if not self.session.closed:
                                await self.session.close()
                            raise
                        else:
                            if not isinstance(_return, NextManager):
                               return

            elif hasattr(update, 'chosen_inline_result'):
                print('its a chosen_inline_result update')
                for rule in self._chosen_inline_result_managers:
                    lambda_: Any = rule['lambda']
                    if lambda_(update.chosen_inline_result):
                        func = rule['func']
                        try:
                            _return = await func(update.chosen_inline_result)
                        except (ClientError, TimeoutError, TelegramError):
                            pass
                        except:
                            if not self.session.closed:
                                await self.session.close()
                            raise
                        else:
                            if not isinstance(_return, NextManager):
                               return

            elif hasattr(update, 'shipping_query'):
                print('its a shipping_query update')
                for rule in self._shipping_query_managers:
                    lambda_: Any = rule['lambda']
                    if lambda_(update.shipping_query):
                        func = rule['func']
                        try:
                            _return = await func(update.shipping_query)
                        except (ClientError, TimeoutError, TelegramError):
                            pass
                        except:
                            if not self.session.closed:
                                await self.session.close()
                            raise
                        else:
                            if not isinstance(_return, NextManager):
                               return

            elif hasattr(update, 'pre_checkout_query'):
                print('its a pre_checkout_query update')
                for rule in self._pre_checkout_query_managers:
                    lambda_: Any = rule['lambda']
                    if lambda_(update.pre_checkout_query):
                        func = rule['func']
                        try:
                            _return = await func(update.pre_checkout_query)
                        except (ClientError, TimeoutError, TelegramError):
                            pass
                        except:
                            if not self.session.closed:
                                await self.session.close()
                            raise
                        else:
                            if not isinstance(_return, NextManager):
                               return

            elif hasattr(update, 'poll'):
                print('its a poll update')
                for rule in self._poll_managers:
                    lambda_: Any = rule['lambda']
                    if lambda_(update.poll):
                        func = rule['func']
                        try:
                            _return = await func(update.poll)
                        except (ClientError, TimeoutError, TelegramError):
                            pass
                        except:
                            if not self.session.closed:
                                await self.session.close()
                            raise
                        else:
                            if not isinstance(_return, NextManager):
                               return

            elif hasattr(update, 'poll_answer'):
                print('its a poll_answer update')
                for rule in self._poll_answer_managers:
                    lambda_: Any = rule['lambda']
                    if lambda_(update.poll_answer):
                        func = rule['func']
                        try:
                            _return = await func(update.poll_answer)
                        except (ClientError, TimeoutError, TelegramError):
                            pass
                        except:
                            if not self.session.closed:
                                await self.session.close()
                            raise
                        else:
                            if not isinstance(_return, NextManager):
                               return

            elif hasattr(update, 'my_chat_member'):
                print('its a my_chat_member update')
                for rule in self._my_chat_member_managers:
                    lambda_: Any = rule['lambda']
                    if lambda_(update.my_chat_member):
                        func = rule['func']
                        try:
                            _return = await func(update.my_chat_member)
                        except (ClientError, TimeoutError, TelegramError):
                            pass
                        except:
                            if not self.session.closed:
                                await self.session.close()
                            raise
                        else:
                            if not isinstance(_return, NextManager):
                               return

            elif hasattr(update, 'chat_member'):
                print('its a chat_member update')
                for rule in self._chat_member_managers:
                    lambda_: Any = rule['lambda']
                    if lambda_(update.chat_member):
                        func = rule['func']
                        try:
                            _return = await func(update.chat_member)
                        except (ClientError, TimeoutError, TelegramError):
                            pass
                        except:
                            if not self.session.closed:
                                await self.session.close()
                            raise
                        else:
                            if not isinstance(_return, NextManager):
                               return

            elif hasattr(update, 'chat_join_request'):
                print('its a chat_join_request update')
                for rule in self._chat_join_request_managers:
                    lambda_: Any = rule['lambda']
                    if lambda_(update.chat_join_request):
                        func = rule['func']
                        try:
                            _return = await func(update.chat_join_request)
                        except (ClientError, TimeoutError, TelegramError):
                            pass
                        except:
                            if not self.session.closed:
                                await self.session.close()
                            raise
                        else:
                            if not isinstance(_return, NextManager):
                               return


