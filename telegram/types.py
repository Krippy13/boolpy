#!/bin/python3

from typing import Union, Optional, List
from boolpy.json_manager import check_dict

class ChatPermissions:
    @classmethod
    def dese(cls, json_):
        if json_ is None: return None
        obj = check_dict(json_)
        obj['can_send_messages'] = obj.get('can_send_messages')
        obj['can_send_audios'] = obj.get('can_send_audios')
        obj['can_send_documents'] = obj.get('can_send_documents')
        obj['can_send_photos'] = obj.get('can_send_photos')
        obj['can_send_videos'] = obj.get('can_send_videos')
        obj['can_send_video_notes'] = obj.get('can_send_video_notes')
        obj['can_send_voice_notes'] = obj.get('can_send_voice_notes')
        obj['can_send_polls'] = obj.get('can_send_polls')
        obj['can_send_other_messages'] = obj.get('can_send_other_messages')
        obj['can_add_web_page_previews'] = obj.get('can_add_web_page_previews')
        obj['can_change_info'] = obj.get('can_change_info')
        obj['can_invite_users'] = obj.get('can_invite_users')
        obj['can_pin_messages'] = obj.get('can_pin_messages')
        obj['can_manage_topics'] = obj.get('can_manage_topics')
        return cls(**obj)
    def __init__(
        self, can_send_messages: bool|None=None, can_send_audios: bool|None=None, can_send_documents: bool|None=None,
        can_send_photos: bool|None=None, can_send_videos: bool|None=None, can_send_video_notes: bool|None=None,
        can_send_voice_notes: bool|None=None, can_send_polls: bool|None=None, can_send_other_messages: bool|None=None,
        can_add_web_page_previews: bool|None=None, can_change_info: bool|None=None, can_invite_users: bool|None=None,
        can_pin_messages: bool|None=None, can_manage_topics: bool|None=None, **kwargs
    ):
        if can_send_messages is not None:
            self.can_send_messages = can_send_messages
        if can_send_audios is not None:
            self.can_send_audios = can_send_audios
        if can_send_documents is not None:
            self.can_send_documents = can_send_documents
        if can_send_photos is not None:
            self.can_send_photos = can_send_photos
        if can_send_videos is not None:
            self.can_send_videos = can_send_videos
        if can_send_video_notes is not None:
            self.can_send_video_notes = can_send_video_notes
        if can_send_voice_notes is not None:
            self.can_send_voice_notes = can_send_voice_notes
        if can_send_polls is not None:
            self.can_send_polls = can_send_polls
        if can_send_other_messages is not None:
            self.can_send_other_messages = can_send_other_messages
        if can_add_web_page_previews is not None:
            self.can_add_web_page_previews = can_add_web_page_previews
        if can_change_info is not None:
            self.can_change_info = can_change_info
        if can_invite_users is not None:
            self.can_invite_users = can_invite_users
        if can_pin_messages is not None:
            self.can_pin_messages = can_pin_messages
        if can_manage_topics is not None:
            self.can_manage_topics = can_manage_topics

class ChatAdministratorRights:
    @classmethod
    def dese(cls, json_):
        if json_ is None: return None
        obj = check_dict(json_)
        obj['is_anonymous'] = obj.get('is_anonymous')
        obj['can_manage_chat'] = obj.get('can_manage_chat')
        obj['can_delete_messages'] = obj.get('can_delete_messages')
        obj['can_manage_video_chats'] = obj.get('can_manage_video_chats')
        obj['can_restrict_members'] = obj.get('can_restrict_members')
        obj['can_promote_members'] = obj.get('can_promote_members')
        obj['can_change_info'] = obj.get('can_change_info')
        obj['can_invite_users'] = obj.get('can_invite_users')
        obj['can_post_messages'] = obj.get('can_post_messages')
        obj['can_edit_messages'] = obj.get('can_edit_messages')
        obj['can_pin_messages'] = obj.get('can_pin_messages')
        obj['can_post_stories'] = obj.get('can_post_stories')
        obj['can_edit_stories'] = obj.get('can_edit_stories')
        obj['can_delete_stories'] = obj.get('can_delete_stories')
        obj['can_manage_topics'] = obj.get('can_manage_topics')
        return cls(**obj)
    def __init__(
        self, is_anonymous: bool, can_manage_chat: bool, can_delete_messages: bool, can_manage_video_chats: bool, can_restrict_members: bool,
        can_promote_members: bool, can_change_info: bool, can_invite_users: bool, can_post_messages: bool|None=None, can_edit_messages: bool|None=None,
        can_pin_messages: bool|None=None, can_post_stories: bool|None=None, can_edit_stories: bool|None=None, can_delete_stories: bool|None=None,
        can_manage_topics: bool|None=None, **kwargs
    ):
        self.is_anonymous = is_anonymous
        self.can_manage_chat = can_manage_chat
        self.can_delete_messages = can_delete_messages
        self.can_manage_video_chats = can_manage_video_chats
        self.can_restrict_members = can_restrict_members
        self.can_promote_members = can_promote_members
        self.can_change_info = can_change_info
        self.can_invite_users = can_invite_users
        if can_post_messages is not None:
            self.can_post_messages = can_post_messages
        if can_edit_messages is not None:
            self.can_edit_messages = can_edit_messages
        if can_pin_messages is not None:
            self.can_pin_messages = can_pin_messages
        if can_post_stories is not None:
            self.can_post_stories = can_post_stories
        if can_edit_stories is not None:
            self.can_edit_stories = can_edit_stories
        if can_delete_stories is not None:
            self.can_delete_stories = can_delete_stories
        if can_manage_topics is not None:
            self.can_manage_topics = can_manage_topics

class SwitchInlineQueryChosenChat:
    @classmethod
    def dese(cls, json_):
        if json_ is None: return None
        obj = check_dict(json_)
        obj['query'] = obj.get('query')
        obj['allow_user_chats'] = obj.get('allow_user_chats')
        obj['allow_bot_chats'] = obj.get('allow_bot_chats')
        obj['allow_group_chats'] = obj.get('allow_group_chats')
        obj['allow_channel_chats'] = obj.get('allow_channel_chats')
        return cls(**obj)
    def __init__(
        self, query: str|None=None, allow_user_chats: bool|None=None, allow_bot_chats: bool|None=None,
        allow_group_chats: bool|None=None, allow_channel_chats: bool|None=None, **kwargs
    ):
        if query is not None:
            self.query = query
        if allow_user_chats is not None:
            self.allow_user_chats = allow_user_chats
        if allow_bot_chats is not None:
            self.allow_bot_chats = allow_bot_chats
        if allow_group_chats is not None:
            self.allow_group_chats = allow_group_chats
        if allow_channel_chats is not None:
            self.allow_channel_chats = allow_channel_chats

class CallbackGame:
    @classmethod
    def dese(cls, json_):
        if json_ is None: return None
        obj = check_dict(json_)
        return cls(**obj)
    def __init__(self, **kwargs):
        self.__dict__ = kwargs

class InputFile:
    @classmethod
    def dese(cls, json_):
        if json_ is None: return None
        obj = check_dict(json_)
        return cls(**obj)
    def __init__(self, **kwargs):
        self.__dict__ = kwargs

class MarkPosition:
    @classmethod
    def dese(cls, json_):
        if json_ is None: return None
        obj = check_dict(json_)
        obj['point'] = obj.get('point')
        obj['x_shift'] = obj.get('x_shift')
        obj['y_shift'] = obj.get('y_shift')
        obj['scale'] = obj.get('scale')
        return cls(**obj)
    def __init__(
        self, point: str, x_shift: float,
        y_shift: float, scale: float, **kwargs
    ):
        self.point = point
        self.x_shift = x_shift
        self.y_shift = y_shift
        self.scale = scale

class LoginUrl:
    @classmethod
    def dese(cls, json_):
        if json_ is None: return None
        obj = check_dict(json_)
        obj['url'] = obj.get('url')
        obj['forward_text'] = obj.get('forward_text')
        obj['bot_username'] = obj.get('bot_username')
        obj['request_write_access'] = obj.get('request_write_access')
        return cls(**obj)
    def __init__(
        self, url: str, forward_text: str|None=None,
        bot_username: str|None=None, request_write_access: bool|None=None, **kwargs
    ):
        self.url = url
        if forward_text is not None:
            self.forward_text = forward_text
        if bot_username is not None:
            self.bot_username = bot_username
        if request_write_access is not None:
            self.request_write_access = request_write_access

class LabeledPrice:
    @classmethod
    def dese(cls, json_):
        if json_ is None: return None
        obj = check_dict(json_)
        obj['label'] = obj.get('label')
        obj['amount'] = obj.get('amount')
        return cls(**obj)
    def __init__(self, label: str, amount: int, **kwargs):
        self.label = label
        self.amount = amount

class User:
    @classmethod
    def dese(cls, json_):
        if json_ is None: return None
        obj = check_dict(json_)
        obj['id'] = obj.get('id')
        obj['is_bot'] = obj.get('is_bot')
        obj['first_name'] = obj.get('first_name')
        obj['last_name'] = obj.get('last_name')
        obj['username'] = obj.get('username')
        obj['language_code'] = obj.get('language_code')
        obj['is_premium'] = obj.get('is_premium')
        obj['added_to_attachment_menu'] = obj.get('added_to_attachment_menu')
        obj['can_join_groups'] = obj.get('can_join_groups')
        obj['can_read_all_group_messages'] = obj.get('can_read_all_group_messages')
        obj['supports_inline_queries'] = obj.get('supports_inline_queries')
        return cls(**obj)
    def __init__(
        self, id: int, is_bot: bool, first_name: str, last_name: str|None=None,
        username: str|None=None, language_code: str|None=None, is_premium: Optional[True]=None,
        added_to_attachment_menu: Optional[True]=None, can_join_groups: bool|None=None,
        can_read_all_group_messages: bool|None=None, supports_inline_queries: bool|None=None, **kwargs
    ):
        self.id = id
        self.is_bot = is_bot
        self.first_name = first_name
        self.last_name = last_name # Optional
        self.username = username # Optional
        if language_code is not None:
            self.language_code = language_code
        if is_premium is not None:
            self.is_premium = is_premium
        if added_to_attachment_menu is not None:
            self.added_to_attachment_menu = added_to_attachment_menu
        if can_join_groups is not None:
            self.can_join_groups = can_join_groups
        if can_read_all_group_messages is not None:
            self.can_read_all_group_messages = can_read_all_group_messages
        if supports_inline_queries is not None:
            self.supports_inline_queries = supports_inline_queries

class MessageEntity:
    @classmethod
    def dese(cls, json_):
        if json_ is None: return None
        obj = check_dict(json_)
        obj['type'] = obj.get('type')
        obj['offset'] = obj.get('offset')
        obj['length'] = obj.get('length')
        obj['url'] = obj.get('url')
        obj['user'] = User.dese(obj.get('user'))
        obj['language'] = obj.get('language')
        obj['custom_emoji_id'] = obj.get('custom_emoji_id')
        return cls(**obj)
    def __init__(
        self, type: str, offset: int, length: int, url: str|None=None, user: Optional[User]=None,
        language: str|None=None, custom_emoji_id: str|None=None, **kwargs
    ):
        self.type = type
        self.offset = offset
        self.length = length
        if url is not None:
            self.url = url
        if user is not None:
            self.user = user
        if language is not None:
            self.language = language
        if custom_emoji_id is not None:
            self.custom_emoji_id = custom_emoji_id

