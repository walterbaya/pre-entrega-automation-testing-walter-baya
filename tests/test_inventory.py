from selenium import webdriver
from selenium.webdriver.common.by import By



def test_inventory():

    driver = webdriver.Chrome()

    driver.implicitly_wait(5)

    try:
        login(driver)

        assert "/inventory" in driver.current_url, "No se redirigio correctamente al inventario."

        main_title = driver.find_element(By.CSS_SELECTOR, "div.app_logo").text 

        #Verificar que el título de la página de inventario sea correcto
        assert main_title == "Swag Labs"

        #Comprobar que existan productos visibles en la página (al menos verificar la presencia de uno)

        #Lista nombre/precio del primero.

        #Validar que elementos importantes de la interfaz estén presentes (menú, filtros, etc.)

    except Exception as e:
        raise
    finally:
        driver.quit()





