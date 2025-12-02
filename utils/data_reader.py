import json
from pathlib import Path

from config.settings import BASE_DIR


def load_json_data(relative_path: str):
    """
    Carga datos de prueba desde un archivo JSON.

    relative_path: ruta relativa desde la raíz del proyecto,
                   por ejemplo: "data/login_negative_data.json"
    """
    data_path = BASE_DIR / relative_path
    with open(data_path, encoding="utf-8") as file:
        return json.load(file)
