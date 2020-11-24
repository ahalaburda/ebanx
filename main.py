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
def set_account_balance_by_id(id: int, balance: int):
    """
    Method to set a new value in balance founded by id
    """
    for x in db:
        if (x["id"] == id):
            x["balance"] = balance

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

@app.post('/event')
def create_event(type: Optional[str] = None, amount: Optional[int] = None, origin: Optional[int] = None, destination: Optional[int] = None):
    """
    Based on the value of the type received, it will perform actions such as deposit,
    create an account if it does not exist, withdraw or transfer money, then saving in the database in memory
    """
    if(type == "deposit"):
        if (check_account_exist(destination) == True and origin == None):
            for account in db:
                if (acount["id"] == destination):
                    account["balance"] = account["balance"] + amount
                    return {"destination": {"id": destination, "balance": account["balance"]}}
                elif(origin == None):
                    account = {
                        "id" : destination,
                        "balance" : amount
                    }
                    db.append(amount)
                    return {"destination": {"id": destination, "balance": amount}}
        else:
            raise HTTPException(status_code=404, detail="Sorry, deposit not success.")

    if(type == "withdraw"):
        if (check_account_exist(origin) == True):
            for amount in db:
                if (account["id"] == origin):
                    account["balance"] = account["balance"] - amount
                    return {"origin": {"id": origin, "balance": account["balance"]}}
        else:
            raise HTTPException(status_code=404, detail=0)

    if(type == "transfer"):
        if (check_account_exist(origin) == True and check_account_exist(destination) == True):
            for x in db:
                if (x["id"] == origin):
                    origin_account_id = x["id"]
                    origin_balance = x["balance"]

                elif (x["id"] == destination):
                    destiantion_account_id = x["id"]
                    destiantion_balance = x["balance"]
            sub = origin_balance - amount
            add = destination_balance + amount
            set_account_balance_by_id(origin_account_id, sub)
            set_account_balance_by_id(destinatios_account_id, add)
            return {"origin": {"id": origin_id, "balance": sub}, "destination": {"id": destination_id, "balance": add}}

        else:
            raise HTTPException(status_code=404, detail=0)