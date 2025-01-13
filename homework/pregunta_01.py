"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel

import matplotlib.pyplot as plt
import pandas as pd
import os

def pregunta_01():
    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.

    """

    estilos = {
        'Television': {'color': 'dimgray', 'zorder': 2, 'linewidth': 2},
        'Newspaper': {'color': 'grey', 'zorder': 1, 'linewidth': 2},
        'Internet': {'color': 'tab:blue', 'zorder': 3, 'linewidth': 3},
        'Radio': {'color': 'lightgrey', 'zorder': 1, 'linewidth': 2},
    }

    datos = pd.read_csv("files/input/news.csv", index_col=0)
    plt.figure(figsize=(8, 6))
    for categoria, propiedades in estilos.items():
        plt.plot(
            datos[categoria],
            label=categoria,
            color=propiedades['color'],
            zorder=propiedades['zorder'],
            linewidth=propiedades['linewidth'],
        )

        inicio = datos.index[0]
        fin = datos.index[-1]
        plt.scatter(inicio, datos[categoria].loc[inicio], color=propiedades['color'])
        plt.text(
            inicio - 0.3,
            datos[categoria].loc[inicio],
            f"{categoria} {datos[categoria].loc[inicio]}%",
            ha='right',
            color=propiedades['color'],
        )
        plt.scatter(fin, datos[categoria].loc[fin], color=propiedades['color'])
        plt.text(
            fin + 0.3,
            datos[categoria].loc[fin],
            f"{categoria} {datos[categoria].loc[fin]}%",
            ha='left',
            color=propiedades['color'],
        )

    plt.title("Preferred News Sources Over Time", fontsize=14, fontweight='bold')
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['left'].set_visible(False)
    plt.gca().axes.get_yaxis().set_visible(False)
    ruta_salida = "files/plots"
    os.makedirs(ruta_salida, exist_ok=True)
    plt.tight_layout()
    plt.savefig(os.path.join(ruta_salida, "news.png"))
    plt.show()

