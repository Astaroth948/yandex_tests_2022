import allure

from autotests.pages.base_page import BasePage
from autotests.pages.main_page.main_page_locators import MainPageLocators


class MainPage(BasePage):
    @allure.step('Проверить, что открылась главная страница Яндекса')
    def assert_open_main_page(self, timeout: int = 20) -> None:
        self.find_element(locator=MainPageLocators.FLAG_MAIN_PAGE, timeout=timeout)

    @allure.step('Перейти на страницу авторизации')
    def goto_auth_page(self, timeout: int = 5) -> None:
        self.click(locator=MainPageLocators.BUTTON_AUTH, timeout=timeout)

    @allure.step('Перейти на страницу Диска')
    def goto_disk_page(self, timeout: int = 5) -> None:
        self.click(locator=MainPageLocators.BUTTON_DISK, timeout=timeout)

    @allure.step('Нажать на профиль пользователя')
    def click_user_profile(self, timeout: int = 5) -> None:
        self.click(locator=MainPageLocators.USER_PROFILE, timeout=timeout)

    @allure.step('Нажать на кнопку "Выйти"')
    def click_logout(self, timeout: int = 5) -> None:
        self.click(locator=MainPageLocators.BUTTON_EXIT, timeout=timeout)

    @allure.step('Проверить, что пользователь не авторизован')
    def assert_logout(self, timeout: int = 5) -> None:
        self.find_element(locator=MainPageLocators.BUTTON_AUTH, timeout=timeout)
