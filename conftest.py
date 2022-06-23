from typing import Any
import pytest
import allure
from _pytest.config.argparsing import Parser
from _pytest.fixtures import FixtureRequest
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver import ChromeOptions
from selenium import webdriver
from autotests.pages.auth_page.auth_page import AuthPage
from autotests.pages.auth_page.auth_page_locators import AuthPageText
from autotests.pages.main_page.main_page import MainPage
from autotests.types import AuthData
from _pytest.nodes import Item


def pytest_addoption(parser: Parser) -> None:
    parser.addoption('--url', action='store', default='https://yandex.ru/', help='URL адрес тестируемой страницы')
    parser.addoption('--login', action='store', default=None, help='Логин')
    parser.addoption('--password', action='store', default=None, help='Пароль')
    parser.addoption('--headless', action='store_true', default=False, help='Флаг включает Headless режим браузера')


@pytest.fixture(scope='module')
def auth_data(request: FixtureRequest) -> AuthData:
    url = request.config.getoption('--url')
    login = request.config.getoption('--login')
    password = request.config.getoption('--password')
    return AuthData(url=url, login=login, password=password)

@pytest.fixture(scope='module')
def driver(request: FixtureRequest) -> WebDriver:
    headless = request.config.getoption('--headless')

    options = ChromeOptions()

    options.add_argument('--no-sandbox')
    options.add_argument('--ignore-certificate-errors')
    options.headless = headless
    if headless:
        options.add_argument('window-size=1920,1080')
    else:
        options.add_argument('--start-maximized')

    web_driver = webdriver.Chrome(options=options)
    yield web_driver
    web_driver.quit()


@pytest.fixture(scope='module')
def authorization(driver: WebDriver, auth_data: AuthData) -> None:
    main_page = MainPage(driver)
    auth_page = AuthPage(driver)

    main_page.open(url=auth_data.url)
    main_page.assert_open_main_page()
    main_page.goto_auth_page()

    auth_page.assert_text_in_header(text=AuthPageText.TITLE_LOGIN)
    auth_page.switch_input_login()
    auth_page.input_login(login=auth_data.login)
    auth_page.click_button_enter()

    auth_page.assert_text_in_header(text=AuthPageText.TITLE_PASSWORD)
    auth_page.assert_current_user_selected(login=auth_data.login)
    auth_page.input_password(password=auth_data.password)
    auth_page.click_button_enter()
    main_page.assert_open_main_page()

    yield
    main_page.click_user_profile()
    main_page.click_logout()
    main_page.assert_logout()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item: Item, call: Any):
    outcome = yield
    result = outcome.get_result()
    if result.when == 'call' and result.failed:
        try:
            driver = item.funcargs['driver']
            allure.attach(body=driver.get_screenshot_as_png(), name='screenshot', attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            print(f'Fail to take screenshot: {e}')

