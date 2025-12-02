import pytest

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

# Credenciales
VALID_USERNAME = "standard_user"
VALID_PASSWORD = "secret_sauce"


@pytest.mark.ui
def test_complete_checkout_flow(driver):
    """
    Caso de prueba:
    - Login con credenciales válidas
    - Agregar un producto al carrito
    - Ir al carrito y proceder al checkout
    - Completar la información de envío
    - Finalizar la compra
    - Verificar mensaje de confirmación de orden

    Este test cubre un flujo completo de compra.
    """
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    # 1) Login
    login_page.open_login_page()
    login_page.login(username=VALID_USERNAME, password=VALID_PASSWORD)
    assert inventory_page.is_loaded(), "La página de inventario no se cargó correctamente."

    # 2) Agregar producto al carrito
    inventory_page.add_backpack_to_cart()
    assert inventory_page.get_cart_badge_count() == 1, "El carrito no muestra 1 producto tras agregarlo."

    # 3) Ir al carrito
    inventory_page.go_to_cart()
    assert cart_page.get_items_count() == 1, "El carrito no tiene exactamente 1 producto antes del checkout."

    # 4) Ir al checkout
    cart_page.click_checkout()

    # 5) Completar información del cliente
    checkout_page.fill_checkout_information(
        first_name="Eudes",
        last_name="Mieres",
        postal_code="1234",
    )
    checkout_page.click_continue()

    # 6) Finalizar compra
    checkout_page.click_finish()

    # 7) Verificar mensaje de confirmación
    assert checkout_page.is_order_complete(), "No se mostró la pantalla de orden completada."
    complete_message = checkout_page.get_complete_message()
    assert "Thank you for your order" in complete_message, (
        f"El mensaje de confirmación no es el esperado. Mensaje real: '{complete_message}'"
    )