class Message:
    @classmethod
    def dese(cls, json_):
        if json_ is None: return None
        obj = check_dict(json_)
        obj['message_id'] = obj.get('message_id')
        obj['message_thread_id'] = obj.get('message_thread_id')
        obj['from_user'] = User.dese(obj.get('from'))
        obj['sender_chat'] = Chat.dese(obj.get('sender_chat'))
        obj['date'] = obj.get('date')
        obj['chat'] = Chat.dese(obj.get('chat'))
        obj['forward_from'] = User.dese(obj.get('forward_from'))
        obj['forward_from_chat'] = Chat.dese(obj.get('forward_from_chat'))
        obj['forward_from_message_id'] = obj.get('forward_from_message_id')
        obj['forward_signature'] = obj.get('forward_signature')
        obj['forward_sender_name'] = obj.get('forward_sender_name')
        obj['forward_date'] = obj.get('forward_date')
        obj['is_topic_message'] = obj.get('is_topic_message')
        obj['is_automatic_forward'] = obj.get('is_automatic_forward')
        obj['reply_to_message'] = Message.dese(obj.get('reply_to_message'))
        obj['via_bot'] = User.dese(obj.get('via_bot'))
        obj['edit_date'] = obj.get('edit_date')
        obj['has_protected_content'] = obj.get('has_protected_content')
        obj['media_group_id'] = obj.get('media_group_id')
        obj['author_signature'] = obj.get('author_signature')
        obj['text'] = obj.get('text')
        obj['entities'] = [MessageEntity.dese(kwargs) for kwargs in obj.get('entities')] if 'entities' in obj else None
        obj['animation'] = Animation.dese(obj.get('animation'))
        obj['audio'] = Audio.dese(obj.get('audio'))
        obj['document'] = Document.dese(obj.get('document'))
        obj['photo'] = [PhotoSize.dese(kwargs) for kwargs in obj.get('photo')] if 'photo' in obj else None
        obj['sticker'] = Sticker.dese(obj.get('sticker'))
        obj['story'] = Story.dese(obj.get('story'))
        obj['video'] = Video.dese(obj.get('video'))
        obj['video_note'] = VideoNote.dese(obj.get('video_note'))
        obj['voice'] = Voice.dese(obj.get('voice'))
        obj['caption'] = obj.get('caption')
        obj['caption_entities'] = [MessageEntity.dese(kwargs) for kwargs in obj.get('caption_entities')] if 'caption_entities' in obj else None
        obj['has_media_spoiler'] = obj.get('has_media_spoiler')
        obj['contact'] = Contact.dese(obj.get('contact'))
        obj['dice'] = Dice.dese(obj.get('dice'))
        obj['game'] = Game.dese(obj.get('game'))
        obj['poll'] = Poll.dese(obj.get('poll'))
        obj['venue'] = Venue.dese(obj.get('venue'))
        obj['location'] = Location.dese(obj.get('location'))
        obj['new_chat_members'] = [User.dese(kwargs) for kwargs in obj.get('new_chat_members')] if 'new_chat_members' in obj else None
        obj['left_chat_member'] = User.dese(obj.get('left_chat_member'))
        obj['new_chat_title'] = obj.get('new_chat_title')
        obj['new_chat_photo'] = [PhotoSize.dese(kwargs) for kwargs in obj.get('new_chat_photo')] if 'new_chat_photo' in obj else None
        obj['delete_chat_photo'] = obj.get('delete_chat_photo')
        obj['group_chat_created'] = obj.get('group_chat_created')
        obj['supergroup_chat_created'] = obj.get('supergroup_chat_created')
        obj['channel_chat_created'] = obj.get('channel_chat_created')
        obj['message_auto_delete_timer_changed'] = MessageAutoDeleteTimerChanged.dese(obj.get('message_auto_delete_timer_changed'))
        obj['migrate_to_chat_id'] = obj.get('migrate_to_chat_id')
        obj['migrate_from_chat_id'] = obj.get('migrate_from_chat_id')
        obj['pinned_message'] = Message.dese(obj.get('pinned_message'))
        obj['invoice'] = Invoice.dese(obj.get('invoice'))
        obj['successful_payment'] = SuccessfulPayment.dese(obj.get('successful_payment'))
        obj['user_shared'] = UserShared.dese(obj.get('user_shared'))
        obj['chat_shared'] = ChatShared.dese(obj.get('chat_shared'))
        obj['connected_website'] = obj.get('connected_website')
        obj['write_access_allowed'] = WriteAccessAllowed.dese(obj.get('write_access_allowed'))
        obj['passport_data'] = PassportData.dese(obj.get('passport_data'))
        obj['proximity_alert_triggered'] = ProximityAlertTriggered.dese(obj.get('proximity_alert_triggered'))
        obj['forum_topic_created'] = ForumTopicCreated.dese(obj.get('forum_topic_created'))
        obj['forum_topic_edited'] = ForumTopicEdited.dese(obj.get('forum_topic_edited'))
        obj['forum_topic_closed'] = ForumTopicClosed.dese(obj.get('forum_topic_closed'))
        obj['forum_topic_reopened'] = ForumTopicReopened.dese(obj.get('forum_topic_reopened'))
        obj['general_forum_topic_hidden'] = GeneralForumTopicHidden.dese(obj.get('general_forum_topic_hidden'))
        obj['general_forum_topic_unhidden'] = GeneralForumTopicUnhidden.dese(obj.get('general_forum_topic_unhidden'))
        obj['video_chat_scheduled'] = VideoChatScheduled.dese(obj.get('video_chat_scheduled'))
        obj['video_chat_started'] = VideoChatStarted.dese(obj.get('video_chat_started'))
        obj['video_chat_ended'] = VideoChatEnded.dese(obj.get('video_chat_ended'))
        obj['video_chat_participants_invited'] = VideoChatParticipantsInvited.dese(obj.get('video_chat_participants_invited'))
        obj['web_app_data'] = WebAppData.dese(obj.get('web_app_data'))
        obj['reply_markup'] = InlineKeyboardMarkup.dese(obj.get('reply_markup'))
        return cls(**obj)
    def __init__(
            self, message_id: int, date: int, chat, message_thread_id=None, from_user=None,
        sender_chat=None, forward_from=None, forward_from_chat=None, forward_from_message_id=None, forward_signature=None,
        forward_sender_name=None, forward_date=None, is_topic_message=None, is_automatic_forward=None, reply_to_message=None,
        via_bot=None, edit_date=None, has_protected_content=None, media_group_id=None, author_signature=None,
        text=None, entities=None, animation=None, audio=None, document=None,
        photo=None, sticker=None, story=None, video=None, video_note=None,
        voice=None, caption=None, caption_entities=None, has_media_spoiler=None, contact=None,
        dice=None, game=None, poll=None, venue=None, location=None,
        new_chat_members=None, left_chat_member=None, new_chat_title=None, new_chat_photo=None, delete_chat_photo=None,
        group_chat_created=None, supergroup_chat_created=None, channel_chat_created=None, message_auto_delete_timer_changed=None, migrate_to_chat_id=None,
        migrate_from_chat_id=None, pinned_message=None, invoice=None, successful_payment=None, user_shared=None,
        chat_shared=None, connected_website=None, write_access_allowed=None, passport_data=None, proximity_alert_triggered=None,
        forum_topic_created=None, forum_topic_edited=None, forum_topic_closed=None, forum_topic_reopened=None, general_forum_topic_hidden=None,
        general_forum_topic_unhidden=None, video_chat_scheduled=None, video_chat_started=None, video_chat_ended=None, video_chat_participants_invited=None,
        web_app_data=None, reply_markup=None, **kwargs
    ):
        self.message_id: int = message_id
        self.date: int = date
        self.chat: Chat = chat
        self.text: str|None = text if text is not None else str() # Optional
        if message_thread_id is not None:
            self.message_thread_id: Optional[int] = message_thread_id
        if from_user is not None:
            self.from_user: Optional[User] = from_user
        if sender_chat is not None:
            self.sender_chat: Optional[Chat] = sender_chat
        if forward_from is not None:
            self.forward_from: Optional[User] = forward_from
        if forward_from_chat is not None:
            self.forward_from_chat: Optional[Chat] = forward_from_chat
        if forward_from_message_id is not None:
            self.forward_from_message_id: Optional[int] = forward_from_message_id
        if forward_signature is not None:
            self.forward_signature: Optional[str] = forward_signature
        if forward_sender_name is not None:
            self.forward_sender_name: Optional[str] = forward_sender_name
        if forward_date is not None:
            self.forward_date: Optional[int] = forward_date
        if is_topic_message is not None:
            self.is_topic_message: Optional[True] = is_topic_message
        if is_automatic_forward is not None:
            self.is_automatic_forward: Optional[True] = is_automatic_forward
        if reply_to_message is not None:
            self.reply_to_message: Optional[Message] = reply_to_message
        if via_bot is not None:
            self.via_bot: Optional[User] = via_bot
        if edit_date is not None:
            self.edit_date: Optional[int] = edit_date
        if has_protected_content is not None:
            self.has_protected_content: Optional[True] = has_protected_content
        if media_group_id is not None:
            self.media_group_id: Optional[str] = media_group_id
        if author_signature is not None:
            self.author_signature: Optional[str] = author_signature
        if entities is not None:
            self.entities: Optional[List[MessageEntity]] = entities
        if animation is not None:
            self.animation: Optional[Animation] = animation
        if audio is not None:
            self.audio: Optional[Audio] = audio
        if document is not None:
            self.document: Optional[Document] = document
        if photo is not None:
            self.photo: Optional[List[PhotoSize]] = photo
        if sticker is not None:
            self.sticker: Optional[Sticker] = sticker
        if story is not None:
            self.story: Optional[Story] = story
        if video is not None:
            self.video: Optional[Video] = video
        if video_note is not None:
            self.video_note: Optional[VideoNote] = video_note
        if voice is not None:
            self.voice: Optional[Voice] = voice
        if caption is not None:
            self.caption: Optional[str] = caption
        if caption_entities is not None:
            self.caption_entities: Optional[List[MessageEntity]] = caption_entities
        if has_media_spoiler is not None:
            self.has_media_spoiler: Optional[True] = has_media_spoiler
        if contact is not None:
            self.contact: Optional[Contact] = contact
        if dice is not None:
            self.dice: Optional[Dice] = dice
        if game is not None:
            self.game: Optional[Game] = game
        if poll is not None:
            self.poll: Optional[Poll] = poll
        if venue is not None:
            self.venue: Optional[Venue] = venue
        if location is not None:
            self.location: Optional[Location] = location
        if new_chat_members is not None:
            self.new_chat_members: Optional[List[User]] = new_chat_members
        if left_chat_member is not None:
            self.left_chat_member: Optional[User] = left_chat_member
        if new_chat_title is not None:
            self.new_chat_title: Optional[str] = new_chat_title
        if new_chat_photo is not None:
            self.new_chat_photo: Optional[List[PhotoSize]] = new_chat_photo
        if delete_chat_photo is not None:
            self.delete_chat_photo: Optional[True] = delete_chat_photo
        if group_chat_created is not None:
            self.group_chat_created: Optional[True] = group_chat_created
        if supergroup_chat_created is not None:
            self.supergroup_chat_created: Optional[True] = supergroup_chat_created
        if channel_chat_created is not None:
            self.channel_chat_created: Optional[True] = channel_chat_created
        if message_auto_delete_timer_changed is not None:
            self.message_auto_delete_timer_changed: Optional[MessageAutoDeleteTimerChanged] = message_auto_delete_timer_changed
        if migrate_to_chat_id is not None:
            self.migrate_to_chat_id: Optional[int] = migrate_to_chat_id
        if migrate_from_chat_id is not None:
            self.migrate_from_chat_id: Optional[int] = migrate_from_chat_id
        if pinned_message is not None:
            self.pinned_message: Optional[Message] = pinned_message
        if invoice is not None:
            self.invoice: Optional[Invoice] = invoice
        if successful_payment is not None:
            self.successful_payment: Optional[SuccessfulPayment] = successful_payment
        if user_shared is not None:
            self.user_shared: Optional[UserShared] = user_shared
        if chat_shared is not None:
            self.chat_shared: Optional[ChatShared] = chat_shared
        if connected_website is not None:
            self.connected_website: Optional[str] = connected_website
        if write_access_allowed is not None:
            self.write_access_allowed: Optional[WriteAccessAllowed] = write_access_allowed
        if passport_data is not None:
            self.passport_data: Optional[PassportData] = passport_data
        if proximity_alert_triggered is not None:
            self.proximity_alert_triggered: Optional[ProximityAlertTriggered] = proximity_alert_triggered
        if forum_topic_created is not None:
            self.forum_topic_created: Optional[ForumTopicCreated] = forum_topic_created
        if forum_topic_edited is not None:
            self.forum_topic_edited: Optional[ForumTopicEdited] = forum_topic_edited
        if forum_topic_closed is not None:
            self.forum_topic_closed: Optional[ForumTopicClosed] = forum_topic_closed
        if forum_topic_reopened is not None:
            self.forum_topic_reopened: Optional[ForumTopicReopened] = forum_topic_reopened
        if general_forum_topic_hidden is not None:
            self.general_forum_topic_hidden: Optional[GeneralForumTopicHidden] = general_forum_topic_hidden
        if general_forum_topic_unhidden is not None:
            self.general_forum_topic_unhidden: Optional[GeneralForumTopicUnhidden] = general_forum_topic_unhidden
        if video_chat_scheduled is not None:
            self.video_chat_scheduled: Optional[VideoChatScheduled] = video_chat_scheduled
        if video_chat_started is not None:
            self.video_chat_started: Optional[VideoChatStarted] = video_chat_started
        if video_chat_ended is not None:
            self.video_chat_ended: Optional[VideoChatEnded] = video_chat_ended
        if video_chat_participants_invited is not None:
            self.video_chat_participants_invited: Optional[VideoChatParticipantsInvited] = video_chat_participants_invited
        if web_app_data is not None:
            self.web_app_data: Optional[WebAppData] = web_app_data
        if reply_markup is not None:
            self.reply_markup: Optional[InlineKeyboardMarkup] = reply_markup

class ChatPhoto:
    @classmethod
    def dese(cls, json_):
        if json_ is None: return None
        obj = check_dict(json_)
        obj['small_file_id'] = obj.get('small_file_id')
        obj['small_file_unique_id'] = obj.get('small_file_unique_id')
        obj['big_file_id'] = obj.get('big_file_id')
        obj['big_file_unique_id'] = obj.get('big_file_unique_id')
        return cls(**obj)
    def __init__(
        self, small_file_id: str, small_file_unique_id: str,
        big_file_id: str, big_file_unique_id: str, **kwargs
    ):
        self.small_file_id = small_file_id
        self.small_file_unique_id = small_file_unique_id
        self.big_file_id = big_file_id
        self.big_file_unique_id = big_file_unique_id

class Location:
    @classmethod
    def dese(cls, json_):
        if json_ is None: return None
        obj = check_dict(json_)
        obj['longitude'] = obj.get('longitude')
        obj['latitude'] = obj.get('latitude')
        obj['horizontal_accuracy'] = obj.get('horizontal_accuracy')
        obj['live_period'] = obj.get('live_period')
        obj['heading'] = obj.get('heading')
        obj['proximity_alert_radius'] = obj.get('proximity_alert_radius')
        return cls(**obj)
    def __init__(
        self, longitude: float, latitude: float, horizontal_accuracy: float|None=None,
        live_period: int|None=None, heading: int|None=None, proximity_alert_radius: int|None=None, **kwargs
    ):
        self.longitude = longitude
        self.latitude = latitude
        if horizontal_accuracy is not None:
            self.horizontal_accuracy = horizontal_accuracy
        if live_period is not None:
            self.live_period = live_period
        if heading is not None:
            self.heading = heading
        if proximity_alert_radius is not None:
            self.proximity_alert_radius = proximity_alert_radius

class ChatLocation:
    @classmethod
    def dese(cls, json_):
        if json_ is None: return None
        obj = check_dict(json_)
        obj['location'] = Location.dese(obj.get('location'))
        obj['address'] = obj.get('address')
        return cls(**obj)
    def __init__(self, location: Location, address: str, **kwargs):
        self.location = location
        self.address = address

