import pytest

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

# Credenciales
VALID_USERNAME = "standard_user"
VALID_PASSWORD = "secret_sauce"


@pytest.mark.ui
def test_add_single_product_to_cart(driver):
    """
    Caso de prueba:
    - Login con credenciales válidas
    - Agregar un producto (Sauce Labs Backpack) al carrito
    - Verificar que el carrito muestre 1 producto
    - Verificar que el producto correcto esté en el carrito
    """
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)

    # 1) Abrir la página de login y autenticarse
    login_page.open_login_page()
    login_page.login(username=VALID_USERNAME, password=VALID_PASSWORD)

    # 2) Verificamos que la página de inventario está cargada
    assert inventory_page.is_loaded(), "La página de inventario no se cargó correctamente."

    # 3) Agregar al carrito
    inventory_page.add_backpack_to_cart()

    # 4) Verificar que el carrito muestre '1'
    badge_count = inventory_page.get_cart_badge_count()
    assert badge_count == 1, f"Se esperaba 1 producto en el carrito, pero hay {badge_count}."

    # 5) Ir al carrito
    inventory_page.go_to_cart()

    # 6) Verificar que el carrito muestre 1 producto y que sea el esperado
    assert cart_page.is_loaded(), "La página de carrito no se cargó correctamente."
    assert cart_page.get_items_count() == 1, "El carrito no tiene exactamente 1 producto."

    item_names = cart_page.get_item_names()
    assert "Sauce Labs Backpack" in item_names, (
        f"El producto 'Sauce Labs Backpack' no está en el carrito. Productos encontrados: {item_names}"
    )
