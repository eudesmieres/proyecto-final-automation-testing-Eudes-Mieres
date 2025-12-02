from datetime import datetime
from pathlib import Path

from config.settings import SCREENSHOTS_DIR


def save_screenshot(driver, test_name: str) -> Path:
    """
    Guarda una captura de pantalla en la carpeta configurada.
    El nombre incluye el nombre del test y la fecha/hora.
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_test_name = test_name.replace(" ", "_").replace("/", "_")
    filename = f"{safe_test_name}_{timestamp}.png"
    file_path = SCREENSHOTS_DIR / filename

    # Selenium guarda el screenshot en la ruta indicada
    driver.save_screenshot(str(file_path))

    return file_path
