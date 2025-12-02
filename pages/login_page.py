from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    """
    Representa la página de login de SauceDemo.
    Contiene los localizadores y acciones disponibles.
    """

    # Localizadores
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    def open_login_page(self):
        """
        Abre la página de login.
        SauceDemo muestra el login directamente en la URL base.
        """

        self.open("")

    def login(self, username: str, password: str):
        """
        Realiza el proceso de login con las credenciales proporcionadas.
        """
        self.type(*self.USERNAME_INPUT, text=username)
        self.type(*self.PASSWORD_INPUT, text=password)
        self.click(*self.LOGIN_BUTTON)

    def get_error_message(self) -> str:
        """
        Devuelve el texto del mensaje de error mostrado en el login.
        Se usa en escenarios negativos.
        """
        return self.get_text(*self.ERROR_MESSAGE)

    def is_error_visible(self) -> bool:
        """
        Verifica si el mensaje de error está visible.
        """
        return self.is_element_visible(*self.ERROR_MESSAGE)
