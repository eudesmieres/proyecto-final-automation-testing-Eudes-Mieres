import pytest

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

# Cedenciales
VALID_USERNAME = "standard_user"
VALID_PASSWORD = "secret_sauce"


@pytest.mark.ui
def test_successful_login_opens_inventory_page(driver):
    """
    Caso de prueba:
    - Abrir la página de login
    - Iniciar sesión con credenciales válidas
    - Verificar que se muestra la página de inventario

    Este test valida el flujo de login positivo.
    """
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    # 1) Abrir la página de login
    login_page.open_login_page()

    # 2) Hacer login con usuario válido
    login_page.login(username=VALID_USERNAME, password=VALID_PASSWORD)

    # 3) Verificar que se abrió la página de inventario
    assert inventory_page.is_loaded(), "La página de inventario no se cargó correctamente."
    assert inventory_page.get_title_text().lower() == "products", "El título de la página no es 'Products'."
