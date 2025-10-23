from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.login import login
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


def test_cart():

    chrome_options = Options()
    chrome_options.add_argument("--incognito")

    driver = webdriver.Chrome(options=chrome_options)
    
    wait = WebDriverWait(driver, 10)

    try:
        login(driver)

        wait.until(EC.url_contains("/inventory"))

        assert "/inventory" in driver.current_url, "No se redirigio correctamente al inventario."

        #Comprobar que existan productos visibles en la página (al menos verificar la presencia de uno)

        products = driver.find_elements(By.CSS_SELECTOR, "div.inventory_item")

        assert len(products) >= 1, "Error, no hay elementos en el inventario"

        #Seleccionamos el botón y lo cliqueamos
        products[0].find_element(By.TAG_NAME, "button").click()  

        #Esperamos a que el texto que aparezca sea 1, en otro caso lanzara un error 
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "span.shopping_cart_badge"),"1"))

    except Exception as e:
        raise
    finally:
        driver.quit()