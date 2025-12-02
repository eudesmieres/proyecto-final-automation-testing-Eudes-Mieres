import pytest


@pytest.mark.api
def test_get_post_by_id_returns_valid_structure(api_client):
    """
    Caso de prueba:
    - Realizar un GET a /posts/1
    - Verificar que el status code sea 200
    - Validar que la respuesta tenga la estructura esperada (userId, id, title, body)
    """
    response = api_client.get("/posts/1")

    # Status
    assert response.status_code == 200, (
        f"Se esperaba status code 200 pero se obtuvo {response.status_code}"
    )

    # Estructura JSON
    data = response.json()
    for key in ("userId", "id", "title", "body"):
        assert key in data, f"Falta la clave '{key}' en la respuesta JSON."

    # Tipos de datos básicos
    assert isinstance(data["userId"], int), "userId debería ser un entero."
    assert isinstance(data["id"], int), "id debería ser un entero."
    assert isinstance(data["title"], str), "title debería ser un string."
    assert isinstance(data["body"], str), "body debería ser un string."
