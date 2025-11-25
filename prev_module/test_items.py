from selenium.webdriver.common.by import By
import time

def test_add_to_cart_button(browser):
    # Открываем страницу товара
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    
    # Для визуальной проверки языка
    time.sleep(30)
    
    # Проверяем наличие кнопки добавления в корзину
    add_to_cart_button = browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")
    
    # Проверяем, что кнопка отображается на странице
    assert add_to_cart_button.is_displayed(), "Add to cart button is not displayed"
