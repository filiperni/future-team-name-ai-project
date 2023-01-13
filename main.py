import json
from fastapi import FastAPI
from funkcje import znajdz_linie


app = FastAPI()


@app.get("/")
async def root(posAx:float=0,posAy:float=0,posBx:float=0,posBy:float=0):


    #kod pyhon tutaj

    
    
    
    
    wynik = znajdz_linie()


    #najblizsze przystanki
    #najblizsze_przystanki= get_najb_przystanki(posAx,posAy,posBx,posBy)

    #dok



    return {"message": "Hello World","najblizsze_przystanki":"wynik"}