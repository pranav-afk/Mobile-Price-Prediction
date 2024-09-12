from fastapi import FastAPI, Request,Form
from fastapi.responses import HTMLResponse
from model.model import Mob
from config.db import conn
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
import pickle
import pandas
import numpy as np

app = FastAPI()
templates = Jinja2Templates(directory="templates")
pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)


@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/")
async def create_item(request: Request):
    form = await request.form()
    formDict=dict(form)
    # Mob = conn.notes.notes.insert_one(formDict) If you want to add data to your MongoDB database then you can use this
    battery=int(formDict["battery"])
    weight=int(formDict["weight"])
    sale=int(formDict["sale"])
    prediction = classifier.predict([[sale,weight,battery]])
    print(prediction)
    return templates.TemplateResponse("index.html", {"request": request, "prediction": prediction})


