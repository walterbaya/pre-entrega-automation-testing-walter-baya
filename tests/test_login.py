from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.login import login

def test_login():

    driver = webdriver.Chrome()

    driver.implicitly_wait(5)

    try:
    
        login(driver) 

        assert "/inventory" in driver.current_url, "No se redirigio correctamente al inventario."

        main_title = driver.find_element(By.CSS_SELECTOR, "div.app_logo").text 
        assert main_title == "Swag Labs"

        products_title = driver.find_element(By.CSS_SELECTOR, "span.title").text 
        assert products_title == "Products"

    except Exception as e:
        raise
    finally:
        
        driver.quit()