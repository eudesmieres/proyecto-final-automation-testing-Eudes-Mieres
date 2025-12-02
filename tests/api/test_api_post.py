import pytest


@pytest.mark.api
def test_create_post_returns_201_and_valid_body(api_client):
    """
    Caso de prueba:
    - Realizar un POST a /posts con un body simple
    - Verificar que el status code sea 201 (creado)
    - Validar que la respuesta contenga los mismos datos enviados y un id generado
    """
    payload = {
        "title": "Automation Test Post",
        "body": "This is a test post created by an automated test.",
        "userId": 1,
    }

    response = api_client.post("/posts", json=payload)

    # JSONPlaceholder suele devolver 201 al crear recursos
    assert response.status_code == 201, (
        f"Se esperaba status code 201 pero se obtuvo {response.status_code}"
    )

    data = response.json()

    # Validar respuesta
    for key, value in payload.items():
        assert key in data, f"Falta la clave '{key}' en la respuesta JSON."
        assert data[key] == value, (
            f"El valor de '{key}' en la respuesta no coincide con el enviado. "
            f"Enviado: {value}, Recibido: {data[key]}"
        )

    # Validar la generacion de un nuevo id
    assert "id" in data, "La respuesta no contiene el campo 'id' para el recurso creado."
