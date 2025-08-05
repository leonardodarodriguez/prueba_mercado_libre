# Prueba de Automatización MercadoLibre con Python y Selenium

Este proyecto implementa un script de prueba automatizada usando "pytest", "Selenium WebDriver" y "webdriver-manager" para interactuar con [https://www.mercadolibre.com]. 

El objetivo es de la prueba cumple con:

1. Abrir la página principal de MercadoLibre.
2. Seleccionar México como país.
3. Buscar el término **"playstation 5"**.
4. Filtrar por condición **"Nuevo"**(no visualice la opcion CDMX como localidad).
5. Filtrar por ubicación **"Local"**.
6. Ordenar resultados de **menor a mayor precio**.
7. Obtener el nombre y precio de los primeros 5 productos.
8. Imprimir esos datos en la consola.
9. Generar un reporte HTML de la ejecución.
10. Tomar capturas de pantalla de cada punto

---

## Requisitos previos

* Python 3.8 o superior
* Google Chrome instalado
* Windows, macOS o Linux

---

## Instalación

1. Clonar este repositorio:

   ```bash
   git clone https://github.com/leonardodarodriguez/prueba_mercado_libre.git
   cd prueba_mercadolibre
   ```

2. Instalar dependencias:

   ```bash
   pip install -r requirements.txt
   ```

---

## Estructura de la prueba

```
Prueba_Mercado_libre/
├── screenshots/            # Capturas de pantalla de cada paso
├── tests/
│   └── test_play5.py       # Script principal de pruebas
├── pytest.ini              # Configuración de pytest 
├── report.html             # Reporte HTML generado tras la ejecución
├── requirements.txt        # Lista de paquetes Python
└── README.md               # Este archivo
```

---

## Configuración de pytest (`pytest.ini`)

```ini
[pytest]
addopts = -s --html=report.html --self-contained-html -q
testpaths = tests
python_files = test_*.py
```

* `-s`: muestra en consola los `print()` de los tests.
* `--html=report.html --self-contained-html`: genera un reporte HTML autónomo.
* `-q`: salida más limpia.
* `testpaths`: carpeta donde buscar tests.
* `python_files`: patrón de nombres de archivo.

---

## Ejecución de pruebas

```bash
python -m pytest
```

Esto mostrará en consola la ejecución con los nombre y precios de los 5 productos y generará `report.html` con:

* Información de tiempos y errores (si los hubiera)
* Estado de la ejecucion 
* Capturas de pantalla en el detalle de la ejecucion 

---

## Capturas de pantalla

Durante la ejecución se guardan imágenes en `screenshots/` 

---

## Notas

* El script crea un perfil de Chrome temporal para no interferir el perfil principal.
* `webdriver-manager` descarga automáticamente la versión correcta de `chromedriver`.
* Si Chrome se actualiza, reinstala dependencias o actualiza `webdriver-manager`.

---

