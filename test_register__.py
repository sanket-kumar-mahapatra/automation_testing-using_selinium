import pytest


from selenium.webdriver.common.by import By
from datetime import datetime


# Function to generate unique email addresses
def generate_unique_email():
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    return "testuser" + timestamp + "@example.com"


@pytest.mark.usefixtures("setup_and_teardown")
class TestRegister():
    def generate_unique_email(self):
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        return "testuser" + timestamp + "@example.com"


    def test_registration(self):
        self.driver.find_element(By.CLASS_NAME, "caret").click()

        register = self.driver.find_element(By.XPATH, "//a[text()='Register']")
        register.click()

        # Fill in the registration form with unique email
        first_name = self.driver.find_element(By.ID, 'input-firstname')
        first_name.send_keys('Mohit')

        last_name = self.driver.find_element(By.ID, 'input-lastname')
        last_name.send_keys('kumar')

        email = self.driver.find_element(By.ID, 'input-email')
        unique_email = self.generate_unique_email()
        email.send_keys(unique_email)

        telephone = self.driver.find_element(By.ID, 'input-telephone')
        telephone.send_keys('1234567890')

        password = self.driver.find_element(By.ID, 'input-password')
        password.send_keys('securepassword')

        confirm_password = self.driver.find_element(By.ID, 'input-confirm')
        confirm_password.send_keys('securepassword')

        # Agree to the privacy policy
        privacy_policy = self.driver.find_element(By.XPATH, "//input[@name='agree']")
        privacy_policy.click()

        # Submit the registration form
        continue_button = self.driver.find_element(By.XPATH, "//input[@value='Continue']")
        continue_button.click()

    def test_regester_with_already_registered_data(self):
        self.driver.find_element(By.CLASS_NAME, "caret").click()

        register = self.driver.find_element(By.XPATH, "//a[text()='Register']")
        register.click()

        # Fill in the registration form with unique email
        first_name = self.driver.find_element(By.ID, 'input-firstname')
        first_name.send_keys('Rohan')

        last_name = self.driver.find_element(By.ID, 'input-lastname')
        last_name.send_keys('kumar')

        self.driver.find_element(By.ID, 'input-email').send_keys("rohan@123.com")

        self.driver.find_element(By.ID, 'input-telephone').send_keys('123456789')

        self.driver.find_element(By.ID, 'input-password').send_keys('Rohan@123')

        self.driver.find_element(By.ID, 'input-confirm').send_keys('Rohan@123')

        # Agree to the privacy policy
        privacy_policy = self.driver.find_element(By.XPATH, "//input[@name='agree']")
        privacy_policy.click()

        # Submit the registration form
        continue_button = self.driver.find_element(By.XPATH, "//input[@value='Continue']")
        continue_button.click()

        expected_output = "Warning: E-Mail Address is already registered!"
        assert self.driver.find_element(By.XPATH, "//div[@class='alert alert-danger alert-dismissible']").text.__contains__(
            expected_output)


