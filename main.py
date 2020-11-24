from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#Database
db=[]


class Balance(BaseModel)>
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

