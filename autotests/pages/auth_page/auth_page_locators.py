from dataclasses import dataclass

from selenium.webdriver.common.by import By


@dataclass
class AuthPageLocators:
    TITLE: tuple = (By.XPATH, '//h1[@data-t="title"]')
    TAB_MAIL: tuple = (By.XPATH, '//button[@data-type="login"]')
    TAB_PHONE: tuple = (By.XPATH, '//button[@data-type="phone"]')
    INPUT_LOGIN: tuple = (By.XPATH, '//input[@data-t="field:input-login"]')
    INPUT_PASSWORD: tuple = (By.XPATH, '//input[@data-t="field:input-passwd"]')
    BUTTON_ENTER: tuple = (By.XPATH, '//button[@type="submit"]')
    BUTTON_SKIP: tuple = (By.XPATH, '//button[@data-t="button:pseudo"]')
    SELECT_CURRENT_ACCOUNT: tuple = (By.XPATH, '//a[@class="CurrentAccount"]')


@dataclass
class AuthPageText:
    TITLE_LOGIN: str = 'Войдите с Яндекс ID'
    TITLE_PASSWORD: str = 'Войдите, чтобы продолжить'
