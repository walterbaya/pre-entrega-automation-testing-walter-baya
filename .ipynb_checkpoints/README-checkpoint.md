# Proyecto de Automatización — SauceDemo (Pre-Entrega Final)
## Propósito del proyecto

Este proyecto tiene como objetivo automatizar pruebas funcionales del sitio SauceDemo
 utilizando Python, Selenium y Pytest.
El propósito es validar los principales flujos de usuario en la aplicación, asegurando que el proceso de inicio de sesión, navegación por el catálogo y gestión del carrito de compras funcionen correctamente.

🧰 Tecnologías utilizadas

Python 3.10+

Pytest → Framework de testing

Selenium WebDriver → Automatización del navegador

pytest-html → Generación de reportes en formato HTML

pytest-xdist (opcional) → Ejecución paralela de pruebas

⚙️ Instalación de dependencias

Clonar el repositorio:

git clone https://github.com/usuario/pre-entrega-final.git
cd pre-entrega-final


(Opcional) Crear y activar un entorno virtual:

python -m venv venv
source venv/bin/activate     # En Linux/Mac
venv\Scripts\activate        # En Windows


Instalar las dependencias necesarias:

pip install -r requirements.txt


El archivo requirements.txt debe incluir:

pytest
selenium
pytest-html
pytest-xdist

🧩 Casos de Prueba Automatizados
🔐 1. Automatización de Login

Objetivo: Verificar que el login funcione correctamente con credenciales válidas.
Pasos:

Navegar a la página de login de SauceDemo
.

Ingresar usuario: standard_user

Ingresar contraseña: secret_sauce

Validar que el login sea exitoso comprobando que se redirija a la página de inventario (/inventory.html).

🛒 2. Navegación y Verificación del Catálogo

Objetivo: Validar la correcta carga de la página de inventario.
Pasos:

Verificar que el título de la página sea el esperado (“Products”).

Comprobar que haya al menos un producto visible.

Validar la presencia de elementos clave de la interfaz, como el menú lateral, el filtro de productos y el ícono del carrito.

🧺 3. Caso de Prueba de Carrito

Objetivo: Verificar el correcto funcionamiento del carrito de compras.
Pasos:

Añadir un producto al carrito haciendo clic en el botón “Add to cart”.

Validar que el contador del carrito se incremente a “1”.

Navegar al carrito de compras (/cart.html).

Verificar que el producto agregado se muestre correctamente dentro del carrito.

▶️ Ejecución de las pruebas

Para ejecutar todas las pruebas con salida detallada:

pytest -v


Para ejecutar únicamente las pruebas del archivo principal:

pytest pre-entrega-final/test_saucedemo.py -v

📊 Generación de reporte HTML

Podés generar un reporte visual de los resultados con el siguiente comando:

pytest pre-entrega-final/test_saucedemo.py -v --html=reporte.html


Esto creará un archivo reporte.html en la raíz del proyecto, que podrás abrir en cualquier navegador web para ver el resumen de las pruebas ejecutadas.

📁 Estructura del proyecto
pre-entrega-final/
│
├── pages/                      # Clases Page Object (login, inventario, carrito)
├── tests/
│   ├── test_saucedemo.py       # Archivo principal de pruebas automatizadas
│
├── conftest.py                 # Configuración global y fixtures de Pytest
├── requirements.txt            # Dependencias del proyecto
├── reporte.html                # Reporte HTML generado (opcional)
└── README.md                   # Este archivo

🧑‍💻 Autor

Nombre: [Tu nombre o legajo]
Materia: Testing Automatizado / Pre-Entrega Final
Institución: [Nombre de la institución o curso]