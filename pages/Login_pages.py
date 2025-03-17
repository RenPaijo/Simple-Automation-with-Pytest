from selenium.webdriver.common.by import By


class LoginPageLocators:
    USERNAME_FIELD = (By.ID, "userName")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login")
    ERROR_MESSAGE = (By.ID, "name")
    DELETE_BUTTON = (By.XPATH, "//div[@class='text-center button']//button[@id='submit']")


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(*LoginPageLocators.USERNAME_FIELD).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

    def get_error_message(self):
        return self.driver.find_element(*LoginPageLocators.ERROR_MESSAGE).text
    
    def get_delete_button(self):
        return self.driver.find_element(*LoginPageLocators.DELETE_BUTTON).text
