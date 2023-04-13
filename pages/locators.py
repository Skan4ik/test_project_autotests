from selenium.webdriver.common.by import By

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form > button")
    REGISTR_FORM = (By.CSS_SELECTOR, "#register_form > button")