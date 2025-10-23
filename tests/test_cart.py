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

        #capturamos el producto 0

        product0 = products[0]
        
        product_title = product0.find_element(By.CSS_SELECTOR, "div.inventory_item_name ").text
        product_price = product0.find_element(By.CSS_SELECTOR, "div.inventory_item_price").text

        #Seleccionamos el botón y lo cliqueamos

        product0.find_element(By.TAG_NAME, "button").click()  

        #Esperamos a que el texto que aparezca sea 1, en otro caso lanzara un error 
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "span.shopping_cart_badge"),"1"))


        #Navegar al carrito de compras

        shopping_cart_container = driver.find_element(By.ID, "shopping_cart_container")
        shopping_cart_container.find_element(By.TAG_NAME, "a").click()


        #Comprobar que aparezca un producto

        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.cart_item")))
        
        #verificamos que sea solo uno y sea especificamente ese
        items = driver.find_elements(By.CSS_SELECTOR, "div.cart_item")

        assert len(items) == 1

        #Obtenemos el unico, su nombre y precio
        item = items[0]
        item_price = item.find_element(By.CSS_SELECTOR, "div.inventory_item_price").text
        item_title = item.find_element(By.CSS_SELECTOR, "div.inventory_item_name").text

        #Obtenemos la misma informacion del producto original Comparamos el nombre y precio        
        assert product_price == item_price and product_title == item_title
        
    except Exception as e:
        raise
    finally:
        driver.quit()