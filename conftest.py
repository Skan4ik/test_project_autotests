import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options
from selenium.webdriver.firefox.options import Options as firefox_options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='ru', help='Choose language')
    parser.addoption('--browser_name', action='store', default='chrome', help='Choose browser: chrome or firefox')


@pytest.fixture
def language(request):
    return request.config.getoption('--language')


@pytest.fixture
def browser_name(request):
    return request.config.getoption('--browser_name')


@pytest.fixture(scope='function', autouse=False)
def browser(language, browser_name):
    browser = None
    if browser_name.lower() == 'chrome':
        options = chrome_options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
    if browser_name.lower() == 'firefox':
        options = firefox_options()
        options.set_preference("intl.accept_languages", language)
        browser = webdriver.Firefox(options=options)
    yield browser
    browser.quit()

    



