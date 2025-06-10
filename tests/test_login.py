import pytest
from config.config import (
    get_driver,
    LOGIN_URL,
    EMAIL,
    PASSWORD,
    EMAIL_INPUT,
    PASSWORD_INPUT,
    SUBMIT_BUTTON,
    ERROR_MESSAGE,
    DASHBOARD_TITLE,
    WAIT_TIME
)
from utils.helpers import wait_and_send_keys, wait_and_click, wait_for_element
import time

@pytest.fixture
def driver():
    """Fixture to create and close the WebDriver"""
    driver = get_driver()
    yield driver
    time.sleep(WAIT_TIME)  # Wait before closing
    driver.quit()

def test_login_success(driver):
    """Test successful login with valid credentials"""
    # Navigate to login page
    driver.get(LOGIN_URL)
    time.sleep(WAIT_TIME)  # Wait for page load
    
    # Fill in credentials
    wait_and_send_keys(driver, EMAIL_INPUT, EMAIL)
    wait_and_send_keys(driver, PASSWORD_INPUT, PASSWORD)
    
    # Click submit button
    wait_and_click(driver, SUBMIT_BUTTON)
    
    # Verify dashboard title
    dashboard_title = wait_for_element(driver, DASHBOARD_TITLE)
    time.sleep(WAIT_TIME)  # Wait to see the dashboard
    assert dashboard_title.text == "Dashboard"

def test_login_error(driver):
    """Test login with invalid credentials"""
    # Navigate to login page
    driver.get(LOGIN_URL)
    time.sleep(WAIT_TIME)  # Wait for page load
    
    # Fill in invalid credentials
    wait_and_send_keys(driver, EMAIL_INPUT, "invalid@email.com")
    wait_and_send_keys(driver, PASSWORD_INPUT, "wrongpassword")
    
    # Click submit button
    wait_and_click(driver, SUBMIT_BUTTON)
    
    # Verify error message
    error_message = wait_for_element(driver, ERROR_MESSAGE)
    time.sleep(WAIT_TIME)  # Wait to see the error message
    assert error_message.text == "Invalid email or password"