class Chat:
    @classmethod
    def dese(cls, json_):
        if json_ is None: return None
        obj = check_dict(json_)
        obj['id'] = obj.get('id')
        obj['type'] = obj.get('type')
        obj['title'] = obj.get('title')
        obj['username'] = obj.get('username')
        obj['first_name'] = obj.get('first_name')
        obj['last_name'] = obj.get('last_name')
        obj['is_forum'] = obj.get('is_forum')
        obj['photo'] = ChatPhoto.dese(obj.get('photo'))
        obj['active_usernames'] = obj.get('active_usernames')
        obj['emoji_status_custom_emoji_id'] = obj.get('emoji_status_custom_emoji_id')
        obj['emoji_status_expiration_date'] = obj.get('emoji_status_expiration_date')
        obj['bio'] = obj.get('bio')
        obj['has_private_forwards'] = obj.get('has_private_forwards')
        obj['has_restricted_voice_and_video_messages'] = obj.get('has_restricted_voice_and_video_messages')
        obj['join_to_send_messages'] = obj.get('join_to_send_messages')
        obj['join_by_request'] = obj.get('join_by_request')
        obj['description'] = obj.get('description')
        obj['invite_link'] = obj.get('invite_link')
        obj['pinned_message'] = Message.dese(obj.get('pinned_message'))
        obj['permissions'] = ChatPermissions.dese(obj.get('permissions'))
        obj['slow_mode_delay'] = obj.get('slow_mode_delay')
        obj['message_auto_delete_time'] = obj.get('message_auto_delete_time')
        obj['has_aggressive_anti_spam_enabled'] = obj.get('has_aggressive_anti_spam_enabled')
        obj['has_hidden_members'] = obj.get('has_hidden_members')
        obj['has_protected_content'] = obj.get('has_protected_content')
        obj['sticker_set_name'] = obj.get('sticker_set_name')
        obj['can_set_sticker_set'] = obj.get('can_set_sticker_set')
        obj['linked_chat_id'] = obj.get('linked_chat_id')
        obj['location'] = ChatLocation.dese(obj.get('location'))
        return cls(**obj)
    def __init__(
        self, id: int, type: str, title: str|None=None, username: str|None=None, first_name: str|None=None,
        last_name: str|None=None, is_forum: Optional[True]=None, photo: Optional[ChatPhoto]=None, active_usernames: List[str]|None=None,
        emoji_status_custom_emoji_id: str|None=None, emoji_status_expiration_date: int|None=None, bio: str|None=None,
        has_private_forwards: Optional[True]=None, has_restricted_voice_and_video_messages: Optional[True]=None,
        join_to_send_messages: Optional[True]=None, join_by_request: Optional[True]=None, description: str|None=None,
        invite_link: str|None=None, pinned_message: Optional[Message]=None, permissions: Optional[ChatPermissions]=None, slow_mode_delay: int|None=None,
        message_auto_delete_time: int|None=None, has_aggressive_anti_spam_enabled: Optional[True]=None,
        has_hidden_members: Optional[True]=None, has_protected_content: Optional[True]=None, sticker_set_name: str|None=None,
        can_set_sticker_set: Optional[True]=None, linked_chat_id: int|None=None, location: Optional[ChatLocation]=None, **kwargs
    ):
        self.id = id
        self.type = type
        if title is not None:
            self.title = title
        if username is not None:
            self.username = username
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if is_forum is not None:
            self.is_forum = is_forum
        if photo is not None:
            self.photo = photo
        if active_usernames is not None:
            self.active_usernames = active_usernames
        if emoji_status_custom_emoji_id is not None:
            self.emoji_status_custom_emoji_id = emoji_status_custom_emoji_id
        if emoji_status_expiration_date is not None:
            self.emoji_status_expiration_date = emoji_status_expiration_date
        if bio is not None:
            self.bio = bio
        if has_private_forwards is not None:
            self.has_private_forwards = has_private_forwards
        if has_restricted_voice_and_video_messages is not None:
            self.has_restricted_voice_and_video_messages = has_restricted_voice_and_video_messages
        if join_to_send_messages is not None:
            self.join_to_send_messages = join_to_send_messages
        if join_by_request is not None:
            self.join_by_request = join_by_request
        if description is not None:
            self.description = description
        if invite_link is not None:
            self.invite_link = invite_link
        if pinned_message is not None:
            self.pinned_message = pinned_message
        if permissions is not None:
            self.permissions = permissions
        if slow_mode_delay is not None:
            self.slow_mode_delay = slow_mode_delay
        if message_auto_delete_time is not None:
            self.message_auto_delete_time = message_auto_delete_time
        if has_aggressive_anti_spam_enabled is not None:
            self.has_aggressive_anti_spam_enabled = has_aggressive_anti_spam_enabled
        if has_hidden_members is not None:
            self.has_hidden_members = has_hidden_members
        if has_protected_content is not None:
            self.has_protected_content = has_protected_content
        if sticker_set_name is not None:
            self.sticker_set_name = sticker_set_name
        if can_set_sticker_set is not None:
            self.can_set_sticker_set = can_set_sticker_set
        if linked_chat_id is not None:
            self.linked_chat_id = linked_chat_id
        if location is not None:
            self.location = location

class MessageId:
    @classmethod
    def dese(cls, json_):
        if json_ is None: return None
        obj = check_dict(json_)
        obj['message_id'] = obj.get('message_id')
        return cls(**obj)
    def __init__(self, message_id: int, **kwargs):
        self.message_id = message_id

class PhotoSize:
    @classmethod
    def dese(cls, json_):
        if json_ is None: return None
        obj = check_dict(json_)
        obj['file_id'] = obj.get('file_id')
        obj['file_unique_id'] = obj.get('file_unique_id')
        obj['width'] = obj.get('width')
        obj['height'] = obj.get('height')
        obj['file_size'] = obj.get('file_size')
        return cls(**obj)
    def __init__(
        self, file_id: str, file_unique_id: str, width: int,
        height: int, file_size: int|None=None, **kwargs
    ):
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.width = width
        self.height = height
        if file_size is not None:
            self.file_size = file_size

class Animation:
    @classmethod
    def dese(cls, json_):
        if json_ is None: return None
        obj = check_dict(json_)
        obj['file_id'] = obj.get('file_id')
        obj['file_unique_id'] = obj.get('file_unique_id')
        obj['width'] = obj.get('width')
        obj['height'] = obj.get('height')
        obj['duration'] = obj.get('duration')
        obj['thumbnail'] = PhotoSize.dese(obj.get('thumbnail'))
        obj['file_name'] = obj.get('file_name')
        obj['mime_type'] = obj.get('mime_type')
        obj['file_size'] = obj.get('file_size')
        return cls(**obj)
    def __init__(
        self, file_id: str, file_unique_id: str, width: int, height: int,
        duration: int, thumbnail: Optional[PhotoSize]=None, file_name: str|None=None,
        mime_type: str|None=None, file_size: int|None=None, **kwargs
    ):
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.width = width
        self.height = height
        self.duration = duration
        if thumbnail is not None:
            self.thumbnail = thumbnail
        if file_name is not None:
            self.file_name = file_name
        if mime_type is not None:
            self.mime_type = mime_type
        if file_size is not None:
            self.file_size = file_size

class Audio:
    @classmethod
    def dese(cls, json_):
        if json_ is None: return None
        obj = check_dict(json_)
        obj['file_id'] = obj.get('file_id')
        obj['file_unique_id'] = obj.get('file_unique_id')
        obj['duration'] = obj.get('duration')
        obj['performer'] = obj.get('performer')
        obj['title'] = obj.get('title')
        obj['file_name'] = obj.get('file_name')
        obj['mime_type'] = obj.get('mime_type')
        obj['file_size'] = obj.get('file_size')
        obj['thumbnail'] = PhotoSize.dese(obj.get('thumbnail'))
        return cls(**obj)
    def __init__(
        self, file_id: str, file_unique_id: str, duration: int,
        performer: str|None=None, title: str|None=None, file_name: str|None=None,
        mime_type: str|None=None, file_size: int|None=None, thumbnail: Optional[PhotoSize]=None, **kwargs
    ):
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.duration = duration
        if performer is not None:
            self.performer = performer
        if title is not None:
            self.title = title
        if file_name is not None:
            self.file_name = file_name
        if mime_type is not None:
            self.mime_type = mime_type
        if file_size is not None:
            self.file_size = file_size
        if thumbnail is not None:
            self.thumbnail = thumbnail

class Document:
    @classmethod
    def dese(cls, json_):
        if json_ is None: return None
        obj = check_dict(json_)
        obj['file_id'] = obj.get('file_id')
        obj['file_unique_id'] = obj.get('file_unique_id')
        obj['thumbnail'] = PhotoSize.dese(obj.get('thumbnail'))
        obj['file_name'] = obj.get('file_name')
        obj['mime_type'] = obj.get('mime_type')
        obj['file_size'] = obj.get('file_size')
        return cls(**obj)
    def __init__(
        self, file_id: str, file_unique_id: str, thumbnail: Optional[PhotoSize]=None,
        file_name: str|None=None, mime_type: str|None=None, file_size: int|None=None, **kwargs
    ):
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        if thumbnail is not None:
            self.thumbnail = thumbnail
        if file_name is not None:
            self.file_name = file_name
        if mime_type is not None:
            self.mime_type = mime_type
        if file_size is not None:
            self.file_size = file_size

class Story:
    @classmethod
    def dese(cls, json_):
        if json_ is None: return None
        obj = check_dict(json_)
        return cls(**obj)
    def __init__(self, **kwargs):
        self.__dict__ = kwargs

class Video:
    @classmethod
    def dese(cls, json_):
        if json_ is None: return None
        obj = check_dict(json_)
        obj['file_id'] = obj.get('file_id')
        obj['file_unique_id'] = obj.get('file_unique_id')
        obj['width'] = obj.get('width')
        obj['height'] = obj.get('height')
        obj['duration'] = obj.get('duration')
        obj['thumbnail'] = PhotoSize.dese(obj.get('thumbnail'))
        obj['file_name'] = obj.get('file_name')
        obj['mime_type'] = obj.get('mime_type')
        obj['file_size'] = obj.get('file_size')
        return cls(**obj)
    def __init__(
        self, file_id: str, file_unique_id: str, width: int, height: int,
        duration: int, thumbnail: Optional[PhotoSize]=None, file_name: str|None=None,
        mime_type: str|None=None, file_size: int|None=None, **kwargs
    ):
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.width = width
        self.height = height
        self.duration = duration
        if thumbnail is not None:
            self.thumbnail = thumbnail
        if file_name is not None:
            self.file_name = file_name
        if mime_type is not None:
            self.mime_type = mime_type
        if file_size is not None:
            self.file_size = file_size

class VideoNote:
    @classmethod
    def dese(cls, json_):
        if json_ is None: return None
        obj = check_dict(json_)
        obj['file_id'] = obj.get('file_id')
        obj['file_unique_id'] = obj.get('file_unique_id')
        obj['length'] = obj.get('length')
        obj['duration'] = obj.get('duration')
        obj['thumbnail'] = PhotoSize.dese(obj.get('thumbnail'))
        obj['file_size'] = obj.get('file_size')
        return cls(**obj)
    def __init__(
        self, file_id: str, file_unique_id: str, length: int,
        duration: int, thumbnail: Optional[PhotoSize]=None, file_size: int|None=None, **kwargs
    ):
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.length = length
        self.duration = duration
        if thumbnail is not None:
            self.thumbnail = thumbnail
        if file_size is not None:
            self.file_size = file_size

class Voice:
    @classmethod
    def dese(cls, json_):
        if json_ is None: return None
        obj = check_dict(json_)
        obj['file_id'] = obj.get('file_id')
        obj['file_unique_id'] = obj.get('file_unique_id')
        obj['duration'] = obj.get('duration')
        obj['mime_type'] = obj.get('mime_type')
        obj['file_size'] = obj.get('file_size')
        return cls(**obj)
    def __init__(
        self, file_id: str, file_unique_id: str, duration: int,
        mime_type: str|None=None, file_size: int|None=None, **kwargs
    ):
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.duration = duration
        if mime_type is not None:
            self.mime_type = mime_type
        if file_size is not None:
            self.file_size = file_size

class Contact:
    @classmethod
    def dese(cls, json_):
        if json_ is None: return None
        obj = check_dict(json_)
        obj['phone_number'] = obj.get('phone_number')
        obj['first_name'] = obj.get('first_name')
        obj['last_name'] = obj.get('last_name')
        obj['user_id'] = obj.get('user_id')
        obj['vcard'] = obj.get('vcard')
        return cls(**obj)
    def __init__(
        self, phone_number: str, first_name: str, last_name: str|None=None,
        user_id: int|None=None, vcard: str|None=None, **kwargs
    ):
        self.phone_number = phone_number
        self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if user_id is not None:
            self.user_id = user_id
        if vcard is not None:
            self.vcard = vcard

class Dice:
    @classmethod
    def dese(cls, json_):
        if json_ is None: return None
        obj = check_dict(json_)
        obj['emoji'] = obj.get('emoji')
        obj['value'] = obj.get('value')
        return cls(**obj)
    def __init__(self, emoji: str, value: int, **kwargs):
        self.emoji = emoji
        self.value = value

class PollOption:
    @classmethod
    def dese(cls, json_):
        if json_ is None: return None
        obj = check_dict(json_)
        obj['text'] = obj.get('text')
        obj['voter_count'] = obj.get('voter_count')
        return cls(**obj)
    def __init__(self, text: str, voter_count: int, **kwargs):
        self.text = text
        self.voter_count = voter_count

class PollAnswer:
    @classmethod
    def dese(cls, json_):
        if json_ is None: return None
        obj = check_dict(json_)
        obj['poll_id'] = obj.get('poll_id')
        obj['voter_chat'] = Chat.dese(obj.get('voter_chat'))
        obj['user'] = User.dese(obj.get('user'))
        obj['option_ids'] = obj.get('option_ids')
        return cls(**obj)
    def __init__(
        self, poll_id: str, voter_chat: Optional[Chat]=None,
        user: Optional[User]=None, option_ids: Optional[List[int]]=None, **kwargs
    ):
        self.poll_id = poll_id
        if voter_chat is not None:
            self.voter_chat = voter_chat
        if user is not None:
            self.user = user
        if option_ids is not None:
            self.option_ids = option_ids

class Poll:
    @classmethod
    def dese(cls, json_):
        if json_ is None: return None
        obj = check_dict(json_)
        obj['id'] = obj.get('id')
        obj['question'] = obj.get('question')
        obj['options'] = [PollOption.dese(obj) for obj in obj.get('options')] if 'options' in obj else None
        obj['total_voter_count'] = obj.get('total_voter_count')
        obj['is_closed'] = obj.get('is_closed')
        obj['is_anonymous'] = obj.get('is_anonymous')
        obj['type'] = obj.get('type')
        obj['allows_multiple_answers'] = obj.get('allows_multiple_answers')
        obj['correct_option_id'] = obj.get('correct_option_id')
        obj['explanation'] = obj.get('explanation')
        obj['explanation_entities'] = [MessageEntity.dese(kwargs) for kwargs in obj.get('explanation_entities')] if 'explanation_entities' in obj else None
        obj['open_period'] = obj.get('open_period')
        obj['close_date'] = obj.get('close_date')
        return cls(**obj)
    def __init__(
        self, id: str, question: str, options, total_voter_count: int, is_closed: bool,
        is_anonymous: bool, type: str, allows_multiple_answers: bool, correct_option_id: int|None=None,
        explanation: str|None=None, explanation_entities=None, open_period: int|None=None,
        close_date: int|None=None, **kwargs
    ):
        self.id = id
        self.question = question
        self.options: List[PollOption] = options
        self.total_voter_count = total_voter_count
        self.is_closed = is_closed
        self.is_anonymous = is_anonymous
        self.type = type
        self.allows_multiple_answers = allows_multiple_answers
        if correct_option_id is not None:
            self.correct_option_id = correct_option_id
        if explanation is not None:
            self.explanation = explanation
        if explanation_entities is not None:
            self.explanation_entities: Optional[List[MessageEntity]] = explanation_entities
        if open_period is not None:
            self.open_period = open_period
        if close_date is not None:
            self.close_date = close_date

