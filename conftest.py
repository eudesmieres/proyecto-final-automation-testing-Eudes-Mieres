import pytest

from utils.driver_factory import create_driver
from utils.api_client import ApiClient
from utils.logger import get_logger
from utils.screenshot import save_screenshot

logger = get_logger()


def pytest_addoption(parser):
    """
    Agrega opciones de línea de comandos para pytest.
    Aquí agregamos '--headless' para ejecutar sin interfaz gráfica.
    """
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Run UI tests in headless mode.",
    )


@pytest.fixture(scope="session")
def api_client():
    """
    Fixture de sesión para el cliente de API.
    Se reutiliza en todos los tests de API.
    """
    logger.info("Creating ApiClient for API tests.")
    return ApiClient()


@pytest.fixture
def driver(request):
    """
    Fixture para crear y cerrar el WebDriver.
    Se ejecuta en cada test de UI que lo necesite.
    """
    headless = request.config.getoption("--headless")
    logger.info("Creating WebDriver instance (headless=%s).", headless)
    driver = create_driver(headless=headless)

    yield driver

    logger.info("Quitting WebDriver instance.")
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook de pytest que se ejecuta después de cada fase del test.
    Aquí detectamos fallos y, si el test usa 'driver', tomamos un screenshot.
    Además, lo adjuntamos al reporte HTML si pytest-html está activo.
    """
    outcome = yield
    report = outcome.get_result()

    # Guardamos el reporte
    if report.when == "call":
        setattr(item, "rep_call", report)

    # Solo tomamos screenshot en fallos de la fase principal del test
    if report.when == "call" and report.failed and "driver" in item.fixturenames:
        driver = item.funcargs.get("driver")
        if driver is not None:
            logger.error("Test failed. Taking screenshot for test '%s'.", item.name)
            screenshot_path = save_screenshot(driver, item.name)
            logger.error("Screenshot saved at: %s", screenshot_path)

            # Integración con pytest-html
            pytest_html = item.config.pluginmanager.getplugin("html")
            if pytest_html is not None:
                extra = getattr(report, "extra", [])
                extra.append(pytest_html.extras.png(str(screenshot_path)))
                report.extra = extra


def pytest_configure(config):
    """
    Configuración inicial de pytest.
    Aquí podríamos ajustar metadatos del reporte HTML si fuera necesario.
    Por simplicidad, solo dejamos el hook preparado.
    """

    logger.info("Pytest configured. HTML plugin active: %s",
                config.pluginmanager.hasplugin("html"))
