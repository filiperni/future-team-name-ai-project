import json
import matplotlib.pyplot as plt
import numpy as np
from przystanek import Przystanek


def plot(A, B, list1, list2=None):
    fig, ax = plt.subplots()
    ax.grid()

    for stop1 in list1:
        ax.plot(stop1.x, stop1.y, 'bo')
    if list2 is not None:
        for stop1 in list2:
            ax.plot(stop1.x, stop1.y, 'go')
    ax.plot(A.x, A.y, 'ro')
    ax.plot(B.x, B.y, 'ro')

    plt.show()


def najb_przystanki(start_x, start_y, dest_x, dest_y):
    lista_przystankow_json = json.load(open('lista_przystankow.json', encoding="utf-8"))
    lista_przystankow = [Przystanek(stop["stopId"], stop["stopLon"], stop["stopLat"]) for stop in lista_przystankow_json["2023-01-12"]["stops"]]

    start = Przystanek(00, start_x, start_y)
    dest = Przystanek(99, dest_x, dest_y)

    for p in lista_przystankow:
        p.dist_to_start = np.sqrt(np.power(p.x - start.x, 2) + np.power(p.y - start.y, 2))
        p.dist_to_dest = np.sqrt(np.power(p.x - dest.x, 2) + np.power(p.y - dest.y, 2))

    sorted_start = sorted(lista_przystankow, key=lambda x: x.dist_to_start)
    sorted_dest = sorted(lista_przystankow, key=lambda x: x.dist_to_dest)

    # sorted_start_short = sorted_start[0:5]
    # sorted_dest_short = sorted_dest[0:5]
    # plot(start, dest, lista_przystankow, sorted_start_short+sorted_dest_short)
    return sorted_start, sorted_dest