class Venue:
    @classmethod
    def dese(cls, json_):
        if json_ is None: return None
        obj = check_dict(json_)
        obj['location'] = Location.dese(obj.get('location'))
        obj['title'] = obj.get('title')
        obj['address'] = obj.get('address')
        obj['foursquare_id'] = obj.get('foursquare_id')
        obj['foursquare_type'] = obj.get('foursquare_type')
        obj['google_place_id'] = obj.get('google_place_id')
        obj['google_place_type'] = obj.get('google_place_type')
        return cls(**obj)
    def __init__(
        self, location, title: str, address: str, foursquare_id: str|None=None,
        foursquare_type: str|None=None, google_place_id: str|None=None,
        google_place_type: str|None=None, **kwargs
    ):
        self.location: Location = location
        self.title = title
        self.address = address
        if foursquare_id is not None:
            self.foursquare_id = foursquare_id
        if foursquare_type is not None:
            self.foursquare_type = foursquare_type
        if google_place_id is not None:
            self.google_place_id = google_place_id
        if google_place_type is not None:
            self.google_place_type = google_place_type

class WebAppData:
    @classmethod
    def dese(cls, json_):
        if json_ is None: return None
        obj = check_dict(json_)
        obj['data'] = obj.get('data')
        obj['button_text'] = obj.get('button_text')
        return cls(**obj)
    def __init__(self, data: str, button_text: str, **kwargs):
        self.data = data
        self.button_text = button_text

class ProximityAlertTriggered:
    @classmethod
    def dese(cls, json_):
        if json_ is None: return None
        obj = check_dict(json_)
        obj['traveler'] = User.dese(obj.get('traveler'))
        obj['watcher'] = User.dese(obj.get('watcher'))
        obj['distance'] = obj.get('distance')
        return cls(**obj)
    def __init__(self, traveler: User, watcher: User, distance: int, **kwargs):
        self.traveler = traveler
        self.watcher = watcher
        self.distance = distance

class MessageAutoDeleteTimerChanged:
    @classmethod
    def dese(cls, json_):
        if json_ is None: return None
        obj = check_dict(json_)
        obj['message_auto_delete_time'] = obj.get('message_auto_delete_time')
        return cls(**obj)
    def __init__(self, message_auto_delete_time: int, **kwargs):
        self.message_auto_delete_time = message_auto_delete_time

class ForumTopicCreated:
    @classmethod
    def dese(cls, json_):
        if json_ is None: return None
        obj = check_dict(json_)
        obj['name'] = obj.get('name')
        obj['icon_color'] = obj.get('icon_color')
        obj['icon_custom_emoji_id'] = obj.get('icon_custom_emoji_id')
        return cls(**obj)
    def __init__(self, name: str, icon_color: int, icon_custom_emoji_id: str|None=None, **kwargs):
        self.name = name
        self.icon_color = icon_color
        if icon_custom_emoji_id is not None:
            self.icon_custom_emoji_id = icon_custom_emoji_id

class ForumTopicClosed:
    @classmethod
    def dese(cls, json_):
        if json_ is None: return None
        obj = check_dict(json_)
        return cls(**obj)
    def __init__(self, **kwargs):
        self.__dict__ = kwargs

class ForumTopicEdited:
    @classmethod
    def dese(cls, json_):
        if json_ is None: return None
        obj = check_dict(json_)
        obj['name'] = obj.get('name')
        obj['icon_custom_emoji_id'] = obj.get('icon_custom_emoji_id')
        return cls(**obj)
    def __init__(self, name: str|None=None, icon_custom_emoji_id: str|None=None, **kwargs):
        if name is not None:
            self.name = name
        if icon_custom_emoji_id is not None:
            self.icon_custom_emoji_id = icon_custom_emoji_id

class ForumTopicReopened:
    @classmethod
    def dese(cls, json_):
        if json_ is None: return None
        obj = check_dict(json_)
        return cls(**obj)
    def __init__(self, **kwargs):
        self.__dict__ = kwargs

class GeneralForumTopicHidden:
    @classmethod
    def dese(cls, json_):
        if json_ is None: return None
        obj = check_dict(json_)
        return cls(**obj)
    def __init__(self, **kwargs):
        self.__dict__ = kwargs

class GeneralForumTopicUnhidden:
    @classmethod
    def dese(cls, json_):
        if json_ is None: return None
        obj = check_dict(json_)
        return cls(**obj)
    def __init__(self, **kwargs):
        self.__dict__ = kwargs

class UserShared:
    @classmethod
    def dese(cls, json_):
        if json_ is None: return None
        obj = check_dict(json_)
        obj['request_id'] = obj.get('request_id')
        obj['user_id'] = obj.get('user_id')
        return cls(**obj)
    def __init__(self, request_id: int, user_id: int, **kwargs):
        self.request_id = request_id
        self.user_id = user_id

class ChatShared:
    @classmethod
    def dese(cls, json_):
        if json_ is None: return None
        obj = check_dict(json_)
        obj['request_id'] = obj.get('request_id')
        obj['chat_id'] = obj.get('chat_id')
        return cls(**obj)
    def __init__(self, request_id: int, chat_id: int, **kwargs):
        self.request_id = request_id
        self.chat_id = chat_id

class WriteAccessAllowed:
    @classmethod
    def dese(cls, json_):
        if json_ is None: return None
        obj = check_dict(json_)
        obj['from_request'] = obj.get('from_request')
        obj['web_app_name'] = obj.get('web_app_name')
        obj['from_attachment_menu'] = obj.get('from_attachment_menu')
        return cls(**obj)
    def __init__(
        self, from_request: bool|None=None, web_app_name: str|None=None,
        from_attachment_menu: bool|None=None, **kwargs):
        if from_request is not None:
            self.from_request = from_request
        if web_app_name is not None:
            self.web_app_name = web_app_name
        if from_attachment_menu is not None:
            self.from_attachment_menu = from_attachment_menu

class VideoChatScheduled:
    @classmethod
    def dese(cls, json_):
        if json_ is None: return None
        obj = check_dict(json_)
        obj['start_date'] = obj.get('start_date')
        return cls(**obj)
    def __init__(self, start_date: int, **kwargs):
        self.start_date = start_date

class VideoChatStarted:
    @classmethod
    def dese(cls, json_):
        if json_ is None: return None
        obj = check_dict(json_)
        return cls(**obj)
    def __init__(self, **kwargs):
        self.__dict__ = kwargs

class VideoChatEnded:
    @classmethod
    def dese(cls, json_):
        if json_ is None: return None
        obj = check_dict(json_)
        obj['duration'] = obj.get('duration')
        return cls(**obj)
    def __init__(self, duration: int, **kwargs):
        self.duration = duration

class VideoChatParticipantsInvited:
    @classmethod
    def dese(cls, json_):
        if json_ is None: return None
        obj = check_dict(json_)
        obj['users'] = [User.dese(obj) for obj in obj.get('users')] if 'users' in obj else None
        return cls(**obj)
    def __init__(self, users: List[User], **kwargs):
        self.users = users

class UserProfilePhotos:
    @classmethod
    def dese(cls, json_):
        if json_ is None: return None
        obj = check_dict(json_)
        obj['total_count'] = obj.get('total_count')
        obj['photos'] = [[PhotoSize.dese(obj) for obj in lst] for lst in obj.get('photos')] if 'photos' in obj else None
        return cls(**obj)
    def __init__(self, total_count: int, photos: List[List[PhotoSize]], **kwargs):
        self.total_count = total_count
        self.photos = photos

class File:
    @classmethod
    def dese(cls, json_):
        if json_ is None: return None
        obj = check_dict(json_)
        obj['file_id'] = obj.get('file_id')
        obj['file_unique_id'] = obj.get('file_unique_id')
        obj['file_size'] = obj.get('file_size')
        obj['file_path'] = obj.get('file_path')
        return cls(**obj)
    def __init__(
        self, file_id: str, file_unique_id: str,
        file_size: int|None=None, file_path: str|None=None, **kwargs
    ):
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        if file_size is not None:
            self.file_size = file_size
        if file_path is not None:
            self.file_path = file_path

class WebAppInfo:
    @classmethod
    def dese(cls, json_):
        if json_ is None: return None
        obj = check_dict(json_)
        obj['url'] = obj.get('url')
        return cls(**obj)
    def __init__(self, url: str, **kwargs):
        self.url = url

class KeyboardButtonRequestUser:
    @classmethod
    def dese(cls, json_):
        if json_ is None: return None
        obj = check_dict(json_)
        obj['request_id'] = obj.get('request_id')
        obj['user_is_bot'] = obj.get('user_is_bot')
        obj['user_is_premium'] = obj.get('user_is_premium')
        return cls(**obj)
    def __init__(
        self, request_id: int, user_is_bot: bool|None=None, user_is_premium: bool|None=None, **kwargs):
        self.request_id = request_id
        if user_is_bot is not None:
            self.user_is_bot = user_is_bot
        if user_is_premium is not None:
            self.user_is_premium = user_is_premium

class KeyboardButtonRequestChat:
    @classmethod
    def dese(cls, json_):
        if json_ is None: return None
        obj = check_dict(json_)
        obj['request_id'] = obj.get('request_id')
        obj['chat_is_channel'] = obj.get('chat_is_channel')
        obj['chat_is_forum'] = obj.get('chat_is_forum')
        obj['chat_has_username'] = obj.get('chat_has_username')
        obj['chat_is_created'] = obj.get('chat_is_created')
        obj['user_administrator_rights'] = ChatAdministratorRights.dese(obj.get('user_administrator_rights'))
        obj['bot_administrator_rights'] = ChatAdministratorRights.dese(obj.get('bot_administrator_rights'))
        obj['bot_is_member'] = obj.get('bot_is_member')
        return cls(**obj)
    def __init__(
        self, request_id: int, chat_is_channel: bool, chat_is_forum: bool|None=None,
        chat_has_username: bool|None=None, chat_is_created: bool|None=None,
        user_administrator_rights: Optional[ChatAdministratorRights]=None,
        bot_administrator_rights: Optional[ChatAdministratorRights]=None,
        bot_is_member: bool|None=None, **kwargs
    ):
        self.request_id = request_id
        self.chat_is_channel = chat_is_channel
        if chat_is_forum is not None:
            self.chat_is_forum = chat_is_forum
        if chat_has_username is not None:
            self.chat_has_username = chat_has_username
        if chat_is_created is not None:
            self.chat_is_created = chat_is_created
        if user_administrator_rights is not None:
            self.user_administrator_rights = user_administrator_rights
        if bot_administrator_rights is not None:
            self.bot_administrator_rights = bot_administrator_rights
        if bot_is_member is not None:
            self.bot_is_member = bot_is_member

class KeyboardButtonPollType:
    @classmethod
    def dese(cls, json_):
        if json_ is None: return None
        obj = check_dict(json_)
        obj['type'] = obj.get('type')
        return cls(**obj)
    def __init__(self, type: str|None=None, **kwargs):
        if type is not None:
            self.type = type

class KeyboardButton:
    @classmethod
    def dese(cls, json_):
        if json_ is None: return None
        obj = check_dict(json_)
        obj['text'] = obj.get('text')
        obj['request_user'] = KeyboardButtonRequestUser.dese(obj.get('request_user'))
        obj['request_chat'] = KeyboardButtonRequestChat.dese(obj.get('request_chat'))
        obj['request_contact'] = obj.get('request_contact')
        obj['request_location'] = obj.get('request_location')
        obj['request_poll'] = KeyboardButtonPollType.dese(obj.get('request_poll'))
        obj['web_app'] = WebAppInfo.dese(obj.get('web_app'))
        return cls(**obj)
    def __init__(
        self, text: str, request_user: Optional[KeyboardButtonRequestUser]=None,
        request_chat: Optional[KeyboardButtonRequestChat]=None, request_contact: bool|None=None,
        request_location: bool|None=None, request_poll: Optional[KeyboardButtonPollType]=None, web_app: Optional[WebAppInfo]=None, **kwargs
    ):
        self.text = text
        if request_user is not None:
            self.request_user = request_user
        if request_chat is not None:
            self.request_chat = request_chat
        if request_contact is not None:
            self.request_contact = request_contact
        if request_location is not None:
            self.request_location = request_location
        if request_poll is not None:
            self.request_poll = request_poll
        if web_app is not None:
            self.web_app = web_app

class ReplyKeyboardMarkup:
    @classmethod
    def dese(cls, json_):
        if json_ is None: return None
        obj = check_dict(json_)
        obj['keyboard'] = [[KeyboardButton.dese(obj) for obj in lst] for lst in obj.get('keyboard')] if 'keyboard' in obj else None
        obj['is_persistent'] = obj.get('is_persistent')
        obj['resize_keyboard'] = obj.get('resize_keyboard')
        obj['one_time_keyboard'] = obj.get('one_time_keyboard')
        obj['input_field_placeholder'] = obj.get('input_field_placeholder')
        obj['selective'] = obj.get('selective')
        return cls(**obj)
    def __init__(
        self, keyboard: List[List[KeyboardButton]], is_persistent: bool|None=None, resize_keyboard: bool|None=None,
        one_time_keyboard: bool|None=None, input_field_placeholder: str|None=None, selective: bool|None=None, **kwargs
    ):
        self.keyboard = keyboard
        if is_persistent is not None:
            self.is_persistent = is_persistent
        if resize_keyboard is not None:
            self.resize_keyboard = resize_keyboard
        if one_time_keyboard is not None:
            self.one_time_keyboard = one_time_keyboard
        if input_field_placeholder is not None:
            self.input_field_placeholder = input_field_placeholder
        if selective is not None:
            self.selective = selective

class ReplyKeyboardRemove:
    @classmethod
    def dese(cls, json_):
        if json_ is None: return None
        obj = check_dict(json_)
        obj['remove_keyboard'] = obj.get('remove_keyboard')
        obj['selective'] = obj.get('selective')
        return cls(**obj)
    def __init__(self, remove_keyboard: True=True, selective: bool|None=None, **kwargs):
        self.remove_keyboard: True = remove_keyboard
        if selective is not None:
            self.selective = selective

