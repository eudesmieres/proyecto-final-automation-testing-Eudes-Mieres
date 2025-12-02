import pytest

from pages.login_page import LoginPage
from utils.data_reader import load_json_data

# Cargamos los datos de prueba desde el archivo JSON
negative_login_data = load_json_data("data/login_negative_data.json")


@pytest.mark.ui
@pytest.mark.parametrize(
    "username,password,expected_error",
    [
        (item["username"], item["password"], item["expected_error"])
        for item in negative_login_data
    ],
)
def test_negative_login_shows_error_message(driver, username, password, expected_error):
    """
    Caso de prueba:
    - Abrir la página de login
    - Intentar iniciar sesión con credenciales inválidas (parametrizadas)
    - Verificar que se muestre un mensaje de error adecuado

    Este test:
    - Cubre escenarios negativos de login
    - Usa datos de prueba externos desde un archivo JSON
    """
    login_page = LoginPage(driver)

    # 1) Abrir la página de login
    login_page.open_login_page()

    # 2) Intentar login con credenciales inválidas
    login_page.login(username=username, password=password)

    # 3) Verificar que se muestre el mensaje de error
    assert login_page.is_error_visible(), "No se mostró el mensaje de error en pantalla."

    error_text = login_page.get_error_message()
    
    assert expected_error in error_text, (
        f"El mensaje de error no es el esperado.\n"
        f"Esperado que contenga: '{expected_error}'\n"
        f"Mensaje real: '{error_text}'"
    )
