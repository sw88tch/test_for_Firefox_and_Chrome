import pytest
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

binary = FirefoxBinary(r'C:\Program Files\Mozilla Firefox\firefox.exe')

supported_browsers = {
    'chrome': webdriver.Chrome,
    'firefox': webdriver.Firefox(firefox_binary=binary)
}

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")

    if browser_name  == "chrome":
        print(f"\nstart {browser_name} browser for test..")
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        binary = FirefoxBinary(r'C:\Program Files\Mozilla Firefox\firefox.exe')
        browser = webdriver.Firefox(firefox_binary=binary)
    else:
        joined_browsers = ', '.join(supported_browsers.keys())
        raise pytest.UsageError(f"--browser_name is invalid, supported browsers: {joined_browsers}")

    yield browser
    print("\nquit browser..")
    browser.quit()