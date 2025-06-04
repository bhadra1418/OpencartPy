from datetime import datetime
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import platform
import os


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")

@pytest.fixture()
def setup(request):
    browser = request.config.getoption("browser")

    if browser.lower() == "chrome":
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

    elif browser.lower() == "firefox":
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)

    else:
        raise ValueError(f"Browser '{browser}' is not supported. Use 'chrome' or 'firefox'.")

    driver.maximize_window()
    driver.implicitly_wait(10)
    return driver


# Add custom metadata to HTML report
def pytest_configure(config):
    config.clear()  # Clears default metadata
    config["Project Name"] = "OpenCart Automation"
    config["Module"] = "Account Registration"
    config["Tester"] = "veerabhadra"
    config["Platform"] = platform.system()
    config["Platform-Version"] = platform.version()
    config["Python Version"] = platform.python_version()
    config["Browser"] = "Chrome / Firefox (CLI selected)"
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.htmlpath = os.path.abspath(os.curdir)+"\\reports\\"+datetime.now().strftime("%Y%m%d-%H%M%S")+".html"