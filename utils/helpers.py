from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
from config.config import WAIT_TIME

def wait_and_click(driver, selector, timeout=10):
    """Wait for element to be clickable and click it"""
    element = WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
    )
    time.sleep(WAIT_TIME)
    element.click()
    return element

def wait_and_send_keys(driver, selector, keys, timeout=10):
    """Wait for element to be present and send keys"""
    element = WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, selector))
    )
    element.clear()
    time.sleep(WAIT_TIME)
    element.send_keys(keys)
    return element

def wait_for_element(driver, selector, timeout=10):
    """Wait for element to be present"""
    return WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, selector))
    )

def click_radio_button(driver, selector):
    """Click a radio button using ActionChains"""
    radio = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, selector))
    )
    ActionChains(driver).move_to_element(radio).click().perform()
    time.sleep(WAIT_TIME)
    return radio

def upload_image(driver, image_path, uploader_selector):
    """Upload an image and verify the upload"""
    uploader = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, uploader_selector))
    )
    uploader.send_keys(image_path)
    time.sleep(WAIT_TIME * 2)  # Wait longer for upload
    return uploader 