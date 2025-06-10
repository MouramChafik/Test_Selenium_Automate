import pytest
import os
from config.config import (
    get_driver,
    LOGIN_URL,
    EMAIL,
    PASSWORD,
    EMAIL_INPUT,
    PASSWORD_INPUT,
    SUBMIT_BUTTON,
    PRODUCTS_URL,
    ADD_PRODUCT_BUTTON,
    PRODUCT_NAME_INPUT,
    PRODUCT_DESCRIPTION_INPUT,
    PRODUCT_PRICE_INPUT,
    PRODUCT_CATEGORY_SELECT,
    STATUS_ENABLED,
    SAVE_BUTTON,
    PRODUCTS_TITLE,
    WAIT_TIME
)
from utils.helpers import (
    wait_and_send_keys,
    wait_and_click,
    wait_for_element,
    click_radio_button,
    upload_image
)
import time

@pytest.fixture
def driver():
    """Fixture to create and close the WebDriver"""
    driver = get_driver()
    yield driver
    time.sleep(WAIT_TIME)  # Wait before closing
    driver.quit()

def test_add_product(driver):
    """Test adding a new product"""
    # Login first
    driver.get(LOGIN_URL)
    time.sleep(WAIT_TIME)
    
    wait_and_send_keys(driver, EMAIL_INPUT, EMAIL)
    wait_and_send_keys(driver, PASSWORD_INPUT, PASSWORD)
    wait_and_click(driver, SUBMIT_BUTTON)
    
    # Navigate to products page
    driver.get(PRODUCTS_URL)
    time.sleep(WAIT_TIME)
    
    # Click add product button
    wait_and_click(driver, ADD_PRODUCT_BUTTON)
    time.sleep(WAIT_TIME)
    
    # Fill in product details
    wait_and_send_keys(driver, PRODUCT_NAME_INPUT, "Test Product")
    wait_and_send_keys(driver, PRODUCT_DESCRIPTION_INPUT, "This is a test product description")
    wait_and_send_keys(driver, PRODUCT_PRICE_INPUT, "99.99")
    
    # Select category
    category_select = wait_for_element(driver, PRODUCT_CATEGORY_SELECT)
    category_select.click()
    time.sleep(WAIT_TIME)
    category_select.send_keys("Electronics")
    time.sleep(WAIT_TIME)
    category_select.send_keys("\n")
    
    # Set status to enabled
    click_radio_button(driver, STATUS_ENABLED)
    
    # Upload image
    image_path = os.path.abspath("data/test_image.jpg")
    upload_image(driver, image_path, "input[type='file']")
    
    # Save product
    wait_and_click(driver, SAVE_BUTTON)
    time.sleep(WAIT_TIME)
    
    # Verify redirection to products page
    products_title = wait_for_element(driver, PRODUCTS_TITLE)
    assert products_title.text == "Products"
