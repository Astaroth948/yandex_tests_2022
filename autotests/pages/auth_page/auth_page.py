import allure

from autotests.pages.auth_page.auth_page_locators import AuthPageLocators
from autotests.pages.base_page import BasePage


class AuthPage(BasePage):
    @allure.step("Нажать на кнопку 'Войти'")
    def click_button_enter(self, timeout: int = 5) -> None:
        self.click(locator=AuthPageLocators.BUTTON_ENTER, timeout=timeout)

    @allure.step("Нажать на кнопку 'Не сейчас'")
    def click_button_skip(self, timeout: int = 5) -> None:
        self.click(locator=AuthPageLocators.BUTTON_SKIP, timeout=timeout)

    @allure.step("Проверить, что заголовок содержит текст '{text}'")
    def assert_text_in_header(self, text: str, timeout: int = 5) -> None:
        self.assert_text_in_element_equal_to(locator=AuthPageLocators.TITLE, text=text, timeout=timeout)

    @allure.step("Проверить, что в качестве текщего пользователя выбран '{login}'")
    def assert_current_user_selected(self, login: str, timeout: int = 5) -> None:
        self.assert_text_in_element_equal_to(
            locator=AuthPageLocators.SELECT_CURRENT_ACCOUNT, text=login, timeout=timeout
        )

    @allure.step("Ввести '{login}' в поле ввода логина")
    def input_login(self, login: str, timeout: int = 5) -> None:
        self.input_text(locator=AuthPageLocators.INPUT_LOGIN, text=login, timeout=timeout)

    @allure.step("Ввести '{password}' в поле ввода пароля")
    def input_password(self, password: str, timeout: int = 5) -> None:
        self.input_text(locator=AuthPageLocators.INPUT_PASSWORD, text=password, timeout=timeout)

    @allure.step('Переключить способ авторизации на ввод логина')
    def switch_input_login(self, timeout: int = 5) -> None:
        if 'button:clear' in self.get_attribute(locator=AuthPageLocators.TAB_MAIL, attribute='data-t', timeout=timeout):
            self.click(locator=AuthPageLocators.TAB_MAIL, timeout=timeout)
