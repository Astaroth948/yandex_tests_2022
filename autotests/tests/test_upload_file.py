import allure
import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from autotests.pages.disk_page.disk_page import ActionBar, DiskLeftPanel, DiskPage, FileViewer, Modal, Toasts
from autotests.pages.disk_page.disk_page_locators import PATH_TO_FILE, ModalText
from autotests.pages.main_page.main_page import MainPage

FILE: str = 'file.txt'
FOLDER: str = 'TestFolder'


@allure.parent_suite('Проверки Яндекс Диска')
@allure.epic('Проверки Яндекс Диска')
@allure.title('Проверка загрузки файла в Яндекс Диск')
@pytest.mark.usefixtures('authorization')
def test_copy_file(driver: WebDriver) -> None:
    main_page = MainPage(driver)
    disk_page = DiskPage(driver)
    action_bar = ActionBar(driver)
    modal = Modal(driver)
    toasts = Toasts(driver)
    disk_left_panel = DiskLeftPanel(driver)
    file_viewer = FileViewer(driver)

    main_page.goto_disk_page()
    main_page.switch_to_new_tab()
    disk_page.assert_open_disk_page()

    disk_left_panel.click_create_folder()
    modal.assert_open_modal(title=ModalText.TITLE_CREATE_FOLDER)
    modal.input_name_folder(name_folder=FOLDER)
    modal.click_button_save()
    modal.assert_modal_closed()

    disk_page.assert_file(name_file=FOLDER)
    disk_page.goto_folder(name_folder=FOLDER)
    disk_page.assert_open_folder(name_folder=FOLDER)

    disk_left_panel.upload_file_to_disk(path_to_file=PATH_TO_FILE)
    toasts.assert_open_uploader()
    toasts.click_close_uploader()
    toasts.assert_uploader_closed()
    disk_page.assert_file(name_file=FILE)

    disk_page.goto_folder(name_folder=FILE)
    disk_page.switch_to_new_tab()
    file_viewer.assert_text_coincide(path_to_file=PATH_TO_FILE)
    disk_page.close_current_tab()

    disk_left_panel.goto_files()
    disk_page.click_file(name_file=FOLDER)
    action_bar.click_button_delete()
    toasts.assert_open_toast_delete()
    toasts.click_toast()
    toasts.assert_toast_closed()
    disk_page.assert_desired_file_deleted(name_file=FOLDER)
    disk_page.close_current_tab()
