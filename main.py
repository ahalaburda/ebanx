from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#Database
db=[]


class Balance(BaseModel)>
	id: int
	balance: int

