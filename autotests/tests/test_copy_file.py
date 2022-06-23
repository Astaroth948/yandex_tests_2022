import allure
import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from autotests.pages.disk_page.disk_page import ActionBar, DiskPage, Modal, Toasts
from autotests.pages.disk_page.disk_page_locators import ModalText
from autotests.pages.main_page.main_page import MainPage

FILE: str = 'Файл для копирования'
FOLDER: str = 'Test'


@allure.parent_suite('Проверки Яндекс Диска')
@allure.epic('Проверки Яндекс Диска')
@allure.title('Проверка копирования файла в папку')
@pytest.mark.usefixtures('authorization')
def test_copy_file(driver: WebDriver) -> None:
    main_page = MainPage(driver)
    disk_page = DiskPage(driver)
    action_bar = ActionBar(driver)
    modal = Modal(driver)
    toasts = Toasts(driver)

    main_page.goto_disk_page()
    main_page.switch_to_new_tab()
    disk_page.assert_open_disk_page()

    disk_page.click_file(name_file=FILE)
    action_bar.click_button_copy()
    modal.assert_open_modal(title=ModalText.TITLE_COPY.replace('name_file-&', FILE))
    modal.click_folder(name_folder=FOLDER)
    modal.click_button_copy()
    modal.assert_modal_closed()

    toasts.assert_open_toast_copy(name_file=FILE, name_folder=FOLDER)
    toasts.click_toast()
    toasts.assert_toast_closed()

    disk_page.goto_folder(name_folder=FOLDER)
    disk_page.assert_open_folder(name_folder=FOLDER)
    disk_page.assert_file(name_file=FILE)

    if disk_page.get_len_unnecessary_files(name_file=FILE) != 0:
        disk_page.select_unnecessary_files(name_file=FILE)
        action_bar.click_button_delete()
        toasts.assert_open_toast_delete()
        toasts.click_toast()
        toasts.assert_toast_closed()
        disk_page.assert_unnecessary_files_deleted(name_file=FILE)

    disk_page.click_file(name_file=FILE)
    action_bar.click_button_delete()
    toasts.assert_open_toast_delete()
    toasts.click_toast()
    toasts.assert_toast_closed()
    disk_page.assert_desired_file_deleted(name_file=FILE)
    disk_page.close_current_tab()
