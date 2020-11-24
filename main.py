from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#Database
db=[]


class Balance(BaseModel)>
    id: int
    balance: int

#routes
@app.get('/')
def index():
    """
    Just a Super Friendly method
    """
    return {"Hello": "World"}

@app.post('/reset')
def reset():
    """
    Reset all DB and insert the first account
    """
    db.clear()
    return "OK"



