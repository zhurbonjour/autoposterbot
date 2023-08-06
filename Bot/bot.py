import telebot
from telebot.types import InputMediaPhoto
import os
from config import CHAT_ID


class TelegramChannelDispatcher(telebot.TeleBot):

    def __init__(self, token: str):
        super().__init__(token)

    def _get_files(self) -> list:
        return os.listdir('tmp/')

    def _get_media_group(self, files: list) -> list:
        group_photo = []
        for file in files:
            path = f'tmp/{file}'
            group_photo.append(InputMediaPhoto(open(path, 'rb')))
        return group_photo

    def _send_files_to_channel(self, media_group: list):
        self.send_media_group(chat_id=CHAT_ID, media=media_group)

    def _clear_tmp_dir(self, files):
        for file in files:
            os.remove(f'tmp/{file}')

    def dispatch_channel(self):
        files = self._get_files()
        if files:
            media_group = self._get_media_group(files)
            self._send_files_to_channel(media_group)
            self._clear_tmp_dir(files)
        else:
            pass