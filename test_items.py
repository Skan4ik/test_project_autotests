import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_find_add_card_button(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30)
    try:
        button = browser.find_element(By.CSS_SELECTOR, "#add_to_basket_form > button")
        button.click()
        present_elem = True
        browser.quit()
    except:
        present_elem = False
    assert present_elem, "No add_card button on page"


