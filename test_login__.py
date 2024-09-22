import pytest

from selenium.webdriver.common.by import By




@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin:
    def test_login_with_valid_credential(self):
        self.driver.find_element(By.CLASS_NAME, "caret").click()
        self.driver.find_element(By.LINK_TEXT, "Login").click()
        self.driver.find_element(By.ID, "input-email").send_keys("kumarsanket32001@gmail.com")
        self.driver.find_element(By.ID, "input-password").send_keys("sanketlalu32004")
        self.driver.find_element(By.XPATH, "//input[@value='Login']").click()

        expected_text = "My Account"
        actual_text = self.driver.find_element(By.XPATH, "//h2[normalize-space()='My Account']").text
        assert actual_text == expected_text

    def test_login_without_details(self):
        self.driver.find_element(By.CLASS_NAME, "caret").click()
        self.driver.find_element(By.LINK_TEXT, "Login").click()
        self.driver.find_element(By.ID, "input-email").send_keys("")
        self.driver.find_element(By.ID, "input-password").send_keys("")
        self.driver.find_element(By.XPATH, "//input[@value='Login']").click()

        expected_text = "Warning: No match for E-Mail Address and/or Password."
        alert_text = self.driver.find_element(By.XPATH, "//div[@class='alert alert-danger alert-dismissible']").text
        assert expected_text in alert_text
