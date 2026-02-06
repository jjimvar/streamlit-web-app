# Predicción de criptoactivos (Streamlit)

Pequeña aplicación web en Streamlit para visualizar y predecir (explorar) cotizaciones de criptoactivos usando datos de `yfinance`.

**Descripción**
- Interfaz interactiva para seleccionar Bitcoin o Ethereum, elegir rango de fechas y visualizar la serie de precios de cierre.
- Muestra métricas clave: precio actual, capitalización y volumen, y rentabilidades en distintos horizontes.
- Los datos se obtienen de Yahoo Finance mediante la librería `yfinance`.

**Requisitos**
- Python 3.8+ (se recomienda 3.10 o superior)
- Dependencias listadas en `requirements.txt` (ej. `streamlit`, `yfinance`, `pandas`)

**Instalación**
1. Crear y activar un entorno virtual (opcional pero recomendado):

```
python -m venv .venv
# Windows
.venv\\Scripts\\activate
```
2. Instalar dependencias:

```
python -m pip install -r requirements.txt
```

**Ejecución**
- Para arrancar la app localmente:

```
streamlit run home.py
# o
python -m streamlit run home.py
```

**Archivos importantes**
- `home.py`: archivo principal de la app (interfaz Streamlit y visualizaciones).
- `utils.py`: utilidades auxiliares (si aplica).
- `requirements.txt`: dependencias del proyecto.
- `Readme.md`: este archivo.

**Cómo funciona (resumen)**
- El usuario selecciona el criptoactivo (Bitcoin o Ethereum).
- Se descargan los datos históricos con `yfinance` y se filtran por las fechas seleccionadas.
- Se muestran gráficos de la cotización, métricas y rentabilidades en periodos predefinidos.

**Notas y recomendaciones**
- Algunos campos como `marketCap` o `volume24Hr` pueden no estar disponibles para todos los tickers; el código actual asume que existen — revisar `ticker.info` si hay errores.
- Para mejorar rendimiento, considerar habilitar caching en las funciones de descarga de datos (ej. `@st.cache_data`).
- Extensiones posibles: añadir modelos de predicción, más activos, o exportación de datos.

**Contacto / Próximos pasos**
- Si quieres, puedo añadir instrucciones para desplegar la app en Streamlit Cloud o Docker, o integrar un modelo de predicción.
