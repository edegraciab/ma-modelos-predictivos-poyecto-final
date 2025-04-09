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

- **notebook/**: Contiene los notebooks de Jupyter utilizados para el análisis y modelado.
  - `01-DataPrep.ipynb`: Notebook para la preparación de datos y análisis descriptivo.
  - `02-RegresionLineal.ipynb`: Notebook que implementa un modelo de regresión lineal múltiple.
  - `03.RandomForest.ipynb`: Notebook que implementa un modelo de Random Forest para predecir el uso de memoria (`memory_gbs`).
- **notebook/data/**: Carpeta que almacena los datos utilizados en el proyecto.
  - `cleaned_data.csv`: Archivo CSV con los datos limpios.
  - `concatenated_openb_pod_all.csv`: Archivo CSV con datos concatenados de múltiples clústeres con data de 2023.
- **notebook/utils/**: Contiene utilidades y funciones personalizadas.
  - `__init__.py`: Archivo de inicialización del módulo.
  - `concatenate.py`: Script para concatenar los CSVs del proyecto original ubicados en: https://github.com/alibaba/clusterdata/tree/master/cluster-trace-gpu-v2023/csv.
  - `graph_boxplot.py`: Script para generar gráficos de boxplot de manera dinámica.
  - `udf_outliers.py`: Script con funciones para manejar outliers.
  - `udf.py`: Archivo con funciones definidas por el usuario (UDFs).
- **Propuesta_EDeGracia_8-788-1186.docx**: Documento con la propuesta inicial del proyecto.
- **Avance_EDeGracia_8-788-1186.docx**: Documento con el avance del proyecto.

## Objetivo del Proyecto

El objetivo de este proyecto fue desarrollar un modelo predictivo que permita analizar y predecir comportamientos específicos basados en los datos proporcionados.

## Progreso Final

1. **Preparación de Datos**: 
   - Se trabajó en la limpieza y preparación de los datos en el notebook `01-DataPrep.ipynb`.
   - Los datos fueron escalados y transformados para su uso en los modelos predictivos.
2. **Modelado**: 
   - Se implementó un modelo de regresión lineal múltiple en el notebook `02-RegresionLineal.ipynb`.
   - Se implementó un modelo de Random Forest en el notebook `03.RandomForest.ipynb` para predecir el uso de memoria (`memory_gbs`), logrando un **R²** satisfactorio y un bajo **Error Cuadrático Medio (MSE)**.
3. **Visualización**:
   - Se generaron gráficos de boxplot dinámicos utilizando el script `graph_boxplot.py` para analizar la distribución de los datos.
4. **Documentación**: 
   - Se elaboraron los documentos de propuesta y avance del proyecto, y se completó la documentación final.

## Resultados Clave

- **Modelo de Regresión Lineal**:
  - Métricas obtenidas: **R²** y **MSE** aceptables para las variables predictoras seleccionadas.
- **Modelo de Random Forest**:
  - Métricas obtenidas:
    - **Error Cuadrático Medio (MSE)**: 2.18
    - **R²**: 0.85
  - Este modelo mostró un mejor desempeño en comparación con la regresión lineal, especialmente para datos no lineales.

## Próximos Pasos

Aunque el proyecto ha concluido, se podrían explorar las siguientes mejoras:
- Implementar técnicas de optimización de hiperparámetros (como Grid Search o Random Search) para mejorar el desempeño del modelo Random Forest.
- Probar otros modelos predictivos avanzados como Gradient Boosting o XGBoost.
- Ampliar el análisis con más datos históricos para mejorar la robustez del modelo.

## Requisitos

- Python 3.x
- Jupyter Notebook
- Librerías necesarias (especificadas en el archivo `requirements.txt`):
  - `pandas`
  - `numpy`
  - `scikit-learn`
  - `matplotlib`
  - `seaborn`

## Cómo Ejecutar

1. Clona este repositorio.
2. Instala las dependencias necesarias ejecutando:
   ```bash
   pip install -r requirements.txt
   ```
3. Navega a la carpeta `notebook/`.
4. Abre los notebooks en Jupyter para explorar y ejecutar el código.

## Conclusión

Este proyecto logró implementar modelos predictivos efectivos para analizar y predecir el uso de recursos computacionales. Los resultados obtenidos son prometedores y pueden ser utilizados como base para futuros análisis y optimizaciones.