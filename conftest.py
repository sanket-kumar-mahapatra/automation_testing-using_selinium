import pytest
from selenium import webdriver




@pytest.fixture()
def setup_and_teardown(request):
    driver=webdriver.Chrome()
    driver.get("https://tutorialsninja.com/demo/")
    request.cls.driver=driver
    yield

    driver.quit()
