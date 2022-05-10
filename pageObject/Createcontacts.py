from selenium.webdriver.common.by import By


class Createcontacts:

    def __init__(self,driver):
        self.driver=driver


    create_icon=(By.ID,'com.google.android.contacts:id/floating_action_button')
    select_account=(By.ID,'android:id/text1')
    input_name=(By.CLASS_NAME,'android.widget.EditText')
    input_number=(By.XPATH,"//android.widget.EditText[@text='Phone']")
    save=(By.ID,"com.google.android.contacts:id/toolbar_button")

    def tap_create(self):
        return self.driver.find_element(*Createcontacts.create_icon)

    def choose_account(self):
        return self.driver.find_element(*Createcontacts.select_account)

    def enter_name(self):
        return self.driver.find_element(*Createcontacts.input_name)

    def enter_number(self):
        return self.driver.find_element(*Createcontacts.input_number)

    def save_contact(self):
        return self.driver.find_element(*Createcontacts.save)