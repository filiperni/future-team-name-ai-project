import requests
import pandas as pd
import json
import shutil
import matplotlib.pyplot as plt


def main():
    url_przebieg_trasy_371 = 'https://ckan2.multimediagdansk.pl/shapes?date=2023-01-15&routeId=10606&tripId=371'
    url_lista_przystankow = 'https://ckan.multimediagdansk.pl/dataset/c24aa637-3619-4dc2-a171-a23eec8f2172/resource/4c4025f0-01bf-41f7-a39f-d156d201b82b/download/stops.json'

    try:
        response = requests.get(url_lista_przystankow)
    except:
        print("Could not download data")    
    
    with open('lista_przystankow.json', 'w') as out_file:
         json.dump(response.json(), out_file)
     
     
        
if __name__ == "__main__":
    main()