# ma-modelos-predictivos-poyecto-final

Proyecto Final de la materia Modelos Predictivos dentro de la Maestría en Analítica de Datos.

## Estructura del Proyecto

El proyecto está organizado de la siguiente manera:

```
.gitignore
Avance_EDeGracia_8-788-1186.docx
Propuesta_EDeGracia_8-788-1186.docx
README.md
notebook/
    data_prep.ipynb
    RegresionLineaMultiple.ipynb
    data/
        openb_pod_list_cpu0.csv
    utils/
        __init__.py
        udf.py
```

### Descripción de Carpetas y Archivos

- **notebook/**: Contiene los notebooks de Jupyter utilizados para el análisis y modelado.
  - `data_prep.ipynb`: Notebook para la preparación de datos.
  - `RegresionLineaMultiple.ipynb`: Notebook que implementa un modelo de regresión lineal múltiple.
- **notebook/data/**: Carpeta que almacena los datos utilizados en el proyecto.
  - `openb_pod_list_cpu0.csv`: Archivo CSV con datos de entrada.
- **notebook/utils/**: Contiene utilidades y funciones personalizadas.
  - `__init__.py`: Archivo de inicialización del módulo.
  - `udf.py`: Archivo con funciones definidas por el usuario (UDFs).
- **Avance_EDeGracia_8-788-1186.docx**: Documento con el avance del proyecto.
- **Propuesta_EDeGracia_8-788-1186.docx**: Documento con la propuesta inicial del proyecto.

## Objetivo del Proyecto

El objetivo de este proyecto es desarrollar un modelo predictivo que permita analizar y predecir comportamientos específicos basados en los datos proporcionados.

## Progreso Actual

1. **Preparación de Datos**: Se ha trabajado en la limpieza y preparación de los datos en el notebook `data_prep.ipynb`.
2. **Modelado**: Se ha implementado un modelo de regresión lineal múltiple en el notebook `RegresionLineaMultiple.ipynb`.
3. **Documentación**: Se han elaborado los documentos de propuesta y avance del proyecto.

## Próximos Pasos

- Refinar el modelo de regresión lineal múltiple.
- Explorar otros modelos predictivos para mejorar la precisión.
- Generar visualizaciones para presentar los resultados.
- Completar la documentación final del proyecto.

## Requisitos

- Python 3.x
- Jupyter Notebook
- Librerías necesarias (especificar en un archivo `requirements.txt` si aplica).

## Cómo Ejecutar

1. Clona este repositorio.
2. Navega a la carpeta `notebook/`.
3. Abre los notebooks en Jupyter para explorar y ejecutar el código.
