from Base import InitiateDriver
from Pages import RegistrationPage
import  pytest
from DataGenerator import DataGen


@pytest.mark.parametrize('data', DataGen.data_generator())
def test_valid_registration(data):
    driver =InitiateDriver.start_browser()
    register = RegistrationPage.RegistrationClass(driver)
    register.enter_username(data[0])
    register.enter_password(data[1])
    register.enter_email(data[2])
    InitiateDriver.close_browser()