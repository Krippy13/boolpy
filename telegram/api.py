#!/bin/python3

from boolpy.logger import get_logger

logger = get_logger('TelegramApi')

# $ # $ # $ # $ # $ # $ # $ # $ #

import asyncio

from aiohttp.client import (ClientError,
                            ClientSession,
                            ClientResponse)

#from aiohttp.formdata import FormData

from typing import Optional
from boolpy.json_manager import prepare_for_json

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:119.0) Gecko/20100101 Firefox/119.0'}

class TelegramError(BaseException):
    """Class to handle errors with the requests to Telegram."""

class NextManager:
    """A new update will be processed by the next manager \
returning an instance of this class on your decorated functions."""

# $ # $ # $ # $ # $ # $ # $ # $ # # $ # $ # $ # $ # $ # $ # $ # $ # $ #

class TelegramApi:

    def __init__(
        self,
        token: str,
        proxy: Optional[str] = None
    ):
        self.token = token
        self.proxy = proxy

        self.base_url = 'https://api.telegram.org'

        logger.info(f'Proxy: {proxy}')

        self.session: Optional[ClientSession] = None

        self.__polling_status = False

# $ # $ # $ # $ # $ # $ # $ # $ # $ #

    @property
    def polling_status(self) -> bool:
        return self.__polling_status

    @polling_status.setter
    def polling_status(self, value) -> None:
        logger.info("polling_status attribute can't be set manually")

    @polling_status.deleter
    def polling_status(self) -> None:
        logger.info("polling_status attribute can't be deleted")

    def start_polling(self) -> bool:
        self.__polling_status = True
        logger.debug(f"polling_status is now {self.polling_status}")
        return self.polling_status

    def stop_polling(self) -> bool:
        self.__polling_status = False
        logger.debug(f"polling_status is now {self.polling_status}")
        return self.polling_status

# $ # $ # $ # $ # $ # $ # $ # $ #

    @staticmethod
    async def check_json(response: ClientResponse):

        result = await response.json()

        if response.ok is True:
            return result['result']
        else:
            raise TelegramError(result['description'])

# $ # $ # $ # $ # $ # $ # $ # $ # $ # $ # $ # $ # $ #

    async def get_session(self) -> ClientSession:

        if (self.session is None
            or self.session.closed):

            self.session = ClientSession(self.base_url)
            logger.debug('A new session was initialized')

        return self.session

# $ # $ # $ # $ # $ # $ # $

    async def fix_polling(self) -> bool:

        self.stop_polling()

        logger.info('Connection lost, long polling was interrupted')

        while True:
            try:
                session = ClientSession(self.base_url)
                await session.get(
                    url = '/',
                    proxy = self.proxy,
                    headers = HEADERS
                )
            except (ClientError, TimeoutError):
                await session.close()
            except:
                await session.close()
                raise
            else:
                self.session = session
                logger.info('Connection ok, long polling has been resumed')

                return self.start_polling()

            await asyncio.sleep(3)

# $ # $ # $ # $ # $ # $ # $ # $ #

    async def request(
        self,
        method: str,
        params: Optional[dict] = None
    ):
        self.session = await self.get_session()
        try:
            async with self.session.get(
                url = '/bot{0}/{1}'.format(self.token, method),
                json = params,
                proxy = self.proxy,
                headers = HEADERS

            ) as response:
                return await self.check_json(response)

        except BaseException as err:

            if (self.polling_status is False
                and not self.session.closed):

                await self.session.close()

            logger.error(f'{type(err).__name__}! {err}')
            raise