class InlineKeyboardButton:
    @classmethod
    def dese(cls, json_):
        if json_ is None: return None
        obj = check_dict(json_)
        obj['text'] = obj.get('text')
        obj['url'] = obj.get('url')
        obj['callback_data'] = obj.get('callback_data')
        obj['web_app'] = WebAppInfo.dese(obj.get('web_app'))
        obj['login_url'] = LoginUrl.dese(obj.get('login_url'))
        obj['switch_inline_query'] = obj.get('switch_inline_query')
        obj['switch_inline_query_current_chat'] = obj.get('switch_inline_query_current_chat')
        obj['switch_inline_query_chosen_chat'] = SwitchInlineQueryChosenChat.dese(obj.get('switch_inline_query_chosen_chat'))
        obj['callback_game'] = CallbackGame.dese(obj.get('callback_game'))
        obj['pay'] = obj.get('pay')
        return cls(**obj)
    def __init__(
        self, text: str, url: str|None=None, callback_data: str|None=None, web_app: Optional[WebAppInfo]=None, 
        login_url: Optional[LoginUrl]=None, switch_inline_query: str|None=None, switch_inline_query_current_chat: str|None=None,
        switch_inline_query_chosen_chat: Optional[SwitchInlineQueryChosenChat]=None, callback_game: Optional[CallbackGame]=None, pay: bool|None=None, **kwargs
    ):
        self.text = text
        if url is not None:
            self.url = url
        if callback_data is not None:
            self.callback_data = callback_data
        if web_app is not None:
            self.web_app = web_app
        if login_url is not None:
            self.login_url = login_url
        if switch_inline_query is not None:
            self.switch_inline_query = switch_inline_query
        if switch_inline_query_current_chat is not None:
            self.switch_inline_query_current_chat = switch_inline_query_current_chat
        if switch_inline_query_chosen_chat is not None:
            self.switch_inline_query_chosen_chat = switch_inline_query_chosen_chat
        if callback_game is not None:
            self.callback_game = callback_game
        if pay is not None:
            self.pay = pay

class InlineKeyboardMarkup:
    @classmethod
    def dese(cls, json_):
        if json_ is None: return None
        obj = check_dict(json_)
        obj['inline_keyboard'] = [[InlineKeyboardButton.dese(obj) for obj in lst] for lst in obj.get('inline_keyboard')] if 'inline_keyboard' in obj else None
        return cls(**obj)
    def __init__(self, inline_keyboard: List[List[InlineKeyboardButton]], **kwargs):
        self.inline_keyboard = inline_keyboard

class CallbackQuery:
    @classmethod
    def dese(cls, json_):
        if json_ is None: return None
        obj = check_dict(json_)
        obj['id'] = obj.get('id')
        obj['from_user'] = User.dese(obj.get('from'))
        obj['message'] = Message.dese(obj.get('message'))
        obj['inline_message_id'] = obj.get('inline_message_id')
        obj['chat_instance'] = obj.get('chat_instance')
        obj['data'] = obj.get('data')
        obj['game_short_name'] = obj.get('game_short_name')
        return cls(**obj)
    def __init__(
        self, id: str, from_user: User, chat_instance: str, message: Optional[Message]=None,
        inline_message_id: str=None, data: str|None=None, game_short_name: str|None=None, **kwargs
    ):
        self.id = id
        self.from_user = from_user
        self.chat_instance = chat_instance
        if message is not None:
            self.message = message
        if inline_message_id is not None:
            self.inline_message_id = inline_message_id
        if data is not None:
            self.data = data
        if game_short_name is not None:
            self.game_short_name = game_short_name

class ForceReply:
    @classmethod
    def dese(cls, json_):
        if json_ is None: return None
        obj = check_dict(json_)
        obj['force_reply'] = obj.get('force_reply')
        obj['input_field_placeholder'] = obj.get('input_field_placeholder')
        obj['selective'] = obj.get('selective')
        return cls(**obj)
    def __init__(
        self, force_reply: True=True, input_field_placeholder: str|None=None,
        selective: bool|None=None, **kwargs
    ):
        self.force_reply = force_reply
        if input_field_placeholder is not None:
            self.input_field_placeholder = input_field_placeholder
        if selective is not None:
            self.selective = selective

class ChatInviteLink:
    @classmethod
    def dese(cls, json_):
        if json_ is None: return None
        obj = check_dict(json_)
        obj['invite_link'] = obj.get('invite_link')
        obj['creator'] = User.dese(obj.get('creator'))
        obj['creates_join_request'] = obj.get('creates_join_request')
        obj['is_primary'] = obj.get('is_primary')
        obj['is_revoked'] = obj.get('is_revoked')
        obj['name'] = obj.get('name')
        obj['expire_date'] = obj.get('expire_date')
        obj['member_limit'] = obj.get('member_limit')
        obj['pending_join_request_count'] = obj.get('pending_join_request_count')
        return cls(**obj)
    def __init__(
        self, invite_link: str, creator: User, creates_join_request: bool,
        is_primary: bool, is_revoked: bool, name: str|None=None, expire_date: int|None=None,
        member_limit: int|None=None, pending_join_request_count: int|None=None, **kwargs
    ):
        self.invite_link = invite_link
        self.creator = creator
        self.creates_join_request = creates_join_request
        self.is_primary = is_primary
        self.is_revoked = is_revoked
        if name is not None:
            self.name = name
        if expire_date is not None:
            self.expire_date = expire_date
        if member_limit is not None:
            self.member_limit = member_limit
        if pending_join_request_count is not None:
            self.pending_join_request_count = pending_join_request_count

# ChatMember: 6 subclasses

class ChatMember:
    @classmethod
    def dese(cls, json_):
        if json_ is None: return None
        obj = check_dict(json_)        
        obj['user'] = User.dese(obj.get('user'))
        status = obj['status']
        if status == 'creator':
            return ChatMemberOwner(**obj)
        elif status == 'administrator':
            return ChatMemberAdministrator(**obj)
        elif status == 'member':
            return ChatMemberMember(**obj)
        elif status == 'restricted':
            return ChatMemberRestricted(**obj)
        elif status == 'left':
            return ChatMemberLeft(**obj)
        elif status == 'kicked':
            return ChatMemberBanned(**obj)
        else:
            return cls(**obj)
    def __init__(
        self, user: User, status: str, can_send_messages: bool|None=None, can_promote_members: bool|None=None,
        can_delete_messages: bool|None=None, can_edit_stories: bool|None=None, can_invite_users: bool|None=None,
        can_restrict_members: bool|None=None, can_send_documents: bool|None=None, can_send_polls: bool|None=None,
        can_pin_messages: bool|None=None, can_send_other_messages: bool|None=None, until_date: int|None=None,
        can_send_voice_notes: bool|None=None, can_post_stories: bool|None=None, can_manage_video_chats: bool|None=None,
        can_be_edited: bool|None=None, can_send_video_notes: bool|None=None, custom_title: str|None=None,
        can_change_info: bool|None=None, can_manage_chat: bool|None=None, can_edit_messages: bool|None=None,
        can_send_photos: bool|None=None, can_delete_stories: bool|None=None, is_member: bool|None=None,
        is_anonymous: bool|None=None, can_manage_voice_chats: bool|None=None, can_post_messages: bool|None=None,
        can_send_videos: bool|None=None, can_send_audios: bool|None=None, can_manage_topics: bool|None=None,
        can_add_web_page_previews: bool|None=None, **kwargs
    ):
        self.user = user
        self.status = status
        if can_send_messages is not None:
            self.can_send_messages = can_send_messages
        if can_promote_members is not None:
            self.can_promote_members = can_promote_members
        if can_delete_messages is not None:
            self.can_delete_messages = can_delete_messages
        if can_edit_stories is not None:
            self.can_edit_stories = can_edit_stories
        if can_invite_users is not None:
            self.can_invite_users = can_invite_users
        if can_restrict_members is not None:
            self.can_restrict_members = can_restrict_members
        if can_send_documents is not None:
            self.can_send_documents = can_send_documents
        if can_send_polls is not None:
            self.can_send_polls = can_send_polls
        if can_pin_messages is not None:
            self.can_pin_messages = can_pin_messages
        if can_send_other_messages is not None:
            self.can_send_other_messages = can_send_other_messages
        if until_date is not None:
            self.until_date = until_date
        if can_send_voice_notes is not None:
            self.can_send_voice_notes = can_send_voice_notes
        if can_post_stories is not None:
            self.can_post_stories = can_post_stories
        if can_manage_video_chats is not None:
            self.can_manage_video_chats = can_manage_video_chats
        if can_be_edited is not None:
            self.can_be_edited = can_be_edited
        if can_send_video_notes is not None:
            self.can_send_video_notes = can_send_video_notes
        if custom_title is not None:
            self.custom_title = custom_title
        if can_change_info is not None:
            self.can_change_info = can_change_info
        if can_manage_chat is not None:
            self.can_manage_chat = can_manage_chat
        if can_edit_messages is not None:
            self.can_edit_messages = can_edit_messages
        if can_send_photos is not None:
            self.can_send_photos = can_send_photos
        if can_delete_stories is not None:
            self.can_delete_stories = can_delete_stories
        if is_member is not None:
            self.is_member = is_member
        if is_anonymous is not None:
            self.is_anonymous = is_anonymous
        if can_manage_voice_chats is not None:
            self.can_manage_voice_chats = can_manage_voice_chats
        if can_post_messages is not None:
            self.can_post_messages = can_post_messages
        if can_send_videos is not None:
            self.can_send_videos = can_send_videos
        if can_send_audios is not None:
            self.can_send_audios = can_send_audios
        if can_manage_topics is not None:
            self.can_manage_topics = can_manage_topics
        if can_add_web_page_previews is not None:
            self.can_add_web_page_previews = can_add_web_page_previews

class ChatMemberOwner(ChatMember):
    pass
class ChatMemberAdministrator(ChatMember):
    pass
class ChatMemberMember(ChatMember):
    pass
class ChatMemberRestricted(ChatMember):
    pass
class ChatMemberLeft(ChatMember):
    pass
class ChatMemberBanned(ChatMember):
    pass

class ChatMemberUpdated:
    @classmethod
    def dese(cls, json_):
        if json_ is None: return None
        obj = check_dict(json_)
        obj['chat'] = Chat.dese(obj.get('chat'))
        obj['from_user'] = User.dese(obj.get('from'))
        obj['date'] = obj.get('date')
        obj['old_chat_member'] = ChatMember.dese(obj.get('old_chat_member'))
        obj['new_chat_member'] = ChatMember.dese(obj.get('new_chat_member'))
        obj['invite_link'] = ChatInviteLink.dese(obj.get('invite_link'))
        obj['via_chat_folder_invite_link'] = obj.get('via_chat_folder_invite_link')
        return cls(**obj)
    def __init__(
        self, chat: Chat, from_user: User, date: int, old_chat_member: ChatMember,
        new_chat_member: ChatMember, invite_link: Optional[ChatInviteLink]=None,
        via_chat_folder_invite_link: bool|None=None, **kwargs
    ):
        self.chat = chat
        self.from_user = from_user
        self.date = date
        self.old_chat_member = old_chat_member
        self.new_chat_member = new_chat_member
        if invite_link is not None:
            self.invite_link = invite_link
        if via_chat_folder_invite_link is not None:
            self.via_chat_folder_invite_link = via_chat_folder_invite_link

class ChatJoinRequest:
    @classmethod
    def dese(cls, json_):
        if json_ is None: return None
        obj = check_dict(json_)
        obj['chat'] = Chat.dese(obj.get('chat'))
        obj['from_user'] = User.dese(obj.get('from'))
        obj['user_chat_id'] = obj.get('user_chat_id')
        obj['date'] = obj.get('date')
        obj['bio'] = obj.get('bio')
        obj['invite_link'] = ChatInviteLink.dese(obj.get('invite_link'))
        return cls(**obj)
    def __init__(
        self, chat: Chat, from_user: User, user_chat_id: int, date: int, bio: str|None=None,
        invite_link: Optional[ChatInviteLink]=None, **kwargs
    ):
        self.chat = chat
        self.from_user = from_user
        self.user_chat_id = user_chat_id
        self.date = date
        if bio is not None:
            self.bio = bio
        if invite_link is not None:
            self.invite_link = invite_link

class ForumTopic:
    @classmethod
    def dese(cls, json_):
        if json_ is None: return None
        obj = check_dict(json_)
        obj['message_thread_id'] = obj.get('message_thread_id')
        obj['name'] = obj.get('name')
        obj['icon_color'] = obj.get('icon_color')
        obj['icon_custom_emoji_id'] = obj.get('icon_custom_emoji_id')
        return cls(**obj)
    def __init__(
        self, message_thread_id: int, name: str, icon_color: int,
        icon_custom_emoji_id: str|None=None, **kwargs
    ):
        self.message_thread_id = message_thread_id
        self.name = name
        self.icon_color = icon_color
        if icon_custom_emoji_id is not None:
            self.icon_custom_emoji_id = icon_custom_emoji_id

class BotCommand:
    @classmethod
    def dese(cls, json_):
        if json_ is None: return None
        obj = check_dict(json_)
        obj['command'] = obj.get('command')
        obj['description'] = obj.get('description')
        return cls(**obj)
    def __init__(self, command: str, description: str, **kwarg):
        self.command = command
        self.description = description

# BotCommandScope: 7 subclasses

class BotCommandScopeDefault:
    def __init__(self, type: str="default"):
        self.type = type

class BotCommandScopeAllPrivateChats:
    def __init__(self, type: str="all_private_chats"):
        self.type = type

class BotCommandScopeAllGroupChats:
    def __init__(self, type: str="all_group_chats"):
        self.type = type

class BotCommandScopeAllChatAdministrators:
    def __init__(self, type: str="all_chat_administrators"):
        self.type = type

class BotCommandScopeChat:
    def __init__(self, chat_id: int|str, type: str="chat"):
        self.type = type
        self.chat_id = chat_id

class BotCommandScopeChatAdministrators:
    def __init__(self, chat_id: int|str, type: str="chat_administrators"):
        self.type = type
        self.chat_id = chat_id

class BotCommandScopeChatMember:
    def __init__(self, chat_id: int|str, user_id: int, type: str="chat_member"):
        self.type = type
        self.chat_id = chat_id
        self.user_id = user_id

class BotCommandScope:
    @classmethod
    def dese(cls, json_):
        if json_ is None: return None
        obj = check_dict(json_)
        type = obj['type']
        if type == 'default':
            return BotCommandScopeDefault(**obj)
        elif type == 'all_private_chats':
            return BotCommandScopeAllPrivateChats(**obj)
        elif type == 'all_group_chats':
            return BotCommandScopeAllGroupChats(**obj)
        elif type == 'all_chat_administrators':
            return BotCommandScopeAllChatAdministrators(**obj)
        elif type == 'chat':
            return BotCommandScopeChat(**obj)
        elif type == 'chat_administrators':
            return BotCommandScopeChatAdministrators(**obj)
        elif type == 'chat_member':
            return BotCommandScopeChatMember(**obj)
        else:
            return cls(**obj)
    def __init__(self, scope: Union[
        BotCommandScopeDefault, BotCommandScopeAllPrivateChats,
        BotCommandScopeAllGroupChats, BotCommandScopeAllChatAdministrators,
        BotCommandScopeChat, BotCommandScopeChatAdministrators, BotCommandScopeChatMember
    ]):
        available_scopes = (
            BotCommandScopeDefault, BotCommandScopeAllPrivateChats,
            BotCommandScopeAllGroupChats, BotCommandScopeAllChatAdministrators,
            BotCommandScopeChat, BotCommandScopeChatAdministrators, BotCommandScopeChatMember
        )
        if not isinstance(scope, available_scopes):
            raise TypeError(f"scope parameter should be an instance of\n{[x.__name__ for x in available_scopes]}")
        self.__dict__ = scope.__dict__

