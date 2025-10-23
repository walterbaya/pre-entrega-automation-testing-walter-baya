from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.login import login
from selenium.webdriver.chrome.options import Options

def test_login():

    #Desactivo esto para usar un perfil limpio y asi evitar las comprobaciones de contraseña
    chrome_options = Options()
    chrome_options.add_argument("--incognito")

    driver = webdriver.Chrome(options=chrome_options)

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