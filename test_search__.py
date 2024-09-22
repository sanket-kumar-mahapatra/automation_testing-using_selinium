import pytest


from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_and_teardown")
class Test_Search():
    def test_search_for_valid_product(self):
        self.driver.find_element(By.NAME, "search").send_keys("iphone")
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']").click()
        assert self.driver.find_element(By.LINK_TEXT, "iPhone").is_displayed()

    def test_search_for_invalid_product(self):
        self.driver.find_element(By.NAME, "search").send_keys("laptop")
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']").click()
        expected_output = "There is no product that matches the search criteria."
        actual_output = self.driver.find_element(By.XPATH, "//p[contains(text(),'There is no product that matches the search criter')]").text
        assert actual_output == expected_output

    def test_search_without_providing_any_product(self):
        self.driver.find_element(By.NAME, "search").send_keys("")
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']").click()
        expected_output = "There is no product that matches the search criteria."
        actual_output = self.driver.find_element(By.XPATH, "//p[contains(text(),'There is no product that matches the search criter')]").text
        assert actual_output == expected_output

