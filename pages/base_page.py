from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.settings import BASE_URL_UI, PAGE_LOAD_TIMEOUT


class BasePage:
    """
    Clase base que contiene funcionalidad común para todas las páginas.
    """

    def __init__(self, driver: WebDriver):
        # Selenium
        self.driver = driver
        self.base_url = BASE_URL_UI

    def open(self, path: str = ""):
        """
        Abre una URL relativa al sitio base.
        Ejemplo: path = "" -> BASE_URL_UI
                 path = "/inventory.html" -> BASE_URL_UI/inventory.html
        """
        url = self.base_url.rstrip("/") + "/" + path.lstrip("/")
        self.driver.get(url)

    def find(self, by: By, locator: str, timeout: int = PAGE_LOAD_TIMEOUT):
        """
        Encuentra un elemento usando una espera explícita.
        """
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.presence_of_element_located((by, locator)))

    def find_visible(self, by: By, locator: str, timeout: int = PAGE_LOAD_TIMEOUT):
        """
        Encuentra un elemento visible en la página.
        """
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.visibility_of_element_located((by, locator)))

    def click(self, by: By, locator: str, timeout: int = PAGE_LOAD_TIMEOUT):
        """
        Hace clic en un elemento cuando está clickeable.
        """
        wait = WebDriverWait(self.driver, timeout)
        element = wait.until(EC.element_to_be_clickable((by, locator)))
        element.click()

    def type(self, by: By, locator: str, text: str, timeout: int = PAGE_LOAD_TIMEOUT):
        """
        Escribe texto en un campo de entrada.
        """
        element = self.find_visible(by, locator, timeout)
        element.clear()
        element.send_keys(text)

    def get_text(self, by: By, locator: str, timeout: int = PAGE_LOAD_TIMEOUT) -> str:
        """
        Obtiene el texto de un elemento visible.
        """
        element = self.find_visible(by, locator, timeout)
        return element.text

    def is_element_visible(self, by: By, locator: str, timeout: int = PAGE_LOAD_TIMEOUT) -> bool:
        """
        Verifica si un elemento es visible en la página.
        Devuelve True si lo encuentra visible dentro del timeout.
        """
        try:
            self.find_visible(by, locator, timeout)
            return True
        except Exception:
            return False
