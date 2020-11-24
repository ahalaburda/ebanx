from typing import Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI()

#Database
db=[]


class Balance(BaseModel):
    id: int
    balance: int


def check_account_exist(id: int):
    """
    Check if the account id exists registered in the database.
    """
    for x in db:
        if (x["id"] == id):
            return True


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

@app.get('/balance')
def get_balance(account_id: Optional[int] = None):
    """
    Get data from balance model using ID account as a parameter.
    """
    if (check_account_exist(account_id) == True):
        for x in db:
            value = x["balance"]
        return value
    else:
        raise HTTPException(status_code=404, detail=0)

