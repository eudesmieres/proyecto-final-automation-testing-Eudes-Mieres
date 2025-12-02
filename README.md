# Proyecto Final - Automation Testing (UI + API)

Este proyecto forma parte del trabajo final del curso de Automatización QA en Python.  
El objetivo es implementar un **mini framework de automatización** que integre:

- Pruebas UI con **Selenium WebDriver** + **Pytest**
- Pruebas de API con **Requests**
- Patrón **Page Object Model (POM)**
- Manejo de **datos externos** (JSON)
- **Screenshots** automáticos en fallos
- **Logging** centralizado
- **Reportes HTML** con `pytest-html`
- Integración lista para ejecutarse en **Git** / **GitHub**

---

## 👩‍💻 Autor

- Nombre: **Eudes Mieres**
- Repositorio: `proyecto-final-automation-testing-Eudes-Mieres`

---

## 🧰 Tecnologías Utilizadas

- **Lenguaje:** Python
- **Framework de testing:** Pytest
- **Automatización UI:** Selenium WebDriver
- **Pruebas de API:** Requests
- **Reportes HTML:** pytest-html
- **Control de versiones:** Git
- **Repositorio remoto:** GitHub

---

## 📁 Estructura del Proyecto

```bash
proyecto-final-automation-testing-Eudes-Mieres/
├─ config/
│  └─ settings.py          
├─ pages/                 
│  ├─ __init__.py
│  ├─ base_page.py         
│  ├─ login_page.py 
│  ├─ inventory_page.py 
│  ├─ cart_page.py 
│  └─ checkout_page.py
├─ tests/
│  ├─ __init__.py
│  ├─ ui/  
│  │  ├─ __init__.py
│  │  ├─ test_login.py 
│  │  ├─ test_negative_login.py    
│  │  ├─ test_add_to_cart.py 
│  │  └─ test_checkout.py 
│  └─ api/ 
│     ├─ __init__.py
│     ├─ test_api_get.py 
│     ├─ test_api_post.py 
│     └─ test_api_delete.py
├─ utils/
│  ├─ __init__.py
│  ├─ driver_factory.py
│  ├─ logger.py
│  ├─ screenshot.py
│  ├─ api_client.py
│  └─ data_reader.py
├─ data/
│  └─ login_negative_data.json
├─ screenshots/
├─ reports/
├─ conftest.py
├─ pytest.ini
├─ requirements.txt
└─ READM
```

---

## ⚙️ Configuración de Entorno

- **1.Clonar el repositorio:** 
git clone https://github.com/<usuario>/proyecto-final-automation-testing-Eudes-Mieres.git
cd proyecto-final-automation-testing-Eudes-Mieres

- **2.Instalar dependencias:**
pip3 install -r requirements.txt

- **3.Requisitos de navegador:**
Este proyecto utiliza Google Chrome y ChromeDriver:

Tener Chrome instalado
Tener chromedriver accesible en el PATH

---

## 🔧 Configuración Global
- **URLs de prueba**
- BASE_URL_UI = "https://www.saucedemo.com"
- BASE_URL_API = "https://jsonplaceholder.typicode.com"

---

## 🧪 Ejecución de Pruebas
- **Ejecutar todas las pruebas (UI + API)**
pytest --html=reports/report_all.html --self-contained-html

- **Ejecutar solo pruebas de UI**
pytest -m ui --html=reports/report_ui.html --self-contained-html

- **Ejecutar solo pruebas de API**
pytest -m api --html=reports/report_api.html --self-contained-html