# $ # $ # $ # $ #

    async def get_updates(self, params: dict) -> dict:
        method = 'getUpdates'
        return await self.request(method, params)

    async def get_me(self) -> dict:
        method = 'getMe'
        return await self.request(method)

    async def send_message(self, params: dict) -> dict:
        method = 'sendMessage'
        if 'entities' in params:
            params['entities'] = prepare_for_json(params['entities'])
        if 'reply_markup' in params:
            params['reply_markup'] = prepare_for_json(params['reply_markup'])
        return await self.request(method, params)

    async def log_out(self) -> dict:
        method = 'logOut'
        return await self.request(method)

    async def close(self) -> dict:
        method = 'close'
        return await self.request(method)

    async def forward_message(self, params: dict) -> dict:
        method = 'forwardMessage'
        return await self.request(method, params)

    async def copy_message(self, params: dict) -> dict:
        method = 'copyMessage'
        if 'caption_entities' in params:
            params['caption_entities'] = prepare_for_json(params['caption_entities'])
        if 'reply_markup' in params:
            params['reply_markup'] = prepare_for_json(params['reply_markup'])
        return await self.request(method, params)

    async def send_photo(self, params: dict) -> dict:
        method = 'sendPhoto'
        if 'photo' in params:
            params['photo'] = prepare_for_json(params['photo'])
        if 'caption_entities' in params:
            params['caption_entities'] = prepare_for_json(params['caption_entities'])
        if 'reply_markup' in params:
            params['reply_markup'] = prepare_for_json(params['reply_markup'])
        return await self.request(method, params)

    async def send_audio(self, params: dict) -> dict:
        method = 'sendAudio'
        if 'audio' in params:
            params['audio'] = prepare_for_json(params['audio'])
        if 'caption_entities' in params:
            params['caption_entities'] = prepare_for_json(params['caption_entities'])
        if 'thumbnail' in params:
            params['thumbnail'] = prepare_for_json(params['thumbnail'])
        if 'reply_markup' in params:
            params['reply_markup'] = prepare_for_json(params['reply_markup'])
        return await self.request(method, params)

    async def send_document(self, params: dict) -> dict:
        method = 'sendDocument'
        if 'document' in params:
            params['document'] = prepare_for_json(params['document'])
        if 'thumbnail' in params:
            params['thumbnail'] = prepare_for_json(params['thumbnail'])
        if 'caption_entities' in params:
            params['caption_entities'] = prepare_for_json(params['caption_entities'])
        if 'reply_markup' in params:
            params['reply_markup'] = prepare_for_json(params['reply_markup'])
        return await self.request(method, params)

    async def send_video(self, params: dict) -> dict:
        method = 'sendVideo'
        if 'video' in params:
            params['video'] = prepare_for_json(params['video'])
        if 'thumbnail' in params:
            params['thumbnail'] = prepare_for_json(params['thumbnail'])
        if 'caption_entities' in params:
            params['caption_entities'] = prepare_for_json(params['caption_entities'])
        if 'reply_markup' in params:
            params['reply_markup'] = prepare_for_json(params['reply_markup'])
        return await self.request(method, params)

    async def send_animation(self, params: dict) -> dict:
        method = 'sendAnimation'
        if 'animation' in params:
            params['animation'] = prepare_for_json(params['animation'])
        if 'thumbnail' in params:
            params['thumbnail'] = prepare_for_json(params['thumbnail'])
        if 'caption_entities' in params:
            params['caption_entities'] = prepare_for_json(params['caption_entities'])
        if 'reply_markup' in params:
            params['reply_markup'] = prepare_for_json(params['reply_markup'])
        return await self.request(method, params)

    async def send_voice(self, params: dict) -> dict:
        method = 'sendVoice'
        if 'voice' in params:
            params['voice'] = prepare_for_json(params['voice'])
        if 'caption_entities' in params:
            params['caption_entities'] = prepare_for_json(params['caption_entities'])
        if 'reply_markup' in params:
            params['reply_markup'] = prepare_for_json(params['reply_markup'])
        return await self.request(method, params)

    async def send_video_note(self, params: dict) -> dict:
        method = 'sendVideoNote'
        if 'video_note' in params:
            params['video_note'] = prepare_for_json(params['video_note'])
        if 'thumbnail' in params:
            params['thumbnail'] = prepare_for_json(params['thumbnail'])
        if 'reply_markup' in params:
            params['reply_markup'] = prepare_for_json(params['reply_markup'])
        return await self.request(method, params)

    async def send_media_group(self, params: dict) -> dict:
        method = 'sendMediaGroup'
        if 'media' in params:
            params['media'] = prepare_for_json(params['media'])
        return await self.request(method, params)

    async def send_location(self, params: dict) -> dict:
        method = 'sendLocation'
        if 'reply_markup' in params:
            params['reply_markup'] = prepare_for_json(params['reply_markup'])
        return await self.request(method, params)

    async def send_venue(self, params: dict) -> dict:
        method = 'sendVenue'
        if 'reply_markup' in params:
            params['reply_markup'] = prepare_for_json(params['reply_markup'])
        return await self.request(method, params)

    async def send_contact(self, params: dict) -> dict:
        method = 'sendContact'
        if 'reply_markup' in params:
            params['reply_markup'] = prepare_for_json(params['reply_markup'])
        return await self.request(method, params)

    async def send_poll(self, params: dict) -> dict:
        method = 'sendPoll'
        if 'explanation_entities' in params:
            params['explanation_entities'] = prepare_for_json(params['explanation_entities'])
        if 'reply_markup' in params:
            params['reply_markup'] = prepare_for_json(params['reply_markup'])
        return await self.request(method, params)

    async def send_dice(self, params: dict) -> dict:
        method = 'sendDice'
        if 'reply_markup' in params:
            params['reply_markup'] = prepare_for_json(params['reply_markup'])
        return await self.request(method, params)

    async def send_chat_action(self, params: dict) -> dict:
        method = 'sendChatAction'
        return await self.request(method, params)

    async def get_user_profile_photos(self, params: dict) -> dict:
        method = 'getUserProfilePhotos'
        return await self.request(method, params)

    async def get_file(self, params: dict) -> dict:
        method = 'getFile'
        return await self.request(method, params)

    async def ban_chat_member(self, params: dict) -> dict:
        method = 'banChatMember'
        return await self.request(method, params)

    async def unban_chat_member(self, params: dict) -> dict:
        method = 'unbanChatMember'
        return await self.request(method, params)

    async def restrict_chat_member(self, params: dict) -> dict:
        method = 'restrictChatMember'
        if 'permissions' in params:
            params['permissions'] = prepare_for_json(params['permissions'])
        return await self.request(method, params)

    async def promote_chat_member(self, params: dict) -> dict:
        method = 'promoteChatMember'
        return await self.request(method, params)

    async def set_chat_administrator_custom_title(self, params: dict) -> dict:
        method = 'setChatAdministratorCustomTitle'
        return await self.request(method, params)

    async def ban_chat_sender_chat(self, params: dict) -> dict:
        method = 'banChatSenderChat'
        return await self.request(method, params)

    async def unban_chat_sender_chat(self, params: dict) -> dict:
        method = 'unbanChatSenderChat'
        return await self.request(method, params)

    async def set_chat_permissions(self, params: dict) -> dict:
        method = 'setChatPermissions'
        if 'permissions' in params:
            params['permissions'] = prepare_for_json(params['permissions'])
        return await self.request(method, params)

    async def export_chat_invite_link(self, params: dict) -> dict:
        method = 'exportChatInviteLink'
        return await self.request(method, params)

    async def create_chat_invite_link(self, params: dict) -> dict:
        method = 'createChatInviteLink'
        return await self.request(method, params)

    async def edit_chat_invite_link(self, params: dict) -> dict:
        method = 'editChatInviteLink'
        return await self.request(method, params)

    async def revoke_chat_invite_link(self, params: dict) -> dict:
        method = 'revokeChatInviteLink'
        return await self.request(method, params)

    async def approve_chat_join__request(self, params: dict) -> dict:
        method = 'approveChatJoinRequest'
        return await self.request(method, params)

    async def decline_chat_join__request(self, params: dict) -> dict:
        method = 'declineChatJoinRequest'
        return await self.request(method, params)

    async def set_chat_photo(self, params: dict) -> dict:
        method = 'setChatPhoto'
        if 'photo' in params:
            params['photo'] = prepare_for_json(params['photo'])
        return await self.request(method, params)

    async def delete_chat_photo(self, params: dict) -> dict:
        method = 'deleteChatPhoto'
        return await self.request(method, params)

    async def set_chat_title(self, params: dict) -> dict:
        method = 'setChatTitle'
        return await self.request(method, params)

    async def set_chat_description(self, params: dict) -> dict:
        method = 'setChatDescription'
        return await self.request(method, params)

    async def pin_chat_message(self, params: dict) -> dict:
        method = 'pinChatMessage'
        return await self.request(method, params)

    async def unpin_chat_message(self, params: dict) -> dict:
        method = 'unpinChatMessage'
        return await self.request(method, params)

    async def unpin_all_chat_messages(self, params: dict) -> dict:
        method = 'unpinAllChatMessages'
        return await self.request(method, params)

    async def leave_chat(self, params: dict) -> dict:
        method = 'leaveChat'
        return await self.request(method, params)

    async def get_chat(self, params: dict) -> dict:
        method = 'getChat'
        return await self.request(method, params)

    async def get_chat_administrators(self, params: dict) -> dict:
        method = 'getChatAdministrators'
        return await self.request(method, params)

    async def get_chat_member_count(self, params: dict) -> dict:
        method = 'getChatMemberCount'
        return await self.request(method, params)

    async def get_chat_member(self, params: dict) -> dict:
        method = 'getChatMember'
        return await self.request(method, params)

    async def set_chat_sticker_set(self, params: dict) -> dict:
        method = 'setChatStickerSet'
        return await self.request(method, params)

    async def delete_chat_sticker_set(self, params: dict) -> dict:
        method = 'deleteChatStickerSet'
        return await self.request(method, params)

    async def get_forum_topic_icon_stickers(self) -> dict:
        method = 'getForumTopicIconStickers'
        return await self.request(method)

    async def create_forum_topic(self, params: dict) -> dict:
        method = 'createForumTopic'
        return await self.request(method, params)

    async def edit_forum_topic(self, params: dict) -> dict:
        method = 'editForumTopic'
        return await self.request(method, params)

    async def close_forum_topic(self, params: dict) -> dict:
        method = 'closeForumTopic'
        return await self.request(method, params)

    async def reopen_forum_topic(self, params: dict) -> dict:
        method = 'reopenForumTopic'
        return await self.request(method, params)

    async def delete_forum_topic(self, params: dict) -> dict:
        method = 'deleteForumTopic'
        return await self.request(method, params)

    async def unpin_all_forum_topic_messages(self, params: dict) -> dict:
        method = 'unpinAllForumTopicMessages'
        return await self.request(method, params)

    async def edit_general_forum_topic(self, params: dict) -> dict:
        method = 'editGeneralForumTopic'
        return await self.request(method, params)

    async def close_general_forum_topic(self, params: dict) -> dict:
        method = 'closeGeneralForumTopic'
        return await self.request(method, params)

    async def reopen_general_forum_topic(self, params: dict) -> dict:
        method = 'reopenGeneralForumTopic'
        return await self.request(method, params)

    async def hide_general_forum_topic(self, params: dict) -> dict:
        method = 'hideGeneralForumTopic'
        return await self.request(method, params)

    async def unhide_general_forum_topic(self, params: dict) -> dict:
        method = 'unhideGeneralForumTopic'
        return await self.request(method, params)

    async def unpin_all_general_forum_topic_messages(self, params: dict) -> dict:
        method = 'unpinAllGeneralForumTopicMessages'
        return await self.request(method, params)

    async def answer_callback_query(self, params: dict) -> dict:
        method = 'answerCallbackQuery'
        return await self.request(method, params)

    async def set_my_commands(self, params: dict) -> dict:
        method = 'setMyCommands'
        if 'commands' in params:
            params['commands'] = prepare_for_json(params['commands'])
        if 'scope' in params:
            params['scope'] = prepare_for_json(params['scope'])
        return await self.request(method, params)

    async def delete_my_commands(self, params: dict) -> dict:
        method = 'deleteMyCommands'
        if 'scope' in params:
            params['scope'] = prepare_for_json(params['scope'])
        return await self.request(method, params)

    async def get_my_commands(self, params: dict) -> dict:
        method = 'getMyCommands'
        if 'scope' in params:
            params['scope'] = prepare_for_json(params['scope'])
        return await self.request(method, params)

    async def set_my_name(self, params: dict) -> dict:
        method = 'setMyName'
        return await self.request(method, params)

    async def get_my_name(self, params: dict) -> dict:
        method = 'getMyName'
        return await self.request(method, params)

    async def set_my_description(self, params: dict) -> dict:
        method = 'setMyDescription'
        return await self.request(method, params)

    async def get_my_description(self, params: dict) -> dict:
        method = 'getMyDescription'
        return await self.request(method, params)

    async def set_my_short_description(self, params: dict) -> dict:
        method = 'setMyShortDescription'
        return await self.request(method, params)

    async def get_my_short_description(self, params: dict) -> dict:
        method = 'getMyShortDescription'
        return await self.request(method, params)

    async def set_chat_menu_button(self, params: dict) -> dict:
        method = 'setChatMenuButton'
        if 'menu_button' in params:
            params['menu_button'] = prepare_for_json(params['menu_button'])
        return await self.request(method, params)

    async def get_chat_menu_button(self, params: dict) -> dict:
        method = 'getChatMenuButton'
        return await self.request(method, params)

    async def set_my_default_administrator_rights(self, params: dict) -> dict:
        method = 'setMyDefaultAdministratorRights'
        if 'rights' in params:
            params['rights'] = prepare_for_json(params['rights'])
        return await self.request(method, params)

    async def get_my_default_administrator_rights(self, params: dict) -> dict:
        method = 'getMyDefaultAdministratorRights'
        return await self.request(method, params)

    async def edit_message_text(self, params: dict) -> dict:
        method = 'editMessageText'
        if 'entities' in params:
            params['entities'] = prepare_for_json(params['entities'])
        if 'reply_markup' in params:
            params['reply_markup'] = prepare_for_json(params['reply_markup'])
        return await self.request(method, params)

    async def edit_message_caption(self, params: dict) -> dict:
        method = 'editMessageCaption'
        if 'caption_entities' in params:
            params['caption_entities'] = prepare_for_json(params['caption_entities'])
        if 'reply_markup' in params:
            params['reply_markup'] = prepare_for_json(params['reply_markup'])
        return await self.request(method, params)

    async def edit_message_media(self, params: dict) -> dict:
        method = 'editMessageMedia'
        if 'media' in params:
            params['media'] = prepare_for_json(params['media'])
        if 'reply_markup' in params:
            params['reply_markup'] = prepare_for_json(params['reply_markup'])
        return await self.request(method, params)

    async def edit_message_live_location(self, params: dict) -> dict:
        method = 'editMessageLiveLocation'
        if 'reply_markup' in params:
            params['reply_markup'] = prepare_for_json(params['reply_markup'])
        return await self.request(method, params)

    async def stop_message_live_location(self, params: dict) -> dict:
        method = 'stopMessageLiveLocation'
        if 'reply_markup' in params:
            params['reply_markup'] = prepare_for_json(params['reply_markup'])
        return await self.request(method, params)

    async def edit_message_reply_markup(self, params: dict) -> dict:
        method = 'editMessageReplyMarkup'
        if 'reply_markup' in params:
            params['reply_markup'] = prepare_for_json(params['reply_markup'])
        return await self.request(method, params)

    async def stop_poll(self, params: dict) -> dict:
        method = 'stopPoll'
        if 'reply_markup' in params:
            params['reply_markup'] = prepare_for_json(params['reply_markup'])
        return await self.request(method, params)

    async def delete_message(self, params: dict) -> dict:
        method = 'deleteMessage'
        return await self.request(method, params)

    async def send_sticker(self, params: dict) -> dict:
        method = 'sendSticker'
        if 'sticker' in params:
            params['sticker'] = prepare_for_json(params['sticker'])
        if 'reply_markup' in params:
            params['reply_markup'] = prepare_for_json(params['reply_markup'])
        return await self.request(method, params)

    async def get_sticker_set(self, params: dict) -> dict:
        method = 'getStickerSet'
        return await self.request(method, params)

    async def get_custom_emoji_stickers(self, params: dict) -> dict:
        method = 'getCustomEmojiStickers'
        return await self.request(method, params)

    async def upload_sticker_file(self, params: dict) -> dict:
        method = 'uploadStickerFile'
        if 'sticker' in params:
            params['sticker'] = prepare_for_json(params['sticker'])
        return await self.request(method, params)

    async def create_new_sticker_set(self, params: dict) -> dict:
        method = 'createNewStickerSet'
        if 'stickers' in params:
            params['stickers'] = prepare_for_json(params['stickers'])
        return await self.request(method, params)

    async def add_sticker_to_set(self, params: dict) -> dict:
        method = 'addStickerToSet'
        if 'sticker' in params:
            params['sticker'] = prepare_for_json(params['sticker'])
        return await self.request(method, params)

    async def set_sticker_position_in_set(self, params: dict) -> dict:
        method = 'setStickerPositionInSet'
        return await self.request(method, params)

    async def delete_sticker_from_set(self, params: dict) -> dict:
        method = 'deleteStickerFromSet'
        return await self.request(method, params)

    async def set_sticker_emoji_list(self, params: dict) -> dict:
        method = 'setStickerEmojiList'
        return await self.request(method, params)

    async def set_sticker_keywords(self, params: dict) -> dict:
        method = 'setStickerKeywords'
        return await self.request(method, params)

    async def set_sticker_mask_position(self, params: dict) -> dict:
        method = 'setStickerMaskPosition'
        if 'mask_position' in params:
            params['mask_position'] = prepare_for_json(params['mask_position'])
        return await self.request(method, params)

    async def set_sticker_set_title(self, params: dict) -> dict:
        method = 'setStickerSetTitle'
        return await self.request(method, params)

    async def set_sticker_set_thumbnail(self, params: dict) -> dict:
        method = 'setStickerSetThumbnail'
        if 'thumbnail' in params:
            params['thumbnail'] = prepare_for_json(params['thumbnail'])
        return await self.request(method, params)

    async def set_custom_emoji_sticker_set_thumbnail(self, params: dict) -> dict:
        method = 'setCustomEmojiStickerSetThumbnail'
        return await self.request(method, params)

    async def delete_sticker_set(self, params: dict) -> dict:
        method = 'deleteStickerSet'
        return await self.request(method, params)

    async def answer_inline_query(self, params: dict) -> dict:
        method = 'answerInlineQuery'
        if 'results' in params:
            params['results'] = prepare_for_json(params['results'])
        if 'button' in params:
            params['button'] = prepare_for_json(params['button'])
        return await self.request(method, params)

    async def answer_web_app_query(self, params: dict) -> dict:
        method = 'answerWebAppQuery'
        if 'result' in params:
            params['result'] = prepare_for_json(params['result'])
        return await self.request(method, params)

    async def send_invoice(self, params: dict) -> dict:
        method = 'sendInvoice'
        if 'prices' in params:
            params['prices'] = prepare_for_json(params['prices'])
        if 'reply_markup' in params:
            params['reply_markup'] = prepare_for_json(params['reply_markup'])
        return await self.request(method, params)

    async def create_invoice_link(self, params: dict) -> dict:
        method = 'createInvoiceLink'
        if 'prices' in params:
            params['prices'] = prepare_for_json(params['prices'])
        return await self.request(method, params)

    async def answer_shipping_query(self, params: dict) -> dict:
        method = 'answerShippingQuery'
        if 'shipping_options' in params:
            params['shipping_options'] = prepare_for_json(params['shipping_options'])
        return await self.request(method, params)

    async def answer_pre_checkout_query(self, params: dict) -> dict:
        method = 'answerPreCheckoutQuery'
        return await self.request(method, params)

    async def set_passport_data_errors(self, params: dict) -> dict:
        method = 'setPassportDataErrors'
        if 'errors' in params:
            params['errors'] = prepare_for_json(params['errors'])
        return await self.request(method, params)

    async def send_game(self, params: dict) -> dict:
        method = 'sendGame'
        if 'reply_markup' in params:
            params['reply_markup'] = prepare_for_json(params['reply_markup'])
        return await self.request(method, params)

    async def set_game_score(self, params: dict) -> dict:
        method = 'setGameScore'
        return await self.request(method, params)

    async def get_game_high_scores(self, params: dict) -> dict:
        method = 'getGameHighScores'
        return await self.request(method, params)