class BotName:
    @classmethod
    def dese(cls, json_):
        if json_ is None: return None
        obj = check_dict(json_)
        return cls(**obj)
    def __init__(self, name: str, *kwargs):
        self.name = name

class BotDescription:
    @classmethod
    def dese(cls, json_):
        if json_ is None: return None
        obj = check_dict(json_)
        obj['description'] = obj.get('description')
        return cls(**obj)
    def __init__(self, description: str, **kwargs):
        self.description = description

class BotShortDescription:
    @classmethod
    def dese(cls, json_):
        if json_ is None: return None
        obj = check_dict(json_)
        obj['short_description'] = obj.get('short_description')
        return cls(**obj)
    def __init__(self, short_description: str, **kwargs):
        self.short_description = short_description

# MenuButton: 3 subclasses

class MenuButtonCommands:
    def __init__(self, type: str='commands'):
        self.type = type

class MenuButtonWebApp:
    def __init__(self, text: str, web_app: WebAppInfo, type: str='web_app'):
        self.type = type
        self.text = text
        self.web_app = web_app

class MenuButtonDefault:
    def __init__(self, type: str='default'):
        self.type = type

class MenuButton:
    @classmethod
    def dese(cls, json_):
        if json_ is None: return None
        obj = check_dict(json_)
        type = obj['type']
        if type == 'commands':
            return MenuButtonCommands(**obj)
        elif type == 'web_app':
            obj['web_app'] = WebAppInfo.dese(obj.get('web_app'))
            return MenuButtonWebApp(**obj)
        elif type == 'default':
            return MenuButtonDefault(**obj)
        else:
            return cls(**obj)
    def __init__(self, menu: Union[MenuButtonCommands, MenuButtonWebApp, MenuButtonDefault]):
        available_menu = (MenuButtonCommands, MenuButtonWebApp, MenuButtonDefault)
        if not isinstance(menu, available_menu):
            raise TypeError(f"menu parameter should be an instance of\n{[x.__name__ for x in available_menu]}")
        self.__dict__ = menu.__dict__

class ResponseParameters:
    @classmethod
    def dese(cls, json_):
        if json_ is None: return None
        obj = check_dict(json_)
        obj['migrate_to_chat_id'] = obj.get('migrate_to_chat_id')
        obj['retry_after'] = obj.get('retry_after')
        return cls(**obj)
    def __init__(self, migrate_to_chat_id: int|None=None, retry_after: int|None=None, **kwargs):
        if migrate_to_chat_id is not None:
            self.migrate_to_chat_id = migrate_to_chat_id
        if retry_after is not None:
            self.retry_after = retry_after

class InputMediaPhoto:
    def __init__(
        self, media: str, type: str='photo', caption: str|None=None,
        parse_mode: str|None=None, caption_entities: Optional[List[MessageEntity]]=None,
        has_spoiler: bool|None=None
    ):
        self.type = type
        self.media = media
        if caption is not None:
            self.caption = caption
        if parse_mode is not None:
            self.parse_mode = parse_mode
        if caption_entities is not None:
            self.caption_entities = caption_entities
        if has_spoiler is not None:
            self.has_spoiler = has_spoiler

class InputMediaVideo:
    def __init__(
        self, media: str, type: str='video', thumbnail: Optional[Union[InputFile, str]]=None,
        caption: str|None=None, parse_mode: str|None=None, caption_entities: Optional[List[MessageEntity]]=None,
        width: int|None=None, height: int|None=None, duration: int|None=None,
        supports_streaming: bool|None=None, has_spoiler: bool|None=None
    ):
        self.type = type
        self.media = media
        if thumbnail is not None:
            self.thumbnail = thumbnail
        if caption is not None:
            self.caption = caption
        if parse_mode is not None:
            self.parse_mode = parse_mode
        if caption_entities is not None:
            self.caption_entities = caption_entities
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if duration is not None:
            self.duration = duration
        if supports_streaming is not None:
            self.supports_streaming = supports_streaming
        if has_spoiler is not None:
            self.has_spoiler = has_spoiler

class InputMediaAnimation:
    def __init__(
        self, media: str, type: str='animation', thumbnail: Optional[Union[InputFile, str]]=None,
        caption: str|None=None, parse_mode: str|None=None, caption_entities: Optional[List[MessageEntity]]=None,
        width: int|None=None, height: int|None=None, duration: int|None=None, has_spoiler: bool|None=None
    ):
        self.type = type
        self.media = media
        if thumbnail is not None:
            self.thumbnail = thumbnail
        if caption is not None:
            self.caption = caption
        if parse_mode is not None:
            self.parse_mode = parse_mode
        if caption_entities is not None:
            self.caption_entities = caption_entities
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if duration is not None:
            self.duration = duration
        if has_spoiler is not None:
            self.has_spoiler = has_spoiler

class InputMediaAudio:
    def __init__(
        self, media: str, type: str='audio', thumbnail: Optional[Union[InputFile, str]]=None,
        caption: str|None=None, parse_mode: str|None=None, caption_entities: Optional[List[MessageEntity]]=None,
        duration: int|None=None, performer: str|None=None, title: str|None=None
    ):
        self.type = type
        self.media = media
        if thumbnail is not None:
            self.thumbnail = thumbnail
        if caption is not None:
            self.caption = caption
        if parse_mode is not None:
            self.parse_mode = parse_mode
        if caption_entities is not None:
            self.caption_entities = caption_entities
        if duration is not None:
            self.duration = duration
        if performer is not None:
            self.performer = performer
        if title is not None:
            self.title = title

class InputMediaDocument:
    def __init__(
        self, media: str, type: str='document', thumbnail: Optional[Union[InputFile, str]]=None,
        caption: str|None=None, parse_mode: str|None=None, caption_entities: Optional[List[MessageEntity]]=None,
        disable_content_type_detection: bool|None=None
    ):
        self.type = type
        self.media = media
        if thumbnail is not None:
            self.thumbnail = thumbnail
        if caption is not None:
            self.caption = caption
        if parse_mode is not None:
            self.parse_mode = parse_mode
        if caption_entities is not None:
            self.caption_entities = caption_entities
        if disable_content_type_detection is not None:
            self.disable_content_type_detection = disable_content_type_detection

class InputMedia:
    @classmethod
    def dese(cls, json_):
        if json_ is None: return None
        obj = check_dict(json_)
        type = obj['type']

        if 'thumbnail' in obj:
            obj['thumbnail'] = InputFile.dese(obj.get('thumbnail'))

        if 'caption_entities' in obj:
            obj['caption_entities'] = [MessageEntity.dese(kwargs) for kwargs in obj.get('caption_entities')]

        if type == 'photo':
            return InputMediaPhoto(**obj)
        elif type == 'video':
            return InputMediaVideo(**obj)
        elif type == 'animation':
            return InputMediaAnimation(**obj)
        elif type == 'audio':
            return InputMediaAudio(**obj)
        elif type == 'document':
            return InputMediaDocument(**obj)
        else:
            return cls(**obj)
    def __init__(self, input_media:
        Union[InputMediaPhoto, InputMediaVideo, InputMediaAnimation, InputMediaAudio, InputMediaDocument]):

        available_input_media = (
            InputMediaPhoto, InputMediaVideo, InputMediaAnimation, InputMediaAudio, InputMediaDocument)

        if not isinstance(input_media, available_input_media):
            raise TypeError(f"menu parameter should be an instance of\n{[x.__name__ for x in available_input_media]}")
        self.__dict__ = input_media.__dict__

class MaskPosition:
    @classmethod
    def dese(cls, json_):
        if json_ is None: return None
        obj = check_dict(json_)
        obj['point'] = obj.get('point')
        obj['x_shift'] = obj.get('x_shift')
        obj['y_shift'] = obj.get('y_shift')
        obj['scale'] = obj.get('scale')
        return cls(**obj)
    def __init__(self, point: str, x_shift: float, y_shift: float, scale: float, **kwargs):
        self.point = point
        self.x_shift= x_shift
        self.y_shift = y_shift
        self.scale = scale

class Sticker:
    @classmethod
    def dese(cls, json_):
        if json_ is None: return None
        obj = check_dict(json_)
        obj['file_id'] = obj.get('file_id')
        obj['file_unique_id'] = obj.get('file_unique_id')
        obj['type'] = obj.get('type')
        obj['width'] = obj.get('width')
        obj['height'] = obj.get('height')
        obj['is_animated'] = obj.get('is_animated')
        obj['is_video'] = obj.get('is_video')
        obj['thumbnail'] = PhotoSize.dese(obj.get('thumbnail'))
        obj['emoji'] = obj.get('emoji')
        obj['set_name'] = obj.get('set_name')
        obj['premium_animation'] = File.dese(obj.get('premium_animation'))
        obj['mask_position'] = MaskPosition.dese(obj.get('mask_position'))
        obj['custom_emoji_id'] = obj.get('custom_emoji_id')
        obj['needs_repainting'] = obj.get('needs_repainting')
        obj['file_size'] = obj.get('file_size')
        return cls(**obj)
    def __init__(
        self, file_id: str, file_unique_id: str, type: str, width: int, height: int,
        is_animated: bool, is_video: bool, thumbnail: Optional[PhotoSize]=None, emoji: str|None=None, set_name: str|None=None,
        premium_animation: Optional[File]=None, mask_position: Optional[MaskPosition]=None, custom_emoji_id: str|None=None,
        needs_repainting: Optional[True]=None, file_size: int|None=None, **kwargs
    ):
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.type = type
        self.width = width
        self.height = height
        self.is_animated = is_animated
        self.is_video = is_video
        if thumbnail is not None:
            self.thumbnail = thumbnail
        if emoji is not None:
            self.emoji = emoji
        if set_name is not None:
            self.set_name = set_name
        if premium_animation is not None:
            self.premium_animation = premium_animation
        if mask_position is not None:
            self.mask_position = mask_position
        if custom_emoji_id is not None:
            self.custom_emoji_id = custom_emoji_id
        if needs_repainting is not None:
            self.needs_repainting = needs_repainting
        if file_size is not None:
            self.file_size = file_size

class StickerSet:
    @classmethod
    def dese(cls, json_):
        if json_ is None: return None
        obj = check_dict(json_)
        obj['name'] = obj.get('name')
        obj['title'] = obj.get('title')
        obj['sticker_type'] = obj.get('sticker_type')
        obj['is_animated'] = obj.get('is_animated')
        obj['is_video'] = obj.get('is_video')
        obj['stickers'] = [Sticker.dese(obj) for obj in obj.get('stickers')] if 'stickers' in obj else None
        obj['thumbnail'] = PhotoSize.dese(obj.get('thumbnail'))
        return cls(**obj)
    def __init__(
        self, name: str, title: str, sticker_type: str, is_animated: bool, is_video: bool,
        stickers: List[Sticker], thumbnail: Optional[PhotoSize]=None, **kwargs
    ):
        self.name = name
        self.title = title
        self.sticker_type = sticker_type
        self.is_animated = is_animated
        self.is_video = is_video
        self.stickers = stickers
        if thumbnail is not None:
            self.thumbnail = thumbnail

class InputSticker:
    @classmethod
    def dese(cls, json_):
        if json_ is None: return None
        obj = check_dict(json_)
        obj['sticker'] = obj.get('sticker')
        obj['emoji_list'] = obj.get('emoji_list')
        obj['mask_position'] = MaskPosition.dese(obj.get('mask_position'))
        obj['keywords'] = obj.get('keywords')
        return cls(**obj)
    def __init__(self, sticker: Union[InputFile, str], emoji_list: List[str],
        mask_position: Optional[MaskPosition]=None, keywords: Optional[List[str]]=None, **kwargs
    ):
        self.sticker = sticker
        self.emoji_list = emoji_list
        if mask_position is not None:
            self.mask_position = mask_position
        if keywords is not None:
            self.keywords = keywords

class InlineQuery:
    @classmethod
    def dese(cls, json_):
        if json_ is None: return None
        obj = check_dict(json_)
        obj['id'] = obj.get('id')
        obj['from_user'] = User.dese(obj.get('from'))
        obj['query'] = obj.get('query')
        obj['offset'] = obj.get('offset')
        obj['chat_type'] = obj.get('chat_type')
        obj['location'] = Location.dese(obj.get('location'))
        return cls(**obj)
    def __init__(self, id: str, from_user: User, query: str, offset: str,
        chat_type: str|None=None, location: Optional[Location]=None, **kwargs
    ):
        self.id: str = id
        self.from_user = from_user
        self.query: str = query
        self.offset: str = offset
        if chat_type is not None:
            self.chat_type = chat_type
        if location is not None:
            self.location = location

class InlineQueryResultsButton:
    @classmethod
    def dese(cls, json_):
        if json_ is None: return None
        obj = check_dict(json_)
        obj['text'] = obj.get('text')
        obj['web_app'] = WebAppInfo.dese(obj.get('web_app'))
        obj['start_parameter'] = obj.get('start_parameter')
        return cls(**obj)
    def __init__(
        self, text: str, web_app: Optional[WebAppInfo]=None,
        start_parameter: str|None=None, **kwargs
    ):
        self.text = text
        if web_app is not None:
            self.web_app = web_app
        if start_parameter is not None:
            self.start_parameter = start_parameter

