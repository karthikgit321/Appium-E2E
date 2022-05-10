import pytest
from appium import webdriver

@pytest.fixture()
def setup(request):
    desired_caps = {
        "appPackage": "com.google.android.contacts",
        "appActivity": "com.android.contacts.activities.PeopleActivity",
        "automationName": "uiautomator2",
        "platformName": "Android",
        "deviceName": "POCO F1"
    }
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    request.cls.driver=driver
    yield
    driver.close_app()
