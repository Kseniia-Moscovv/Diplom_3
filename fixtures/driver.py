from selenium import webdriver
import pytest
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.service import Service as ChromeService

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from constants.url_constants import UrlConstants


@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    if request.param == 'chrome':
        options = ChromeOptions()
        options.add_argument('--window-size=1400,1800')
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(options=options, service=service)
    elif request.param == 'firefox':
        options = FirefoxOptions()
        options.add_argument('--width=1400')
        options.add_argument('--height=1800')
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(options=options, service=service)

    driver.get(UrlConstants.BASE_URL)
    yield driver
    driver.quit()


