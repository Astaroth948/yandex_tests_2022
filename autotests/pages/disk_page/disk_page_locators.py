from dataclasses import dataclass
from pathlib import Path

from selenium.webdriver.common.by import By

PATH_TO_FILE = Path('autotests', 'data', 'file.txt')


@dataclass
class DiskPageLocators:
    FLAG_DISK_PAGE: tuple = (By.XPATH, '//a[contains(@class, "PSHeaderService_active")]/span[text()="Диск"]')
    DESIRED_FILE: tuple = (By.XPATH, '//div[@class="listing__items"]//div[@aria-label="name_file-&"]')
    UNNECESSARY_FILES: tuple = (By.XPATH, '//div[@class="listing__items"]//div[@aria-label!="name_file-&"]')
    FOLDER_TITLE: tuple = (By.XPATH, '//div[@class="listing-heading__title-inner"]')


@dataclass
class ActionBarLocators:
    BUTTON_COPY: tuple = (By.XPATH, '//button[@aria-label="Копировать"]')
    BUTTON_DELETE: tuple = (By.XPATH, '//button[@aria-label="Удалить"]')


@dataclass
class ModalLocators:
    MODAL_TITLE: tuple = (By.XPATH, '//div[@class="Modal-Content"]//h2')
    MODAL_FOLDER: tuple = (By.XPATH, '//div[@class="Modal-Content"]//div[@title="name_folder-&"]')
    BUTTON_COPY: tuple = (By.XPATH, '//div[@class="Modal-Content"]//button/span[text()="Копировать"]/parent::button')
    INPUT_CREATE_FOLDER: tuple = (By.XPATH, '//div[@class="Modal-Content"]//input')
    BUTTON_SAVE: tuple = (By.XPATH, '//div[@class="Modal-Content"]//button/span[text()="Сохранить"]/parent::button')


@dataclass
class ToastsLocators:
    TOAST: tuple = (By.XPATH, '//div[@class="notifications__text js-message"]')
    UPLOADER_TITLE: tuple = (By.XPATH, '//div[@class="uploader-progress"]//h3')
    UPLOADER_CLOSE: tuple = (By.XPATH, '//div[@class="uploader-progress"]//button[@aria-label="Закрыть"]')


@dataclass
class DiskLeftPanelLocators:
    FILES: tuple = (By.XPATH, '//div[@class="LeftColumn__InnerWrapperTop"]//span[@id="/disk"]')
    BUTTON_CREATE: tuple = (By.XPATH, '//span[@class="create-resource-popup-with-anchor"]/button')
    BUTTON_CREATE_FOLDER: tuple = (By.XPATH, '//button[@aria-label="Папку"]')
    INPUT_UPLOAD_FILE: tuple = (
        By.XPATH,
        '//div[@class="LeftColumn__InnerWrapperTop"]//input[@title="Загрузить файлы"]',
    )


@dataclass
class FileViewerLocators:
    PAGE_1: tuple = (By.XPATH, '//div[@class="__page-1"]')


@dataclass
class ModalText:
    TITLE_COPY: str = 'Куда копировать «name_file-&»?'
    TITLE_CREATE_FOLDER: str = 'Укажите название папки'


@dataclass
class ToastsText:
    TOAST_COPY: str = 'Файл «name_file-&» скопирован в папку «name_folder-&»'
    UPLOADER_TITLE: str = 'Все файлы загружены'
