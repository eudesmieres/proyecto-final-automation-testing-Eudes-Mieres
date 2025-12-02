import logging
from pathlib import Path
from config.settings import REPORTS_DIR

LOG_FILE = REPORTS_DIR / "execution.log"


def get_logger(name: str = "automation") -> logging.Logger:
    """
    Devuelve una instancia de logger configurada.
    Usa un handler para archivo y otro para consola.
    """
    logger = logging.getLogger(name)

    if not logger.handlers:
        logger.setLevel(logging.INFO)

        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )

        # Handler para archivo
        file_handler = logging.FileHandler(LOG_FILE, encoding="utf-8")
        file_handler.setFormatter(formatter)

        # Handler para consola
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger
