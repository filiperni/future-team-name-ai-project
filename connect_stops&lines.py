from classes import Przystanek, Linia, StopInTrip
import matplotlib.pyplot as plt
import numpy as np
import requests
import json


lista_przystankow_dict = json.load(open('data/lista_przystankow.json', encoding="utf-8"))
lista_przystankow = [Przystanek(stop["stopId"], stop["stopLon"], stop["stopLat"]) for stop in lista_przystankow_dict["2023-01-12"]["stops"]]

lista_linii_dict = json.load(open('data/lista_linii.json', encoding="utf-8"))
lista_linii = [Linia(line["routeId"], line["routeShortName"], line["routeType"]) for line in lista_linii_dict["2023-01-12"]["routes"]]

stopsInTrip_dict = json.load(open('data/stopsintrip.json', encoding="utf-8"))
lista_stopInTrip = [StopInTrip(stopInTrip['routeId'], stopInTrip['stopId']) for stopInTrip in stopsInTrip_dict["2023-01-12"]["stopsInTrip"]]


for linia in lista_linii:
    for stopInTrip in lista_stopInTrip:
        if linia.routeID == stopInTrip.routeID:
            for przystanek in lista_przystankow:
                if przystanek.stopId == stopInTrip.stopID:
                    linia.add_przstanek(przystanek)

# for i, _ in enumerate(lista_linii):
#     print(f"Linia {lista_linii[i].routeID} ma {len(lista_linii[i].przystanki_na_linii)} przystanków", )
# print(type(lista_linii[0]))


for i, linia in enumerate(lista_linii):
    fig, ax = plt.subplots()
    ax.grid()
    for przystanek in lista_przystankow:
        ax.plot(przystanek.stopLon, przystanek.stopLat, 'ro')
    for przystanek in linia.przystanki_na_linii:
        ax.plot(przystanek.stopLon, przystanek.stopLat, 'bo')

    plt.title(f"{linia.routeShortName}, {i}")
    plt.show()


