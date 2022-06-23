from pathlib import Path
from typing import List

import allure
import pytest
from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from autotests.tools import new_expected_conditions as NEC


# pylint: disable=too-many-public-methods
class BasePage:
    def __init__(self, driver: WebDriver) -> None:
        self._driver = driver

    @allure.step("Открыть страницу '{url}'")
    def open(self, url: str) -> None:
        self._driver.get(url)

    @allure.step("Найти элемент '{locator}'")
    def find_element(self, locator: tuple, timeout: int = 5) -> WebElement:
        return WebDriverWait(self._driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step("Найти элементы '{locator}'")
    def find_elements(self, locator: tuple) -> List[WebElement]:
        return self._driver.find_elements(*locator)

    @allure.step("Проверить, есть элемент '{locator}' на странице")
    def is_element_present(self, locator: tuple, timeout: int = 5) -> bool:
        try:
            WebDriverWait(self._driver, timeout).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            return False
        return True

    @allure.step("Проверить, что элемента '{locator}' нет или он закрылся")
    def assert_element_closed(self, locator: tuple, timeout: int = 5) -> None:
        WebDriverWait(self._driver, timeout).until(EC.invisibility_of_element_located(locator))

    @allure.step("Нажать на элемент '{locator}'")
    def click(self, locator: tuple, timeout: int = 5) -> None:
        try:
            self.find_element(locator=locator, timeout=timeout).click()
        except ElementClickInterceptedException:
            pytest.fail(f"Элемент '{locator}' перекрыт")

    @allure.step("Дважды нажать на элемент '{locator}'")
    def double_click(self, locator: tuple, timeout: int = 5) -> None:
        ActionChains(self._driver).double_click(
            on_element=self.find_element(locator=locator, timeout=timeout)
        ).perform()

    @allure.step("Выделить элементы '{locator}' с нажатым левым CTRL")
    def select_files(self, locator: tuple) -> None:
        action = ActionChains(self._driver)
        action.key_down(Keys.LEFT_CONTROL)
        for element in self.find_elements(locator=locator):
            action.click(on_element=element)
        action.key_up(Keys.LEFT_CONTROL).perform()

    @allure.step("Проверить, что текст элемента '{locator}' равен тексту {text}")
    def assert_text_in_element_equal_to(self, locator: tuple, text: str, timeout: int = 5) -> None:
        WebDriverWait(self._driver, timeout).until(NEC.text_in_element_equal_to(locator, text))

    @allure.step("Проверить, что элемент '{locator}' содержит текст {text}")
    def assert_text_in_element(self, locator: tuple, text: str, timeout: int = 5) -> None:
        WebDriverWait(self._driver, timeout).until(EC.text_to_be_present_in_element(locator, text))

    @allure.step("Очистить текстовое поле '{locator}'")
    def clear_input(self, locator: tuple, timeout: int = 5) -> None:
        element = self.find_element(locator=locator, timeout=timeout)
        element.send_keys(Keys.CONTROL + 'a')
        element.send_keys(Keys.DELETE)

    @allure.step("Ввести текст '{text}' в элемент '{locator}'")
    def input_text(self, locator: tuple, text: str, timeout: int = 5) -> None:
        self.find_element(locator=locator, timeout=timeout).send_keys(text)

    @allure.step("Получить значение атрибута '{attribute}' у элемента '{locator}'")
    def get_attribute(self, locator: tuple, attribute: str, timeout: int = 5) -> str:
        attribute_value = self.find_element(locator=locator, timeout=timeout).get_attribute(attribute)
        if attribute_value is None:
            pytest.fail(f"Значение атрибута '{attribute}' не найдено у элемента '{locator}'")
        return attribute_value

    @allure.step("Проверить, что кол-во элементов '{locator}' равно {quantity}")
    def assert_quantity_of_elements(self, locator: tuple, quantity: int, timeout: int = 5) -> None:
        WebDriverWait(self._driver, timeout).until(NEC.quantity_of_elements(locator, quantity))

    @allure.step('Переключиться на последнюю вкладку')
    def switch_to_new_tab(self) -> None:
        self._driver.switch_to.window(self._driver.window_handles[-1])

    @allure.step('Загрузить файл')
    def upload_file_to_server(self, locator: tuple, path_to_file: Path, timeout: int = 5) -> None:
        element = WebDriverWait(self._driver, timeout).until(EC.presence_of_element_located(locator))
        element.send_keys(str(Path(Path.cwd(), path_to_file)))

    @allure.step('Закрыть текщую вкладку')
    def close_current_tab(self) -> None:
        self._driver.close()
        self.switch_to_new_tab()
