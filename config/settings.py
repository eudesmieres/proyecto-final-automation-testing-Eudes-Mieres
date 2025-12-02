import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# URLs
BASE_URL_UI = "https://www.saucedemo.com"
BASE_URL_API = "https://jsonplaceholder.typicode.com"

# Configuración del navegador
BROWSER = os.getenv("BROWSER", "chrome")

IMPLICIT_WAIT = 10        # espera implícita
PAGE_LOAD_TIMEOUT = 30    # carga de página


SCREENSHOTS_DIR = BASE_DIR / "screenshots"
REPORTS_DIR = BASE_DIR / "reports"

# Se crea un directorios si no existe
for path in (SCREENSHOTS_DIR, REPORTS_DIR):
    path.mkdir(parents=True, exist_ok=True)
