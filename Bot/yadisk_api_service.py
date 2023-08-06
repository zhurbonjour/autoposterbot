"""
Функционал подразумевает обращение к АПИ яндекс диска
с целью получения изображений и дальнейших операций с ними
Класс диспетчера должен инкапсулировать логику получения
для дальнейшей обработки изображений,
а так же функционал обработки их на сервере
то есть сохранение, анализ, отправку и удаление
"""
import yadisk
import random
from config import PREP_DIR, PAST_DIR


class YaCloudDispatcher(yadisk.YaDisk):
    def __init__(self, token):
        super().__init__(token=token)

    def _get_files_names(self) -> list:
        files_qtt = random.randint(1, 2)
        files_generator = super().listdir(PREP_DIR)
        return [files_generator.__next__()['name'] for i in range(files_qtt)]

    def _download_files(self, filenames: list):
        for file in filenames:
            super().download(f'{PREP_DIR}/{file}', f'./tmp/{file}')

    def _move_files(self, filenames: list):
        for file in filenames:
            super().move(f'{PREP_DIR}/{file}', f'{PAST_DIR}/{file}')

    def dispatch_cloud(self):
        try:
            filenames = self._get_files_names()
            if filenames:
                self._download_files(filenames)
                self._move_files(filenames)
        except:
            pass