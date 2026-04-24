# Dashboard de anuncios de coches

## Descripción del proyecto

Este proyecto consiste en el desarrollo de una aplicación web interactiva para el análisis de un conjunto de datos de anuncios de venta de coches en Estados Unidos.

El objetivo principal es explorar y visualizar información relevante mediante gráficos interactivos, permitiendo identificar patrones en variables como el kilometraje (odómetro) y el precio de los vehículos.

## Tecnologías utilizadas

* Python
* pandas
* plotly-express
* streamlit

## Funcionalidad

La aplicación web incluye:

* Un encabezado descriptivo
* Un botón para generar un histograma de la variable odómetro
* Un botón para generar un gráfico de dispersión entre el odómetro y el precio

Los gráficos se generan dinámicamente a partir de la interacción del usuario.

## Estructura del proyecto

```
s7_prjct/
├── app.py
├── vehicles_us.csv
├── requirements.txt
├── README.md
└── notebooks/
    └── EDA.ipynb
```

## Ejecución del proyecto

1. Clonar el repositorio:

```
git clone <URL_DEL_REPOSITORIO>
```

2. Crear y activar un entorno virtual:

```
python3 -m venv vehicles_env
source vehicles_env/bin/activate
```

3. Instalar dependencias:

```
pip install -r requirements.txt
```

4. Ejecutar la aplicación:

```
streamlit run app.py
```

## Aplicación en línea

La aplicación desplegada estará disponible en:
https://s7-prjct.onrender.com/

## Autor

Laura D. Ladino F.
