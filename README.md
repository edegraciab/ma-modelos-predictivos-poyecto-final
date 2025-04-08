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
    01-DataPrep.ipynb
    02-RegresionLineal.ipynb
    03.RandomForest.ipynb
    data/
        cleaned_data.csv
        concatenated_openb_pod_all.csv
    utils/
        __init__.py
        concatenate.py
        graph_boxplot.py
        udf_outliers.py
        udf.py
```

### Descripción de Carpetas y Archivos

- **notebook/**: folder con los notebooks de Jupyter utilizados para el análisis y modelado.
  - `01-DataPrep.ipynb`: Notebook para la preparación de datos y análisis descriptivo.
  - `02-RegresionLineal.ipynb`: Notebook que implementa un modelo de regresión lineal múltiple.
  - `03.RandomForest.ipynb`: Notebook que implementa un modelo de Random Forest.
- **notebook/data/**: Carpeta que almacena los datos utilizados en el proyecto.
  - `cleaned_data.csv`: Archivo CSV con los datos limpios.
  - `concatenated_openb_pod_all.csv`: Archivo CSV con datos concatenados de multiples cluster con data de 2023.
- **notebook/utils/**: Contiene utilidades y funciones personalizadas.
  - `__init__.py`: Archivo de inicialización del módulo.
  - `concatenate.py`: Script para concatenar los cvs del proyecto original ubicados en: https://github.com/alibaba/clusterdata/tree/master/cluster-trace-gpu-v2023/csv.
  - `graph_boxplot.py`: Script para generar gráficos de boxplot de manera dinamico.
  - `udf_outliers.py`: Script con funciones para manejar outliers.
  - `udf.py`: Archivo con funciones definidas por el usuario (UDFs).
- **Propuesta_EDeGracia_8-788-1186.docx**: Documento con la propuesta inicial del proyecto.
- **Avance_EDeGracia_8-788-1186.docx**: Documento con el avance del proyecto.

## Objetivo del Proyecto

El objetivo de este proyecto es desarrollar un modelo predictivo que permita analizar y predecir comportamientos específicos basados en los datos proporcionados.

## Progreso Actual

1. **Preparación de Datos**: 
   - Se ha trabajado en la limpieza y preparación de los datos en el notebook `01-DataPrep.ipynb`.
2. **Modelado**: 
   - Se ha implementado un modelo de regresión lineal múltiple en el notebook `02-RegresionLineal.ipynb`.
   - Se ha implementado un modelo de Random Forest en el notebook `03.RandomForest.ipynb`.
3. **Documentación**: 
   - Se han elaborado los documentos de propuesta y avance del proyecto.

## Próximos Pasos

- Refinar los modelos implementados para mejorar su precisión.
- Explorar otros modelos predictivos adicionales.
- Generar visualizaciones avanzadas para presentar los resultados.
- Completar la documentación final del proyecto.

## Requisitos

- Python 3.x
- Jupyter Notebook
- Librerías necesarias (especificar en un archivo `requirements.txt` si aplica).

## Cómo Ejecutar

1. Clona este repositorio.
2. Navega a la carpeta `notebook/`.
3. Abre los notebooks en Jupyter para explorar y ejecutar el código.