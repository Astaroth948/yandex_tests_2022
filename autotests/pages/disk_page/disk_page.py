from pathlib import Path

import allure

from autotests.pages.base_page import BasePage
from autotests.pages.disk_page.disk_page_locators import (
    ActionBarLocators,
    DiskLeftPanelLocators,
    DiskPageLocators,
    FileViewerLocators,
    ModalLocators,
    ToastsLocators,
    ToastsText,
)


class DiskPage(BasePage):
    @allure.step('Проверить, что открылась страница Яндекс Диска')
    def assert_open_disk_page(self, timeout: int = 20) -> None:
        self.find_element(locator=DiskPageLocators.FLAG_DISK_PAGE, timeout=timeout)

    @allure.step("Нажать на файл или папку '{name_file}'")
    def click_file(self, name_file: str, timeout: int = 5) -> None:
        self.click(
            locator=(
                DiskPageLocators.DESIRED_FILE[0],
                DiskPageLocators.DESIRED_FILE[1].replace('name_file-&', name_file),
            ),
            timeout=timeout,
        )

    @allure.step("Найти файл или папку '{name_file}'")
    def assert_file(self, name_file: str, timeout: int = 5) -> None:
        self.find_element(
            locator=(
                DiskPageLocators.DESIRED_FILE[0],
                DiskPageLocators.DESIRED_FILE[1].replace('name_file-&', name_file),
            ),
            timeout=timeout,
        )

    @allure.step("Перейти в папку или открыть файл '{name_folder}'")
    def goto_folder(self, name_folder: str, timeout: int = 5) -> None:
        self.double_click(
            locator=(
                DiskPageLocators.DESIRED_FILE[0],
                DiskPageLocators.DESIRED_FILE[1].replace('name_file-&', name_folder),
            ),
            timeout=timeout,
        )

    @allure.step("Выделить все файлы, кроме '{name_file}'")
    def select_unnecessary_files(self, name_file: str) -> None:
        self.select_files(
            locator=(
                DiskPageLocators.UNNECESSARY_FILES[0],
                DiskPageLocators.UNNECESSARY_FILES[1].replace('name_file-&', name_file),
            )
        )

    @allure.step("Проверить, что открылась директория '{name_folder}'")
    def assert_open_folder(self, name_folder: str, timeout: int = 10) -> None:
        self.assert_text_in_element_equal_to(locator=DiskPageLocators.FOLDER_TITLE, text=name_folder, timeout=timeout)

    @allure.step("Проверить, что удалились все файлы, кроме '{name_file}'")
    def assert_unnecessary_files_deleted(self, name_file: str, timeout: int = 10) -> None:
        self.assert_quantity_of_elements(
            locator=(
                DiskPageLocators.UNNECESSARY_FILES[0],
                DiskPageLocators.UNNECESSARY_FILES[1].replace('name_file-&', name_file),
            ),
            quantity=0,
            timeout=timeout,
        )
        self.assert_quantity_of_elements(
            locator=(
                DiskPageLocators.DESIRED_FILE[0],
                DiskPageLocators.DESIRED_FILE[1].replace('name_file-&', name_file),
            ),
            quantity=1,
            timeout=timeout,
        )

    @allure.step("Проверить, что файл '{name_file}' удалился")
    def assert_desired_file_deleted(self, name_file: str, timeout: int = 10) -> None:
        self.assert_quantity_of_elements(
            locator=(
                DiskPageLocators.DESIRED_FILE[0],
                DiskPageLocators.DESIRED_FILE[1].replace('name_file-&', name_file),
            ),
            quantity=0,
            timeout=timeout,
        )

    @allure.step("Получить кол-во файлов, кроме '{name_file}'")
    def get_len_unnecessary_files(self, name_file: str) -> int:
        return len(
            self.find_elements(
                locator=(
                    DiskPageLocators.UNNECESSARY_FILES[0],
                    DiskPageLocators.UNNECESSARY_FILES[1].replace('name_file-&', name_file),
                )
            )
        )


class ActionBar(BasePage):
    @allure.step("Нажать на кнопку 'Копировать'")
    def click_button_copy(self, timeout: int = 5) -> None:
        self.click(locator=ActionBarLocators.BUTTON_COPY, timeout=timeout)

    @allure.step("Нажать на кнопку 'Удалить'")
    def click_button_delete(self, timeout: int = 5) -> None:
        self.click(locator=ActionBarLocators.BUTTON_DELETE, timeout=timeout)


