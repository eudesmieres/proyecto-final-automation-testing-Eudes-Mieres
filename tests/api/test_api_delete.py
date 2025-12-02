import pytest


@pytest.mark.api
def test_delete_post_returns_success_status(api_client):
    """
    Caso de prueba:
    - Realizar un DELETE a /posts/1
    - Verificar que el status code indique éxito (200 o 204)
    - Validar que la respuesta no contenga un error
      (en JSONPlaceholder la respuesta suele ser un JSON vacío).
    """
    response = api_client.delete("/posts/1")

    # un 200 o 204 para DELETE exitoso
    assert response.status_code in (200, 204), (
        f"Se esperaba status code 200 o 204 pero se obtuvo {response.status_code}"
    )

    # JSONPlaceholder devuelve un {} o cuerpo vacío
    try:
        data = response.json()
        # Si parsea JSON, esperamos que sea un dict (posiblemente vacío)
        assert isinstance(data, dict), "La respuesta DELETE debería ser un JSON tipo objeto."
    except ValueError:
        # Si no se puede parsear, aceptamos cuerpo vacío
        pass