class InlineQueryResult:
    @classmethod
    def dese(cls, json_):
        if json_ is None: return None
        obj = check_dict(json_)
        type = obj['type']
        if 'caption_entities' in obj: 
            obj['caption_entities'] = [MessageEntity.dese(kwargs) for kwargs in obj.get('caption_entities')] if 'caption_entities' in obj else None
        if 'reply_markup' in obj: 
            obj['reply_markup'] = InlineKeyboardMarkup.dese(obj.get('reply_markup'))
        if 'input_message_content' in obj: 
            obj['input_message_content'] = InputMessageContent.dese(obj.get('input_message_content'))

        if type == 'article':
            return InlineQueryResultArticle(**obj)
        elif type == 'photo' and 'photo_url' in obj:
            return InlineQueryResultPhoto(**obj)
        elif type == 'gif' and 'gif_url' in obj:
            return InlineQueryResultGif(**obj)
        elif type == 'mpeg4_gif' and 'mpeg4_url' in obj:
            return InlineQueryResultMpeg4Gif(**obj)
        elif type == 'video'and 'video_url' in obj:
            return InlineQueryResultVideo(**obj)
        elif type == 'audio' and 'audio_url' in obj:
            return InlineQueryResultAudio(**obj)
        elif type == 'voice' and 'voice_url' in obj:
            return InlineQueryResultVoice(**obj)
        elif type == 'document' and 'document_url' in obj:
            return InlineQueryResultDocument(**obj)
        elif type == 'location':
            return InlineQueryResultLocation(**obj)
        elif type == 'venue':
            return InlineQueryResultVenue(**obj)
        elif type == 'contact':
            return InlineQueryResultContact(**obj)
        elif type == 'game':
            return InlineQueryResultGame(**obj)
        elif type == 'photo': # duplicate
            return InlineQueryResultCachedPhoto(**obj)
        elif type == 'gif': # duplicate
            return InlineQueryResultCachedGif(**obj)
        elif type == 'mpeg4_gif': # duplicate
            return InlineQueryResultCachedMpeg4Gif(**obj)
        elif type == 'sticker':
            return InlineQueryResultCachedSticker(**obj)
        elif type == 'document': # duplicate
            return InlineQueryResultCachedDocument(**obj)
        elif type == 'video': # duplicate
            return InlineQueryResultCachedVideo(**obj)
        elif type == 'voice': # duplicate
            return InlineQueryResultCachedVoice(**obj)
        elif type == 'audio': # duplicate
            return InlineQueryResultCachedAudio(**obj)
        else:
            return cls(**obj)
    def __init__(
        self, type: str, id: str, reply_markup=None, thumbnail_width=None, thumbnail_mime_type=None, foursquare_type=None,
        first_name=None, video_file_id=None, mime_type=None, proximity_alert_radius=None, url=None, mpeg4_url=None, performer=None,
        longitude=None, thumbnail_url=None, audio_duration=None, google_place_type=None, vcard=None, gif_file_id=None,
        thumbnail_height=None, photo_height=None, document_url=None, voice_duration=None, voice_file_id=None, description=None,
        document_file_id=None, video_height=None, gif_url=None, photo_file_id=None, photo_width=None, audio_url=None, heading=None,
        latitude=None, gif_duration=None, video_duration=None, video_width=None, gif_width=None, caption=None, mpeg4_duration=None,
        live_period=None, photo_url=None, address=None, caption_entities=None, input_message_content=None, hide_url=None, mpeg4_width=None,
        mpeg4_height=None, foursquare_id=None, title=None, video_url=None, audio_file_id=None, parse_mode=None, google_place_id=None,
        last_name=None, phone_number=None, sticker_file_id=None, voice_url=None, horizontal_accuracy=None, game_short_name=None,
        mpeg4_file_id=None, gif_height=None, **kwargs
    ):
        self.id = id
        self.type = type
        if reply_markup is not None:
            self.reply_markup = reply_markup
        if thumbnail_width is not None:
            self.thumbnail_width = thumbnail_width
        if thumbnail_mime_type is not None:
            self.thumbnail_mime_type = thumbnail_mime_type
        if foursquare_type is not None:
            self.foursquare_type = foursquare_type
        if first_name is not None:
            self.first_name = first_name
        if video_file_id is not None:
            self.video_file_id = video_file_id
        if mime_type is not None:
            self.mime_type = mime_type
        if proximity_alert_radius is not None:
            self.proximity_alert_radius = proximity_alert_radius
        if url is not None:
            self.url = url
        if mpeg4_url is not None:
            self.mpeg4_url = mpeg4_url
        if performer is not None:
            self.performer = performer
        if longitude is not None:
            self.longitude = longitude
        if thumbnail_url is not None:
            self.thumbnail_url = thumbnail_url
        if audio_duration is not None:
            self.audio_duration = audio_duration
        if google_place_type is not None:
            self.google_place_type = google_place_type
        if vcard is not None:
            self.vcard = vcard
        if gif_file_id is not None:
            self.gif_file_id = gif_file_id
        if thumbnail_height is not None:
            self.thumbnail_height = thumbnail_height
        if photo_height is not None:
            self.photo_height = photo_height
        if document_url is not None:
            self.document_url = document_url
        if voice_duration is not None:
            self.voice_duration = voice_duration
        if voice_file_id is not None:
            self.voice_file_id = voice_file_id
        if description is not None:
            self.description = description
        if document_file_id is not None:
            self.document_file_id = document_file_id
        if video_height is not None:
            self.video_height = video_height
        if gif_url is not None:
            self.gif_url = gif_url
        if photo_file_id is not None:
            self.photo_file_id = photo_file_id
        if photo_width is not None:
            self.photo_width = photo_width
        if audio_url is not None:
            self.audio_url = audio_url
        if heading is not None:
            self.heading = heading
        if latitude is not None:
            self.latitude = latitude
        if gif_duration is not None:
            self.gif_duration = gif_duration
        if video_duration is not None:
            self.video_duration = video_duration
        if video_width is not None:
            self.video_width = video_width
        if gif_width is not None:
            self.gif_width = gif_width
        if caption is not None:
            self.caption = caption
        if mpeg4_duration is not None:
            self.mpeg4_duration = mpeg4_duration
        if live_period is not None:
            self.live_period = live_period
        if photo_url is not None:
            self.photo_url = photo_url
        if address is not None:
            self.address = address
        if caption_entities is not None:
            self.caption_entities = caption_entities
        if input_message_content is not None:
            self.input_message_content = input_message_content
        if hide_url is not None:
            self.hide_url = hide_url
        if mpeg4_width is not None:
            self.mpeg4_width = mpeg4_width
        if mpeg4_height is not None:
            self.mpeg4_height = mpeg4_height
        if foursquare_id is not None:
            self.foursquare_id = foursquare_id
        if title is not None:
            self.title = title
        if video_url is not None:
            self.video_url = video_url
        if audio_file_id is not None:
            self.audio_file_id = audio_file_id
        if parse_mode is not None:
            self.parse_mode = parse_mode
        if google_place_id is not None:
            self.google_place_id = google_place_id
        if last_name is not None:
            self.last_name = last_name
        if phone_number is not None:
            self.phone_number = phone_number
        if sticker_file_id is not None:
            self.sticker_file_id = sticker_file_id
        if voice_url is not None:
            self.voice_url = voice_url
        if horizontal_accuracy is not None:
            self.horizontal_accuracy = horizontal_accuracy
        if game_short_name is not None:
            self.game_short_name = game_short_name
        if mpeg4_file_id is not None:
            self.mpeg4_file_id = mpeg4_file_id
        if gif_height is not None:
            self.gif_height = gif_height

class InlineQueryResultArticle(InlineQueryResult):
    pass
class InlineQueryResultPhoto(InlineQueryResult):
    pass
class InlineQueryResultGif(InlineQueryResult):
    pass
class InlineQueryResultMpeg4Gif(InlineQueryResult):
    pass
class InlineQueryResultVideo(InlineQueryResult):
    pass
class InlineQueryResultAudio(InlineQueryResult):
    pass
class InlineQueryResultVoice(InlineQueryResult):
    pass
class InlineQueryResultDocument(InlineQueryResult):
    pass
class InlineQueryResultLocation(InlineQueryResult):
    pass
class InlineQueryResultVenue(InlineQueryResult):
    pass
class InlineQueryResultContact(InlineQueryResult):
    pass
class InlineQueryResultGame(InlineQueryResult):
    pass
class InlineQueryResultCachedPhoto(InlineQueryResult):
    pass
class InlineQueryResultCachedGif(InlineQueryResult):
    pass
class InlineQueryResultCachedMpeg4Gif(InlineQueryResult):
    pass
class InlineQueryResultCachedSticker(InlineQueryResult):
    pass
class InlineQueryResultCachedDocument(InlineQueryResult):
    pass
class InlineQueryResultCachedVideo(InlineQueryResult):
    pass
class InlineQueryResultCachedVoice(InlineQueryResult):
    pass
class InlineQueryResultCachedAudio(InlineQueryResult):
    pass

class InputTextMessageContent:
    def __init__(
        self, message_text: str, parse_mode: str|None=None,
        entities: Optional[List[MessageEntity]]=None, disable_web_page_preview: bool|None=None, **kwargs
    ):
        self.message_text = message_text
        if parse_mode is not None:
            self.parse_mode = parse_mode
        if entities is not None:
            self.entities = entities
        if disable_web_page_preview is not None:
            self.disable_web_page_preview = disable_web_page_preview

class InputLocationMessageContent:
    def __init__(
        self, latitude: float, longitude: float, horizontal_accuracy: float|None=None,
        live_period: int|None=None, heading: int|None=None, proximity_alert_radius: int|None=None, **kwargs
    ):
        self.latitude = latitude
        self.longitude = longitude
        if horizontal_accuracy is not None:
            self.horizontal_accuracy = horizontal_accuracy
        if live_period is not None:
            self.live_period = live_period
        if heading is not None:
            self.heading = heading
        if proximity_alert_radius is not None:
            self.proximity_alert_radius = proximity_alert_radius

class InputVenueMessageContent:
    def __init__(self, latitude: float, longitude: float, title: str, address: str,
        foursquare_id: str|None=None, foursquare_type: str|None=None,
        google_place_id: str|None=None, google_place_type: str|None=None, **kwargs
    ):
        self.latitude = latitude
        self.longitude = longitude
        self.title = title
        self.address = address
        if foursquare_id is not None:
            self.foursquare_id = foursquare_id
        if foursquare_type is not None:
            self.foursquare_type = foursquare_type
        if google_place_id is not None:
            self.google_place_id = google_place_id
        if google_place_type is not None:
            self.google_place_type = google_place_type

class InputContactMessageContent:
    def __init__(self, phone_number: str, first_name: str,
        last_name: str|None=None, vcard: str|None=None, **kwargs
    ):
        self.phone_number = phone_number
        self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if vcard is not None:
            self.vcard = vcard

class InputInvoiceMessageContent:
    def __init__(
        self, title: str, description: str, payload: str, provider_token: str, currency: str,
        prices: List[LabeledPrice], max_tip_amount: int|None=None, suggested_tip_amounts: Optional[List[int]]=None,
        provider_data: str|None=None, photo_url: str|None=None, photo_size: int|None=None, photo_width: int|None=None,
        photo_height: int|None=None, need_name: bool|None=None, need_phone_number: bool|None=None, need_email: bool|None=None,
        need_shipping_address: bool|None=None, send_phone_number_to_provider: bool|None=None,
        send_email_to_provider: bool|None=None, is_flexible: bool|None=None, **kwargs
    ):
        self.title = title
        self.description = description
        self.payload = payload
        self.provider_token = provider_token
        self.currency = currency
        self.prices = prices
        if max_tip_amount is not None:
            self.max_tip_amount = max_tip_amount
        if suggested_tip_amounts is not None:
            self.suggested_tip_amounts = suggested_tip_amounts
        if provider_data is not None:
            self.provider_data = provider_data
        if photo_url is not None:
            self.photo_url = photo_url
        if photo_size is not None:
            self.photo_size = photo_size
        if photo_width is not None:
            self.photo_width = photo_width
        if photo_height is not None:
            self.photo_height = photo_height
        if need_name is not None:
            self.need_name = need_name
        if need_phone_number is not None:
            self.need_phone_number = need_phone_number
        if need_email is not None:
            self.need_email = need_email
        if need_shipping_address is not None:
            self.need_shipping_address = need_shipping_address
        if send_phone_number_to_provider is not None:
            self.send_phone_number_to_provider = send_phone_number_to_provider
        if send_email_to_provider is not None:
            self.send_email_to_provider = send_email_to_provider
        if is_flexible is not None:
            self.is_flexible = is_flexible

class InputMessageContent:
    @classmethod
    def dese(cls, json_):
        if json_ is None: return None
        obj = check_dict(json_)
        if 'message_text' in obj:
            obj['entities'] = [MessageEntity.dese(kwargs) for kwargs in obj.get('entities')] if 'entities' in obj else None
            return InputTextMessageContent(**obj)
        elif 'address' in obj:
            return InputVenueMessageContent(**obj)
        elif 'latitude' in obj:
            return InputLocationMessageContent(**obj)
        elif 'phone_number' in obj:
            return InputContactMessageContent(**obj)
        elif 'currency' in obj:
            obj['prices'] = [LabeledPrice.dese(obj) for obj in obj.get('prices')] if 'prices' in obj else None
            return InputInvoiceMessageContent(**obj)
        else:
            return cls(**obj)
    def __init__(self, input_message_content: Union[
        InputTextMessageContent, InputVenueMessageContent,
        InputLocationMessageContent, InputContactMessageContent, InputInvoiceMessageContent
    ]):
        available_inputs = (
        InputTextMessageContent, InputVenueMessageContent,
        InputLocationMessageContent, InputContactMessageContent, InputInvoiceMessageContent
    )
        available_input_names = [i.__name__ for i in available_inputs]
        if not isinstance(input_message_content, available_inputs):
            raise TypeError(f'input_message_content parameter should be an instance of\n{available_input_names}')
        self.__dict__ = input_message_content.__dict__

class ChosenInlineResult:
    @classmethod
    def dese(cls, json_):
        if json_ is None: return None
        obj = check_dict(json_)
        obj['result_id'] = obj.get('result_id')
        obj['from_user'] = User.dese(obj.get('from'))
        obj['location'] = Location.dese(obj.get('location'))
        obj['inline_message_id'] = obj.get('inline_message_id')
        obj['query'] = obj.get('query')
        return cls(**obj)
    def __init__(
        self, result_id: str, from_user: User, query: str,
        location: Optional[Location]=None, inline_message_id: str|None=None, **kwargs
    ):
        self.result_id = result_id
        self.from_user = from_user
        self.query = query
        if location is not None:
            self.location = location
        if inline_message_id is not None:
            self.inline_message_id = inline_message_id

class SentWebAppMessage:
    @classmethod
    def dese(cls, json_):
        if json_ is None: return None
        obj = check_dict(json_)
        obj['inline_message_id'] = obj.get('inline_message_id')
        return cls(**obj)
    def __init__(self, inline_message_id: str|None=None, **kwargs):
        if inline_message_id is not None:
            self.inline_message_id = inline_message_id

class Invoice:
    @classmethod
    def dese(cls, json_):
        if json_ is None: return None
        obj = check_dict(json_)
        obj['title'] = obj.get('title')
        obj['description'] = obj.get('description')
        obj['start_parameter'] = obj.get('start_parameter')
        obj['currency'] = obj.get('currency')
        obj['total_amount'] = obj.get('total_amount')
        return cls(**obj)
    def __init__(
        self, title: str, description: str, start_parameter: str,
        currency: str, total_amount: int, **kwargs
    ):
        self.title = title
        self.description = description
        self.start_parameter = start_parameter
        self.currency = currency
        self.total_amount = total_amount

