from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.login import login



def test_inventory():

    driver = webdriver.Chrome()

    driver.implicitly_wait(5)

    try:
        login(driver)

        assert "/inventory" in driver.current_url, "No se redirigio correctamente al inventario."

        main_title = driver.find_element(By.CSS_SELECTOR, "div.app_logo").text 

        #Verificar que el título de la página de inventario sea correcto
        assert main_title == "Swag Labs", "Error, el titulo Swag Labs no esta presente"

        #Comprobar que existan productos visibles en la página (al menos verificar la presencia de uno)

        products = driver.find_elements(By.CSS_SELECTOR, "div.inventory_item")

        assert len(products) >= 1, "Error, no hay elementos en el inventario"

        #Lista nombre/precio del primero.

        price = products[0].find_element(By.CSS_SELECTOR, "div.inventory_item_price").text
        name =  products[0].find_element(By.CSS_SELECTOR, "div.inventory_item_name").text  

        assert price == "$29.99"
        assert name == "Sauce Labs Backpack"

        #Validar que elementos importantes de la interfaz estén presentes (menú, filtros, etc.)

    except Exception as e:
        raise
    finally:
        driver.quit()





