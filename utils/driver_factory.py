import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from config.settings import BROWSER, IMPLICIT_WAIT, PAGE_LOAD_TIMEOUT


def create_driver(headless: bool = False):
    """
    Crea una instancia de WebDriver según el navegador configurado.
    Por simplicidad, implementamos Chrome.
    """
    browser = BROWSER.lower()

    if browser == "chrome":
        chrome_options = Options()

        # Activar modo headless
        if headless or os.getenv("HEADLESS", "false").lower() == "true":
            # 'new' es la forma recomendada en versiones recientes de Chrome
            chrome_options.add_argument("--headless=new")

        chrome_options.add_argument("--start-maximized")

        driver = webdriver.Chrome(options=chrome_options)
    else:
        # Se podría extender a otros navegadores si fuera necesario
        raise ValueError(f"Browser '{BROWSER}' is not supported in this project.")

    # Esperas
    driver.implicitly_wait(IMPLICIT_WAIT)
    driver.set_page_load_timeout(PAGE_LOAD_TIMEOUT)

    return driver