class ShippingAddress:
    @classmethod
    def dese(cls, json_):
        if json_ is None: return None
        obj = check_dict(json_)
        obj['country_code'] = obj.get('country_code')
        obj['state'] = obj.get('state')
        obj['city'] = obj.get('city')
        obj['street_line1'] = obj.get('street_line1')
        obj['street_line2'] = obj.get('street_line2')
        obj['post_code'] = obj.get('post_code')
        return cls(**obj)
    def __init__(
        self, country_code: str, state: str, city: str, street_line1: str,
        street_line2: str, post_code: str, **kwargs
    ):
        self.country_code = country_code
        self.state = state
        self.city = city
        self.street_line1 = street_line1
        self.street_line2 = street_line2
        self.post_code = post_code

class OrderInfo:
    @classmethod
    def dese(cls, json_):
        if json_ is None: return None
        obj = check_dict(json_)
        obj['name'] = obj.get('name')
        obj['phone_number'] = obj.get('phone_number')
        obj['email'] = obj.get('email')
        obj['shipping_address'] = ShippingAddress.dese(obj.get('shipping_address'))
        return cls(**obj)
    def __init__(
        self, name: str|None=None, phone_number: str|None=None, email: str|None=None,
        shipping_address: Optional[ShippingAddress]=None, **kwargs
    ):
        if name is not None:
            self.name = name
        if phone_number is not None:
            self.phone_number = phone_number
        if email is not None:
            self.email = email
        if shipping_address is not None:
            self.shipping_address = shipping_address

class ShippingOption:
    @classmethod
    def dese(cls, json_):
        if json_ is None: return None
        obj = check_dict(json_)
        obj['id'] = obj.get('id')
        obj['title'] = obj.get('title')
        obj['prices'] = [LabeledPrice.dese(obj) for obj in obj.get('prices')] if 'prices' in obj else None
        return cls(**obj)
    def __init__(self, id: str, title: str, prices: List[LabeledPrice], **kwargs):
        self.id = id
        self.title = title
        self.prices = prices

class SuccessfulPayment:
    @classmethod
    def dese(cls, json_):
        if json_ is None: return None
        obj = check_dict(json_)
        obj['currency'] = obj.get('currency')
        obj['total_amount'] = obj.get('total_amount')
        obj['invoice_payload'] = obj.get('invoice_payload')
        obj['shipping_option_id'] = obj.get('shipping_option_id')
        obj['order_info'] = OrderInfo.dese(obj.get('order_info'))
        obj['telegram_payment_charge_id'] = obj.get('telegram_payment_charge_id')
        obj['provider_payment_charge_id'] = obj.get('provider_payment_charge_id')
        return cls(**obj)
    def __init__(
        self, currency: str, total_amount: int, invoice_payload: str,
        telegram_payment_charge_id: str, provider_payment_charge_id: str,
        shipping_option_id: str|None=None, order_info: Optional[OrderInfo]=None, **kwargs
    ):
        self.currency = currency
        self.total_amount = total_amount
        self.invoice_payload = invoice_payload
        self.telegram_payment_charge_id = telegram_payment_charge_id
        self.provider_payment_charge_id = provider_payment_charge_id
        if shipping_option_id is not None:
            self.shipping_option_id = shipping_option_id
        if order_info is not None:
            self.order_info = order_info

class ShippingQuery:
    @classmethod
    def dese(cls, json_):
        if json_ is None: return None
        obj = check_dict(json_)
        obj['id'] = obj.get('id')
        obj['from_user'] = User.dese(obj.get('from'))
        obj['invoice_payload'] = obj.get('invoice_payload')
        obj['shipping_address'] = ShippingAddress.dese(obj.get('shipping_address'))
        return cls(**obj)
    def __init__(
        self, id: str, from_user: User, invoice_payload: str,
        shipping_address: ShippingAddress, **kwargs
    ):
        self.id = id
        self.from_user = from_user
        self.invoice_payload = invoice_payload
        self.shipping_address = shipping_address

class PreCheckoutQuery:
    @classmethod
    def dese(cls, json_):
        if json_ is None: return None
        obj = check_dict(json_)
        obj['id'] = obj.get('id')
        obj['from_user'] = User.dese(obj.get('from'))
        obj['currency'] = obj.get('currency')
        obj['total_amount'] = obj.get('total_amount')
        obj['invoice_payload'] = obj.get('invoice_payload')
        obj['shipping_option_id'] = obj.get('shipping_option_id')
        obj['order_info'] = OrderInfo.dese(obj.get('order_info'))
        return cls(**obj)
    def __init__(
        self, id: str, from_user: User, currency: str, total_amount: int,
        invoice_payload: str, shipping_option_id: str|None=None,
        order_info: Optional[OrderInfo]=None, **kwargs
    ):
        self.id = id
        self.from_user = from_user
        self.currency = currency
        self.total_amount = total_amount
        self.invoice_payload = invoice_payload
        if shipping_option_id is not None:
            self.shipping_option_id = shipping_option_id
        if order_info is not None:
            self.order_info = order_info

class PassportFile:
    @classmethod
    def dese(cls, json_):
        if json_ is None: return None
        obj = check_dict(json_)
        obj['file_id'] = obj.get('file_id')
        obj['file_unique_id'] = obj.get('file_unique_id')
        obj['file_size'] = obj.get('file_size')
        obj['file_date'] = obj.get('file_date')
        return cls(**obj)
    def __init__(
        self, file_id: str, file_unique_id: str,
        file_size: int, file_date: int, **kwargs
    ):
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.file_size = file_size
        self.file_date = file_date

class EncryptedPassportElement:
    @classmethod
    def dese(cls, json_):
        if json_ is None: return None
        obj = check_dict(json_)
        obj['type'] = obj.get('type')
        obj['data'] = obj.get('data')
        obj['phone_number'] = obj.get('phone_number')
        obj['email'] = obj.get('email')
        obj['files'] = [PassportFile.dese(kwargs) for kwargs in obj.get('files')] if 'files' in obj else None
        obj['front_side'] = PassportFile.dese(obj.get('front_side'))
        obj['reverse_side'] = PassportFile.dese(obj.get('reverse_side'))
        obj['selfie'] = PassportFile.dese(obj.get('selfie'))
        obj['translation'] = obj.get('translation')
        obj['hash'] = [PassportFile.dese(kwargs) for kwargs in obj.get('hash')] if 'hash' in obj else None
        return cls(**obj)
    def __init__(self, type: str, hash: str, data: str|None=None, phone_number: str|None=None, email: str|None=None,
        files: Optional[List[PassportFile]]=None, front_side: Optional[PassportFile]=None, reverse_side: Optional[PassportFile]=None,
        selfie: Optional[PassportFile]=None, translation: Optional[List[PassportFile]]=None, **kwargs
    ):
        self.type = type
        self.hash = hash
        if data is not None:
            self.data = data
        if phone_number is not None:
            self.phone_number = phone_number
        if email is not None:
            self.email = email
        if files is not None:
            self.files = files
        if front_side is not None:
            self.front_side = front_side
        if reverse_side is not None:
            self.reverse_side = reverse_side
        if selfie is not None:
            self.selfie = selfie
        if translation is not None:
            self.translation = translation

class EncryptedCredentials:
    @classmethod
    def dese(cls, json_):
        if json_ is None: return None
        obj = check_dict(json_)
        obj['data'] = obj.get('data')
        obj['hash'] = obj.get('hash')
        obj['secret'] = obj.get('secret')
        return cls(**obj)
    def __init__(self, data: str, hash: str, secret: str, **kwargs):
        self.data = data
        self.hash = hash
        self.secret = secret

class PassportData:
    @classmethod
    def dese(cls, json_):
        if json_ is None: return None
        obj = check_dict(json_)
        obj['data'] = [EncryptedPassportElement.dese(obj) for obj in obj.get('data')] if 'data' in obj else None
        obj['credentials'] = EncryptedCredentials.dese(obj.get('credentials'))
        return cls(**obj)
    def __init__(self, data: List[EncryptedPassportElement], credentials: EncryptedCredentials, **kwargs):
        self.data = data
        self.credentials = credentials

class PassportElementError:
    @classmethod
    def dese(cls, json_):
        if json_ is None: return None
        obj = check_dict(json_)
        source = obj['source']
        if source == 'data':
            return PassportElementErrorDataField(**obj)
        elif source == 'front_side':
            return PassportElementErrorFrontSide(**obj)
        elif source == 'reverse_side':
            return PassportElementErrorReverseSide(**obj)
        elif source == 'selfie':
            return PassportElementErrorSelfie(**obj)
        elif source == 'file':
            return PassportElementErrorFile(**obj)
        elif source == 'files':
            return PassportElementErrorFiles(**obj)
        elif source == 'translation_file':
            return PassportElementErrorTranslationFile(**obj)
        elif source == 'translation_files':
            return PassportElementErrorTranslationFiles(**obj)
        elif source == 'unspecified':
            return PassportElementErrorUnspecified(**obj)
        else:
            return cls(**obj)
    def __init__(
        self, message: str, type: str, source: str, data_hash=None, field_name=None,
        file_hashes=None, file_hash=None, element_hash=None, **kwargs
    ):
        self.message = message
        self.type = type
        self.source = source
        if data_hash is not None:
            self.data_hash = data_hash
        if field_name is not None:
            self.field_name = field_name
        if file_hashes is not None:
            self.file_hashes = file_hashes
        if file_hash is not None:
            self.file_hash = file_hash
        if element_hash is not None:
            self.element_hash = element_hash

class PassportElementErrorDataField(PassportElementError):
    pass
class PassportElementErrorFrontSide(PassportElementError):
    pass
class PassportElementErrorReverseSide(PassportElementError):
    pass
class PassportElementErrorSelfie(PassportElementError):
    pass
class PassportElementErrorFile(PassportElementError):
    pass
class PassportElementErrorFiles(PassportElementError):
    pass
class PassportElementErrorTranslationFile(PassportElementError):
    pass
class PassportElementErrorTranslationFiles(PassportElementError):
    pass
class PassportElementErrorUnspecified(PassportElementError):
    pass

class Game:
    @classmethod
    def dese(cls, json_):
        if json_ is None: return None
        obj = check_dict(json_)
        obj['title'] = obj.get('title')
        obj['description'] = obj.get('description')
        obj['photo'] = [PhotoSize.dese(obj) for obj in obj.get('photo')] if 'photo' in obj else None
        obj['text'] = obj.get('text')
        obj['text_entities'] = [MessageEntity.dese(kwargs) for kwargs in obj.get('text_entities')] if 'text_entities' in obj else None
        obj['animation'] = Animation.dese(obj.get('animation'))
        return cls(**obj)
    def __init__(
        self, title: str, description: str, photo: List[PhotoSize], text: str|None=None,
        text_entities: Optional[List[MessageEntity]]=None, animation: Optional[Animation]=None, **kawrgs
    ):
        self.title = title
        self.description = description
        self.photo = photo
        if text is not None:
            self.text = text
        if text_entities is not None:
            self.text_entities = text_entities
        if animation is not None:
            self.animation = animation

class GameHighScore:
    @classmethod
    def dese(cls, json_):
        if json_ is None: return None
        obj = check_dict(json_)
        obj['position'] = obj.get('position')
        obj['user'] = User.dese(obj.get('user'))
        obj['score'] = obj.get('score')
        return cls(**obj)
    def __init__(self, position: int, user: User, score: int, **kwargs):
        self.position = position
        self.user = user
        self.score = score

class Update:
    @classmethod
    def dese(cls, json_):
        if json_ is None: return None
        obj = check_dict(json_)
        obj['update_id'] = obj.get('update_id')
        obj['message'] = Message.dese(obj.get('message'))
        obj['edited_message'] = Message.dese(obj.get('edited_message'))
        obj['channel_post'] = Message.dese(obj.get('channel_post'))
        obj['edited_channel_post'] = Message.dese(obj.get('edited_channel_post'))
        obj['inline_query'] = InlineQuery.dese(obj.get('inline_query'))
        obj['chosen_inline_result'] = ChosenInlineResult.dese(obj.get('chosen_inline_result'))
        obj['callback_query'] = CallbackQuery.dese(obj.get('callback_query'))
        obj['shipping_query'] = ShippingQuery.dese(obj.get('shipping_query'))
        obj['pre_checkout_query'] = PreCheckoutQuery.dese(obj.get('pre_checkout_query'))
        obj['poll'] = Poll.dese(obj.get('poll'))
        obj['poll_answer'] = PollAnswer.dese(obj.get('poll_answer'))
        obj['my_chat_member'] = ChatMemberUpdated.dese(obj.get('my_chat_member'))
        obj['chat_member'] = ChatMemberUpdated.dese(obj.get('chat_member'))
        obj['chat_join_request'] = ChatJoinRequest.dese(obj.get('chat_join_request'))
        return cls(**obj)
    def __init__(
        self, update_id: int, message: Optional[Message]=None, edited_message: Optional[Message]=None, channel_post: Optional[Message]=None,
        edited_channel_post: Optional[Message]=None, inline_query: Optional[InlineQuery]=None, chosen_inline_result: Optional[ChosenInlineResult]=None,
        callback_query: Optional[CallbackQuery]=None, shipping_query: Optional[ShippingQuery]=None, pre_checkout_query: Optional[PreCheckoutQuery]=None,
        poll: Optional[Poll]=None, poll_answer: Optional[PollAnswer]=None, my_chat_member: Optional[ChatMemberUpdated]=None, chat_member: Optional[ChatMemberUpdated]=None,
        chat_join_request: Optional[ChatJoinRequest]=None, **kwargs
    ):
        self.update_id = update_id
        if message is not None:
            self.message = message
        if edited_message is not None:
            self.edited_message = edited_message
        if channel_post is not None:
            self.channel_post = channel_post
        if edited_channel_post is not None:
            self.edited_channel_post = edited_channel_post
        if inline_query is not None:
            self.inline_query = inline_query
        if chosen_inline_result is not None:
            self.chosen_inline_result = chosen_inline_result
        if callback_query is not None:
            self.callback_query = callback_query
        if shipping_query is not None:
            self.shipping_query = shipping_query
        if pre_checkout_query is not None:
            self.pre_checkout_query = pre_checkout_query
        if poll is not None:
            self.poll = poll
        if poll_answer is not None:
            self.poll_answer = poll_answer
        if my_chat_member is not None:
            self.my_chat_member = my_chat_member
        if chat_member is not None:
            self.chat_member = chat_member
        if chat_join_request is not None:
            self.chat_join_request = chat_join_request

