import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import (
    get_driver,
    HOME_URL,
    CART_URL,
    FEATURED_PRODUCTS_TITLE,
    PRODUCTS_GRID,
    PRODUCT_LINK,
    ADD_TO_CART_BUTTON,
    MINI_CART_TOAST,
    MINI_CART_TITLE,
    MINI_CART_ITEM_NAME,
    MINI_CART_ITEM_QTY,
    VIEW_CART_BUTTON,
    CONTINUE_SHOPPING_LINK
)

@pytest.fixture
def driver():
    """Create and close WebDriver"""
    driver = get_driver()
    yield driver
    driver.quit()

def test_shopping_journey(driver):
    """Test the shopping journey from home page to cart"""
    # Navigate to home page
    driver.get(HOME_URL)
    print("\nNavigated to home page")

    # Verify Featured Products section
    featured_title = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, FEATURED_PRODUCTS_TITLE))
    )
    assert featured_title.is_displayed(), "Featured Products title should be visible"
    assert featured_title.text.upper() == "FEATURED PRODUCTS", "Title should be 'FEATURED PRODUCTS'"
    print("Found Featured Products section")

    # Find products grid
    products_grid = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, PRODUCTS_GRID))
    )
    assert products_grid.is_displayed(), "Products grid should be visible"
    print("Found products grid")

    # Find and click on "Test Product 2"
    product_links = driver.find_elements(By.CSS_SELECTOR, PRODUCT_LINK)
    target_product = None
    for link in product_links:
        if link.text.strip() == "Test Product 2":
            target_product = link
            break

    assert target_product is not None, "Test Product 2 not found"
    print("Found Test Product 2")
    target_product.click()

    # Vérifier la présence du titre produit et du bouton 'ADD TO CART'
    product_title = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "h1.product-single-name"))
    )
    assert product_title.is_displayed(), "Product title should be visible"
    assert product_title.text.strip() == "Test Product 2", f"Titre inattendu : {product_title.text}"
    print("Product title found")

    add_to_cart = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ADD_TO_CART_BUTTON))
    )
    assert add_to_cart.is_displayed(), "Add to Cart button should be visible"
    print("Found Add to Cart button")

    # Scroll to button and click
    driver.execute_script("arguments[0].scrollIntoView(true);", add_to_cart)
    time.sleep(1)  # Wait for scroll to complete
    add_to_cart.click()
    print("Clicked Add to Cart button")

    # Wait and check for mini cart
    time.sleep(2)  # Wait for mini cart to appear
    mini_carts = driver.find_elements(By.CSS_SELECTOR, MINI_CART_TOAST)
    print(f"Found {len(mini_carts)} mini cart elements")
    
    # Verify mini cart toast appears
    mini_cart = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, MINI_CART_TOAST))
    )
    assert mini_cart.is_displayed(), "Mini cart toast should be visible"

    # Verify mini cart contents
    cart_title = mini_cart.find_element(By.CSS_SELECTOR, MINI_CART_TITLE)
    assert cart_title.text == "JUST ADDED TO YOUR CART", "Cart title should be correct"

    item_name = mini_cart.find_element(By.CSS_SELECTOR, MINI_CART_ITEM_NAME)
    assert item_name.text == "Test Product 2", "Product name should be correct"

    item_qty = mini_cart.find_element(By.CSS_SELECTOR, MINI_CART_ITEM_QTY)
    assert item_qty.text == "QTY: 1", "Quantity should be 1"
    print("Verified mini cart contents")

    # Click View Cart button
    view_cart = mini_cart.find_element(By.CSS_SELECTOR, VIEW_CART_BUTTON)
    assert view_cart.is_displayed(), "View Cart button should be visible"
    print("Found View Cart button")
    view_cart.click()

    # Verify we're on the cart page
    WebDriverWait(driver, 10).until(
        EC.url_to_be(CART_URL)
    )
    print("Navigated to cart page")
