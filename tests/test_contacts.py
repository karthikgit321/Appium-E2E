import pytest
from appium import webdriver
import time
from appium.webdriver.common.touch_action import TouchAction

from pageObject.Createcontacts import Createcontacts
from pageObject.Deletecontact import Deletecontact
from utilities.Baseclass import Baseclass

'''
desired_caps = {
  "appPackage": "com.google.android.contacts",
  "appActivity": "com.android.contacts.activities.PeopleActivity",
  "automationName": "uiautomator2",
  "platformName": "Android"
}
driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
time.sleep(2)
'''

class Testcontacts(Baseclass):
    #to create the contact
    def test_createcontact(self):

        create_contact=Createcontacts(self.driver)
        delete_contact=Deletecontact(self.driver)
        log=self.get_Logger()

        #time.sleep(2)
        #self.driver.find_element_by_id('android:id/button2').click()
        time.sleep(2)
        #self.scroll(x1=728, y1=1272, x2=746, y2=565)
        #time.sleep(2)
        create_contact.tap_create().click()
        #self.driver.find_element_by_id('com.google.android.contacts:id/floating_action_button').click()
        time.sleep(3)
        #self.driver.find_element_by_id('android:id/text1').click()
        #create_contact.choose_account().click()
        #time.sleep(3)
        #self.driver.find_element_by_class_name("android.widget.EditText").send_keys("karthik")
        create_contact.enter_name().send_keys("karthik")
        time.sleep(3)
        #self.driver.find_element_by_xpath("//android.widget.EditText[@text='Phone']").send_keys("123456")

        create_contact.enter_number().send_keys("123456")
        time.sleep(2)
        #self.driver.find_element_by_id("com.google.android.contacts:id/toolbar_button").click()
        create_contact.save_contact().click()
        log.info("the contact karthik is created")
        self.driver.close_app()

        #to delete the contact
        self.driver.start_activity('com.google.android.contacts','com.android.contacts.activities.PeopleActivity')
        time.sleep(5)
        #self.driver.find_element_by_id("com.google.android.contacts:id/open_search_bar_text_view").click()
        #user_actions=TouchAction(self.driver)
        #self.scroll(x1=575,y1=1827,x2=540,y2=540)
        #time.sleep(3)
        #user_actions.press(x=23,y=1833).move_to(x=23,y=1387).release().perform()
        #time.sleep(3)
        delete_contact.search_box().click()
        time.sleep(2)
        #self.driver.find_element_by_id("com.google.android.contacts:id/open_search_view_edit_text").send_keys("karthik")
        delete_contact.search_enter().send_keys("karthik")
        time.sleep(3)
        self.driver.back()
        #self.driver.find_element_by_accessibility_id("karthik").click()
        delete_contact.pick_choose().click()
        time.sleep(2)
        #self.driver.find_element_by_accessibility_id("More options").click()
        delete_contact.more_settings().click()
        time.sleep(2)
        #self.driver.find_element_by_xpath("//android.widget.TextView[@text='Delete']").click()
        delete_contact.delete().click()
        time.sleep(2)
        #self.driver.find_element_by_id("android:id/button1").click()
        delete_contact.confirm_delete().click()
        log.info("contact karthik is deleted")

