from typing import Any, Dict, Optional

import requests

from config.settings import BASE_URL_API


class ApiClient:
    """
    Cliente simple para consumir APIs REST.
    Envuelve la librería requests para centralizar la base URL.
    """

    def __init__(self, base_url: str = BASE_URL_API):
        # No '/' duplicadas
        self.base_url = base_url.rstrip("/")

    def _build_url(self, path: str) -> str:
        """
        Construye la URL completa a partir de la ruta relativa.
        """
        return f"{self.base_url}/{path.lstrip('/')}"

    def get(self, path: str, params: Optional[Dict[str, Any]] = None, **kwargs):
        """
        Envía una petición GET.
        """
        url = self._build_url(path)
        return requests.get(url, params=params, **kwargs)

    def post(
        self,
        path: str,
        json: Optional[Dict[str, Any]] = None,
        data: Optional[Dict[str, Any]] = None,
        **kwargs,
    ):
        """
        Envía una petición POST.
        """
        url = self._build_url(path)
        return requests.post(url, json=json, data=data, **kwargs)

    def delete(self, path: str, **kwargs):
        """
        Envía una petición DELETE.
        """
        url = self._build_url(path)
        return requests.delete(url, **kwargs)
