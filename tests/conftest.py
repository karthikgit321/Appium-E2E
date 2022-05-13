import pytest
import openpyxl
from appium import webdriver
Dict={}
book =openpyxl.load_workbook("C:\\Users\\karthiks\\Desktop\\package_name.xlsx")
sheet=book.active
Dict[sheet.cell(row=1,column=2).value]=sheet.cell(row=2,column=2).value
Dict[sheet.cell(row=1,column=3).value]=sheet.cell(row=2,column=3).value

@pytest.fixture()
def setup(request):
    desired_caps = {
        "appPackage": 'Dict[0]',
        "appActivity": 'Dict[1]',
        "automationName": "uiautomator2",
        "platformName": "Android",
        "deviceName": "POCO F1",
        "ignoreHiddenApiPolicyError":True,
        'autoGrantPermissions':True
    }
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    request.cls.driver=driver
    yield
    driver.close_app()