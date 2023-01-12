import json
from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def root(x:float=0,y:float=0):



    #kod pyhon tutaj

    print(x,y)


    return {"message": "Hello World"}