from  Base import InitiateDriver
from Pages import LoginPage



def test_valid_login():
    driver = InitiateDriver.start_browser()
    login =LoginPage.LoginClass(driver)
    login.login_link()
    login.enter_username('test')
    login.enter_password('test')
    login.click_login_button()
    InitiateDriver.close_browser()
