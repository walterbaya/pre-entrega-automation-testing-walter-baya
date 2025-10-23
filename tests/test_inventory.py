from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.login import login
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


def test_inventory():

    chrome_options = Options()
    chrome_options.add_argument("--incognito")

    driver = webdriver.Chrome(options=chrome_options)
    
    wait = WebDriverWait(driver, 10)

    try:
        login(driver)

        wait.until(EC.url_contains("/inventory"))

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

        #Verificamos que aparezca el simbolo $ y tambien que el nombre no sea vacio.
        assert "$" in price
        assert len(name) > 0

        #Validar que elementos importantes de la interfaz estén presentes (menú, filtros, etc.)

        #Verificamos que este presente el filtro y tenga los 4 elementos
        product_sort_container = driver.find_element(By.CSS_SELECTOR, "select.product_sort_container")
        options = product_sort_container.find_elements(By.TAG_NAME, "option")
        
        assert len(options) == 4

        wait.until(EC.visibility_of_element_located((By.ID, "react-burger-menu-btn")))

        #Verificamos que este el menu hamburguesa.
        hamburguer_button = driver.find_element(By.ID, "react-burger-menu-btn")

        #Hacemos click y verificamos que aparezcan los elementos
        hamburguer_button.click()

        #Esperamos hasta que el primer elemento se muestre
        wait.until(EC.visibility_of_element_located((By.ID, "inventory_sidebar_link")))

        assert "All Items" == driver.find_element(By.ID, "inventory_sidebar_link").text
        assert "About" == driver.find_element(By.ID, "about_sidebar_link").text
        assert "Logout" == driver.find_element(By.ID, "logout_sidebar_link").text
        assert "Reset App State" == driver.find_element(By.ID, "reset_sidebar_link").text 

        #Verificamos que también esté el menu para cerrarlo una vez abierto y lo cerramos.
        driver.find_element(By.ID, "react-burger-cross-btn").click()

        #Verificamos que se halla cerrado correctamente, o sea que se invisible ahora el menu

        wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "bm-menu-wrap")))        

        #Verificamos el carrito de compras y su elemento a cliqueable    

        shopping_cart_container = driver.find_element(By.ID, "shopping_cart_container")

        assert len(shopping_cart_container.find_elements(By.TAG_NAME, "a")) == 1
    
    except Exception as e:
        raise
    finally:
        driver.quit()





