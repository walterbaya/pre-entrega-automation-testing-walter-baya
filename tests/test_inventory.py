'''Caso de Prueba de Navegación:

Verificar que el título de la página de inventario sea correcto

Comprobar que existan productos visibles en la página (al menos verificar la presencia de uno)

Validar que elementos importantes de la interfaz estén presentes (menú, filtros, etc.)

Criterios mínimos:

Valida título

Valida presencia de productos 

Lista nombre/precio del primero.'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from other


def test_inventory():

    driver = webdriver.Chrome()

    driver.implicitly_wait(5)

    


    try:
        

        assert "/inventory" in driver.current_url, "No se redirigio correctamente al inventario."

        main_title = driver.find_element(By.CSS_SELECTOR, "div.app_logo").text 

        assert main_title == "Swag Labs"

        products_title = driver.find_element(By.CSS_SELECTOR, "span.title").text 

        assert products_title == "Products"

    except Exception as e:
        raise
    finally:
        driver.quit()