class Modal(BasePage):
    @allure.step('Проверить, что открылось модальное окно с заголовком {title}')
    def assert_open_modal(self, title: str, timeout: int = 5) -> None:
        self.assert_text_in_element_equal_to(locator=ModalLocators.MODAL_TITLE, text=title, timeout=timeout)

    @allure.step('Проверить, что модальное окно закрылось')
    def assert_modal_closed(self, timeout: int = 5) -> None:
        self.assert_element_closed(locator=ModalLocators.MODAL_TITLE, timeout=timeout)

    @allure.step("Нажать на директорию копирования: '{name_folder}' в модальном окне")
    def click_folder(self, name_folder: str, timeout: int = 5) -> None:
        self.click(
            locator=(
                ModalLocators.MODAL_FOLDER[0],
                ModalLocators.MODAL_FOLDER[1].replace('name_folder-&', name_folder),
            ),
            timeout=timeout,
        )

    @allure.step("Нажать на кнопку 'Копировать' в модальном окне")
    def click_button_copy(self, timeout: int = 5) -> None:
        self.click(locator=ModalLocators.BUTTON_COPY, timeout=timeout)

    @allure.step("Ввести название папки: '{name_folder}'")
    def input_name_folder(self, name_folder: str, timeout: int = 5) -> None:
        self.clear_input(locator=ModalLocators.INPUT_CREATE_FOLDER, timeout=timeout)
        self.input_text(locator=ModalLocators.INPUT_CREATE_FOLDER, text=name_folder, timeout=timeout)

    @allure.step("Нажать на кнопку 'Сохранить' в модальном окне")
    def click_button_save(self, timeout: int = 5) -> None:
        self.click(locator=ModalLocators.BUTTON_SAVE, timeout=timeout)


class Toasts(BasePage):
    @allure.step('Проверить, что появился тост с оповещением об окончании копирования')
    def assert_open_toast_copy(self, name_file: str, name_folder: str, timeout: int = 30) -> None:
        self.assert_text_in_element_equal_to(
            locator=ToastsLocators.TOAST,
            text=ToastsText.TOAST_COPY.replace('name_file-&', name_file).replace('name_folder-&', name_folder),
            timeout=timeout,
        )

    @allure.step('Проверить, что появился тост с оповещением об удалении')
    def assert_open_toast_delete(self, timeout: int = 30) -> None:
        self.assert_text_in_element(locator=ToastsLocators.TOAST, text='Очистить Корзину', timeout=timeout)

    @allure.step('Нажать на тост')
    def click_toast(self, timeout: int = 5) -> None:
        self.click(locator=ToastsLocators.TOAST, timeout=timeout)

    @allure.step('Проверить, что тост закрылся')
    def assert_toast_closed(self, timeout: int = 5) -> None:
        self.assert_element_closed(locator=ToastsLocators.TOAST, timeout=timeout)

    @allure.step('Проверить, что появилось оповещение об окончании загрузки файла')
    def assert_open_uploader(self, timeout: int = 30) -> None:
        self.assert_text_in_element_equal_to(
            locator=ToastsLocators.UPLOADER_TITLE, text=ToastsText.UPLOADER_TITLE, timeout=timeout
        )

    @allure.step('Закрыть оповещение об окончании загрузки файла')
    def click_close_uploader(self, timeout: int = 5) -> None:
        self.click(locator=ToastsLocators.UPLOADER_CLOSE, timeout=timeout)

    @allure.step('Проверить, что оповещение об окончании загрузки файла закрылось')
    def assert_uploader_closed(self, timeout: int = 5) -> None:
        self.assert_element_closed(locator=ToastsLocators.UPLOADER_TITLE, timeout=timeout)


class DiskLeftPanel(BasePage):
    @allure.step("Перейти во вкладку 'Файлы' в левом меню")
    def goto_files(self, timeout: int = 5) -> None:
        self.click(locator=DiskLeftPanelLocators.FILES, timeout=timeout)

    @allure.step("Нажать 'Создать' -> 'Папку' в левом меню")
    def click_create_folder(self, timeout: int = 5) -> None:
        self.click(locator=DiskLeftPanelLocators.BUTTON_CREATE, timeout=timeout)
        self.click(locator=DiskLeftPanelLocators.BUTTON_CREATE_FOLDER, timeout=timeout)

    @allure.step('Загрузить файл {path_to_file} в Яндекс Диск')
    def upload_file_to_disk(self, path_to_file: Path, timeout: int = 5) -> None:
        self.upload_file_to_server(
            locator=DiskLeftPanelLocators.INPUT_UPLOAD_FILE, path_to_file=path_to_file, timeout=timeout
        )


class FileViewer(BasePage):
    @allure.step('Сравнить текст из файла с текстом на странице')
    def assert_text_coincide(self, path_to_file: Path, timeout: int = 5) -> None:
        with open(str(Path(Path.cwd(), path_to_file)), encoding='utf-8') as file:
            text = file.read()
        self.assert_text_in_element_equal_to(locator=FileViewerLocators.PAGE_1, text=text, timeout=timeout)
