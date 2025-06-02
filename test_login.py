import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
import time

@pytest.fixture
def driver():
    options = Options()
    # options.add_argument("--headless")  # Uncomment if you want to run headless
    service = ChromeService()  # Make sure chromedriver is in your PATH
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()

def test_login_success(driver):
    driver.get("https://the-internet.herokuapp.com/login")

    username_input = driver.find_element(By.ID, "username")
    username_input.send_keys("tomsmith")

    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys("SuperSecretPassword!")

    login_button = driver.find_element(By.CSS_SELECTOR, "button.radius")
    login_button.click()

    time.sleep(2)  # Better to use WebDriverWait, but for simplicity we keep sleep here

    success_message = driver.find_element(By.ID, "flash")
    assert "You logged into a secure area!" in success_message.text
