import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from Test.test_base import BaseTest
from Config.config import TestData


@pytest.fixture(params=["chrome"], scope='class')
def init_driver(request):
    if request.param == "chrome":
        service = Service(executable_path=TestData.CHROME_EXECUTEABLE_PATH)
        # Or dynamically: service = Service(ChromeDriverManager().install())
        web_driver = webdriver.Chrome(service=service)
    else:
        raise ValueError(f"Unsupported browser: {request.param}")

    web_driver.implicitly_wait(10)
    request.cls.driver = web_driver
    # yield web_driver
    # web_driver.quit()