from dataclasses import dataclass

from selenium.webdriver.common.by import By


@dataclass
class MainPageLocators:
    BUTTON_AUTH: tuple = (By.XPATH, '//a[@data-statlog="notifications.mail.logout.enter"]')
    BUTTON_MAIL: tuple = (By.XPATH, '//a[text()="Почта"]')
    BUTTON_DISK: tuple = (By.XPATH, '//a[text()="Диск"]')
    FLAG_MAIN_PAGE: tuple = (By.XPATH, '//div[@class="home-logo home-arrow__logo"]')
    USER_PROFILE: tuple = (By.XPATH, '//a[@data-statlog="notifications.mail.login.usermenu.toggle"]')
    BUTTON_EXIT: tuple = (By.XPATH, '//a[@aria-label="Выйти"]')
