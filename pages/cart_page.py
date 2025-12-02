from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CartPage(BasePage):
    """
    Representa la página de carrito de SauceDemo.
    Aquí se muestran los productos agregados antes del checkout.
    """

    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    CART_ITEM_NAME = (By.CSS_SELECTOR, ".inventory_item_name")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def is_loaded(self) -> bool:
        """
        Verifica que la página de carrito esté cargada mediante
        la presencia de los ítems del carrito (o el contenedor, si lo prefieres).
        """
        # muestra el contenedor de items
        return self.is_element_visible(By.ID, "cart_contents_container")

    def get_items_count(self) -> int:
        """
        Devuelve la cantidad de productos presentes en el carrito.
        """
        elements = self.driver.find_elements(*self.CART_ITEMS)
        return len(elements)

    def get_item_names(self):
        """
        Devuelve una lista con los nombres de los productos en el carrito.
        """
        elements = self.driver.find_elements(*self.CART_ITEM_NAME)
        return [el.text for el in elements]

    def click_checkout(self):
        """
        Hace clic en el botón de checkout.
        """
        self.click(*self.CHECKOUT_BUTTON)
