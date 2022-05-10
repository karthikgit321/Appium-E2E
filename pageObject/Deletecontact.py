from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy


class Deletecontact:
    def __init__(self,driver):
        self.driver=driver

    search=(By.ID,'com.google.android.contacts:id/open_search_bar_text_view')

    search_input=(By.ID,'com.google.android.contacts:id/open_search_view_edit_text')
    pick_contact=(MobileBy.ACCESSIBILITY_ID,'karthik')
    more_options=(MobileBy.ACCESSIBILITY_ID,'More options')
    bin=(By.XPATH,"//android.widget.TextView[@text='Delete']")
    move_to_bin=(By.ID,'android:id/button1')

    def search_box(self):
        return self.driver.find_element(*Deletecontact.search)

    def search_enter(self):
        return self.driver.find_element(*Deletecontact.search_input)

    def pick_choose(self):
        return self.driver.find_element(*Deletecontact.pick_contact)

    def more_settings(self):
        return self.driver.find_element(*Deletecontact.more_options)

    def delete(self):
        return self.driver.find_element(*Deletecontact.bin)

    def confirm_delete(self):
        return self.driver.find_element(*Deletecontact.move_to_bin)
