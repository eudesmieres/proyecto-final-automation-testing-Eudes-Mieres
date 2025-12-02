from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CheckoutPage(BasePage):
    """
    Representa las pantallas del flujo de checkout de SauceDemo:
    - Checkout: Your Information
    - Checkout: Overview
    - Checkout: Complete
    """

    # Paso 1: formulario de información del cliente
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")

    # Paso 2: overview y botón finalizar
    FINISH_BUTTON = (By.ID, "finish")

    # Paso 3: confirmación de compra
    COMPLETE_HEADER = (By.CSS_SELECTOR, "[data-test='complete-header']")

    def fill_checkout_information(self, first_name: str, last_name: str, postal_code: str):
        """
        Completa el formulario de información del cliente en el paso 1 del checkout.
        """
        self.type(*self.FIRST_NAME_INPUT, text=first_name)
        self.type(*self.LAST_NAME_INPUT, text=last_name)
        self.type(*self.POSTAL_CODE_INPUT, text=postal_code)

    def click_continue(self):
        """
        Hace clic en el botón 'Continue' (paso 1 del checkout).
        """
        self.click(*self.CONTINUE_BUTTON)

    def click_finish(self):
        """
        Hace clic en el botón 'Finish' (paso 2 del checkout).
        """
        self.click(*self.FINISH_BUTTON)

    def is_order_complete(self) -> bool:
        """
        Verifica que se muestre el mensaje de orden completada.
        """
        return self.is_element_visible(*self.COMPLETE_HEADER)

    def get_complete_message(self) -> str:
        """
        Devuelve el texto del mensaje de completado de la orden.
        Ejemplo: 'Thank you for your order!'
        """
        return self.get_text(*self.COMPLETE_HEADER)
