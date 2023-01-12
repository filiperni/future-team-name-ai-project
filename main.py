import json
from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def root():



    #kod pyhon tutaj




    return {"message": "Hello World"}