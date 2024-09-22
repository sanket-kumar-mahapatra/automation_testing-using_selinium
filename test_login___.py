import allure
import pytest
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By




@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin:

    def test_login_with_valid_credential(self):
        self.driver.find_element(By.CLASS_NAME,"caret").click()
        self.driver.find_element(By.LINK_TEXT, "Login").click()
        self.driver.find_element(By.ID, "input-email").send_keys("rohan@123.com")
        self.driver.find_element(By.ID, "input-password").send_keys("Rohan@123")
        self.driver.find_element(By.XPATH, "//input[@value='Login']").click()

        expexted_text="My Account"
        assert self.driver.find_element(By.XPATH,"//h2[normalize-space()='My Account']").text.__eq__(expexted_text)

    def test_login_without_details(self):
        self.driver.find_element(By.CLASS_NAME, "caret").click()
        self.driver.find_element(By.LINK_TEXT, "Login").click()
        self.driver.find_element(By.ID, "input-email").send_keys("")
        self.driver.find_element(By.ID, "input-password").send_keys("")
        self.driver.find_element(By.XPATH, "//input[@value='Login']").click()
        expected_text="Warning: No match for E-Mail Address and/or Password."
        assert self.driver.find_element(By.XPATH,"//div[@class='alert alert-danger alert-dismissible']").text.__contains__(expected_text)
        #adding screenshot to allure report for a test method
        allure.attach(self.driver.get_screenshot_as_png(),name="log in without details",attachment_type=AttachmentType.PNG)









































"""
----------------------------------------------------------------------------------------------------------------------------------
#how to set up and use WebDriver in test classes, and how to write test methods that interact with a
web application using Selenium and pytest.
---------------------------------------------------------------------------------------------------------------------------------

### Summary :

#### **Class Structure**:
- **What is a Class?**
  - A class is a way to group related functions (methods) and variables (attributes). It helps in organizing code better.

#### **Object Variables**:
- **What is `self`?**
  - `self` is a referece variable in Python that  is used to access variables and methods that is present inside the class.

- **Why Use `self.driver`?**
  - `self.driver` is used to access the WebDriver variable from anywhere within the class. This makes it easy to interact
   with the web browser in all our test methods.

#### **Fixture Setup**:
- **What is a Fixture?**
  - A fixture is a special function used by `pytest` to set up conditions before running tests and to clean up afterward.
   It helps keep the tests clean and ensures a fresh start for each test case.

- **Setting Up WebDriver with a Fixture**:
  - In the fixture `setup_and_teardown`, we initialize the WebDriver, open the browser, and navigate to the website.
  - We use `request.cls.driver = driver` to attach the `driver` to the test class , making it accessible as `self.driver`
   in all test methods.

#### **Accessing WebDriver in Test Methods**:
- **How to Use `self.driver` in Test Methods**:
  - In each test method, we use `self.driver` to interact with the web browser.
  - This ensures that all test methods use the same WebDriver variable set up by the fixture.


- **Imports**:
  - We import `pytest` for testing and `webdriver` from Selenium to control the web browser.

- **Fixture Definition**:
  - We define a fixture `setup_and_teardown` that sets up the WebDriver and opens the browser to the specified URL.
  - The `request.cls.driver = driver` line attaches the WebDriver to the test class object.



- **Using the Fixture**:
  - We use `@pytest.mark.usefixtures("setup_and_teardown")` to apply the fixture to the `TestLogin` class, ensuring that setup and teardown are performed for each test method.

- **Test Class and Methods**:
  - `class TestLogin`: Defines the `TestLogin` class that contains our test methods.
  - `self.driver`: Used within test methods to access the WebDriver variable set up by the fixture.

- **Test Methods**:
  - `test_login_with_valid_credential`: Tests logging in with valid credentials. It navigates to the login page, enters the credentials, clicks login, and verifies successful login.
  - `test_login_without_details`: Tests logging in without entering any details. It navigates to the login page, leaves the fields empty, clicks login, and verifies the warning message.

 
"""