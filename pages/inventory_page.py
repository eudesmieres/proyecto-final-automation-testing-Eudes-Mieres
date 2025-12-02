from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class InventoryPage(BasePage):
    """
    Representa la página de inventario (productos) de SauceDemo.
    Se muestra después de un login exitoso.
    """

    INVENTORY_CONTAINER = (By.ID, "inventory_container")
    TITLE = (By.CSS_SELECTOR, ".title")

    # Producto
    BACKPACK_ADD_TO_CART_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")

    # Icono del carrito y con cantidad
    CART_ICON = (By.ID, "shopping_cart_container")
    CART_BADGE = (By.CSS_SELECTOR, ".shopping_cart_badge")

    def is_loaded(self) -> bool:
        """
        Verifica que la página de inventario esté cargada.
        Utilizamos la visibilidad del contenedor principal.
        """
        return self.is_element_visible(*self.INVENTORY_CONTAINER)

    def get_title_text(self) -> str:
        """
        Devuelve el texto del título de la página (ej: 'Products').
        """
        return self.get_text(*self.TITLE)

    def add_backpack_to_cart(self):
        """
        Agrega el producto 'Sauce Labs Backpack' al carrito.
        """
        self.click(*self.BACKPACK_ADD_TO_CART_BUTTON)

    def go_to_cart(self):
        """
        Hace clic en el icono del carrito para ir a la página de carrito.
        """
        self.click(*self.CART_ICON)

    def get_cart_badge_count(self) -> int:
        """
        Devuelve la cantidad de productos mostrada en el badge del carrito.
        Si no hay badge visible, significa que no hay productos.
        """
        if self.is_element_visible(*self.CART_BADGE):
            text = self.get_text(*self.CART_BADGE)
            try:
                return int(text)
            except ValueError:
                return 0
        return 0
