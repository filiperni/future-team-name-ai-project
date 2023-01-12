import json
from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def root(posAx:float=0,posAy:float=0,posBx:float=0,posBy:float=0):
#async def root(x:float=0,y:float=0):


    #kod pyhon tutaj

    
    
    
    
    print(posAx,posAy,posBx,posBy)



    return {"message": "Hello World"}