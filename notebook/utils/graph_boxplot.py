import matplotlib.pyplot as plt
import seaborn as sns

def plot_boxplots(dataframe, numeric_columns, num_cols=3, figsize=(18, 6)):
    """
    Genera boxplots para las columnas numéricas de un DataFrame.

    Parameters:
        dataframe (pd.DataFrame): El DataFrame que contiene los datos.
        numeric_columns (list): Lista de nombres de columnas numéricas a graficar.
        num_cols (int): Número de columnas por fila en los subplots.
        figsize (tuple): Tamaño de la figura (ancho, alto).

    Returns:
        None: Muestra los gráficos directamente.
    """
    # Filtrar las columnas numéricas
    box_plot_df = dataframe[numeric_columns]

    # Calcular el número de filas necesarias
    num_plots = len(box_plot_df.columns)
    num_rows = (num_plots + num_cols - 1) // num_cols  # Calcular el número de filas necesarias

    # Crear subplots
    fig, axes = plt.subplots(num_rows, num_cols, figsize=(figsize[0], figsize[1] * num_rows))
    axes = axes.flatten()

    # Ocultar subplots no utilizados
    for ax in axes[num_plots:]:
        ax.axis('off')

    # Graficar cada columna numérica como boxplot
    for ax, column in zip(axes, box_plot_df):
        sns.boxplot(data=box_plot_df, x=column, ax=ax)
        ax.set_title(f"Box Plot - {column}")
        ax.set_xlabel(column)
        ax.grid(True)

    plt.tight_layout()  # Evitar superposición
    plt.show()