from klasy import Przystanek, Linia, StopsInTrip
import matplotlib.pyplot as plt
import numpy as np
import requests
import json


def plot(A, B, list1, list2=None):
    fig, ax = plt.subplots()
    ax.grid()

    for stop1 in list1:
        ax.plot(stop1.stopLon, stop1.stopLat, 'bo')
    if list2 is not None:
        for stop1 in list2:
            ax.plot(stop1.stopLon, stop1.stopLat, 'go')
    ax.plot(A.stopLon, A.stopLat, 'ro')
    ax.plot(B.stopLon, B.stopLat, 'ro')

    plt.show()


def najb_przystanki(start_x, start_y, dest_x, dest_y):
    url_lista_przystankow = "https://ckan.multimediagdansk.pl/dataset/c24aa637-3619-4dc2-a171-a23eec8f2172/resource/4c4025f0-01bf-41f7-a39f-d156d201b82b/download/stops.json"
    try:
        lista_przystankow_json = requests.get(url_lista_przystankow)
    except:
        print("Could not download data")

    with open('lista_przystankow.json', 'w') as out_file:
        json.dump(lista_przystankow_json.json(), out_file)

    lista_przystankow_dict = json.load(open('lista_przystankow.json', encoding="utf-8"))
    lista_przystankow = [Przystanek(stop["stopId"], stop["stopLon"], stop["stopLat"]) for stop in
                         lista_przystankow_dict["2023-01-12"]["stops"]]

    start = Przystanek(00, start_x, start_y)
    dest = Przystanek(99, dest_x, dest_y)

    for p in lista_przystankow:
        p.dist_to_start = np.sqrt(np.power(p.stopLon - start.stopLon, 2) + np.power(p.stopLat - start.stopLat, 2))
        p.dist_to_dest = np.sqrt(np.power(p.stopLon - dest.stopLon, 2) + np.power(p.stopLat - dest.stopLat, 2))

    sorted_start = sorted(lista_przystankow, key=lambda x: x.dist_to_start)
    sorted_dest = sorted(lista_przystankow, key=lambda x: x.dist_to_dest)

    sorted_start_short = sorted_start[0:5]
    sorted_dest_short = sorted_dest[0:5]
    plot(start, dest, lista_przystankow, sorted_start_short + sorted_dest_short)
    return sorted_start, sorted_dest


def generate_lista_linii():
    url_lista_przystankow = "https://ckan.multimediagdansk.pl/dataset/c24aa637-3619-4dc2-a171-a23eec8f2172/resource/4c4025f0-01bf-41f7-a39f-d156d201b82b/download/stops.json"
    try:
        lista_przystankow_json = requests.get(url_lista_przystankow)
    except:
        print("Could not download data")

    with open('lista_przystankow.json', 'w') as out_file:
        json.dump(lista_przystankow_json.json(), out_file)

    url_lista_linii = "https://ckan.multimediagdansk.pl/dataset/c24aa637-3619-4dc2-a171-a23eec8f2172/resource/22313c56-5acf-41c7-a5fd-dc5dc72b3851/download/routes.json"
    try:
        lista_linii_json = requests.get(url_lista_linii)
    except:
        print("Could not download data")

    with open('lista_linii.json', 'w') as out_file:
        json.dump(lista_linii_json.json(), out_file)

    url_lista_stopsInTrip = "https://ckan.multimediagdansk.pl/dataset/c24aa637-3619-4dc2-a171-a23eec8f2172/resource/3115d29d-b763-4af5-93f6-763b835967d6/download/stopsintrip.json"
    try:
        lista_stopsInTrip_json = requests.get(url_lista_stopsInTrip)
    except:
        print("Could not download data")

    with open('lista_stopsInTrip.json', 'w') as out_file:
        json.dump(lista_stopsInTrip_json.json(), out_file)

    lista_przystankow_dict = json.load(open('data/lista_przystankow.json', encoding="utf-8"))
    lista_linii_dict = json.load(open('data/lista_linii.json', encoding="utf-8"))
    lista_stopsInTrip_dict = json.load(open('data/stopsintrip.json', encoding="utf-8"))

    lista_linii = [Linia(line["routeId"], line["routeShortName"], line["routeType"])
                   for line in lista_linii_dict["2023-01-12"]["routes"]]
    lista_przystankow = [Przystanek(stop["stopId"], stop["stopLon"], stop["stopLat"])
                         for stop in lista_przystankow_dict["2023-01-12"]["stops"]]
    lista_stopsInTrip = [StopsInTrip(elem['routeId'], elem['stopId'])
                         for elem in lista_stopsInTrip_dict["2023-01-12"]["stopsInTrip"]]

    [[linia.add_przstanek(przystanek) for przystanek in lista_przystankow if przystanek.stopId == elem.stopID]
     for linia in lista_linii for elem in lista_stopsInTrip if linia.routeID == elem.routeID]

    # for i, linia in enumerate(lista_linii):
    #     fig, ax = plt.subplots()
    #     ax.grid()
    #     for przystanek in lista_przystankow:
    #         ax.plot(przystanek.stopLon, przystanek.stopLat, 'ro')
    #     for przystanek in linia.przystanki_na_linii:
    #         ax.plot(przystanek.stopLon, przystanek.stopLat, 'bo')
    #
    #     plt.title(f"{linia.routeShortName}, {i}")
    #     plt.show()

    return lista_linii
