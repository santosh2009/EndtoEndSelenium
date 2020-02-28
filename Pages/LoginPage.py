from Library import ConfigReader


class LoginClass:

    def __init__(self, obj):

        global driver
        driver = obj


    def login_link(self):

        try:
            driver.find_element_by_xpath(ConfigReader.fetch_element_locator('LoginPage', 'login_link_xpath')).click()
        except:
            print("Element not found")


    def enter_username(self, username):

        driver.find_element_by_name(ConfigReader.fetch_element_locator('LoginPage','user_name')).send_keys(username)


    def enter_password(self,password):

        driver.find_element_by_name(ConfigReader.fetch_element_locator('LoginPage', 'password')).send_keys(password)

    def click_login_button(self):

        driver.find_element_by_xpath(ConfigReader.fetch_element_locator('LoginPage', 'login_button_xpath')).click()









