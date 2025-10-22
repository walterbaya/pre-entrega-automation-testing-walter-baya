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


        '''ACA SERIA MEJOR VERIFICAR QUE ESTEN LOS 4 ELEMENTOS DIRECTAMENTE.'''
        #Verificamos que este presente el filtro tenga 4 elementos
        filtro = driver.find_element(By.CSS_SELECTOR, "span.product_sort_container")
        
        assert len(filtro.find_elements(By.TAG, "option")) == 4


        #Verificamos que este el menu hamburguesa.
        hamburguer_button = driver.find_element(By.ID, "react-burger-menu-btn")

        #Hacemos click y verificamos que aparezcan los elementos
        hamburguer_button.click()

        assert "All items" == driver.find_element(By.ID, "a.inventory_sidebar_link").text
        assert "About" == driver.find_element(By.ID, "a.about_sidebar_link").text
        assert "Logout" == driver.find_element(By.ID, "a.logout_sidebar_link").text
        assert "Reset App State" == driver.find_element(By.ID, "a.reset_sidebar_link").text 

        #Verificamos que también esté el menu para cerrarlo una vez abierto.
        driver.find_element(By.ID, "react-burger-cross-btn")        

    except Exception as e:
        raise
    finally:
        driver.quit()





