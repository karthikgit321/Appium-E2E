'''
from appium import webdriver
import time
desired_caps = {
  "appPackage": "com.miui.calculator",
  "appActivity": "com.miui.calculator.cal.CalculatorActivity",
  "automationName": "uiautomator2",
  "platformName": "Android"
}
driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
#click to agree
driver.find_element_by_id('android:id/button1').click()
time.sleep(3)
driver.find_element_by_id("com.miui.calculator:id/btn_9_s").click()
#driver.find_element_by_id('com.android.permissioncontroller:id/permission_allow_foreground_only_button').click()
#driver.find_element_by_id("android:id/button1").click()
'''