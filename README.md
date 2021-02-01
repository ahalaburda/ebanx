# ebanx-home-assignment

This is my submission to the EBANX home assignment during the inteview process.

## Instalation

Made with [FastAPI](https://fastapi.tiangolo.com/), so you need to install first Python 3 and pip to later install all the necessaries dependencies, if you have installed just run
```
pip install -r requiremets.txt
```
then, next run the project

```
uvicorn main:app --reload
```
and with that just enjoy.


Implement the following API in the simplest way you can:


#### Reset state before starting tests
POST /reset
200 OK

#### Get balance for non-existing account
GET /balance?account_id=1234
404 0

#### Create account with initial balance
POST /event {"type":"deposit", "destination":"100", "amount":10}
201 {"destination": {"id":"100", "balance":10}}

#### Deposit into existing account
POST /event {"type":"deposit", "destination":"100", "amount":10}
201 {"destination": {"id":"100", "balance":20}}

#### Get balance for existing account
GET /balance?account_id=100
200 20

#### Withdraw from non-existing account
POST /event {"type":"withdraw", "origin":"200", "amount":10}
404 0

#### Withdraw from existing account
POST /event {"type":"withdraw", "origin":"100", "amount":5}
201 {"origin": {"id":"100", "balance":15}}

#### Transfer from existing account
POST /event {"type":"transfer", "origin":"100", "amount":15, "destination":"300"}
201 {"origin": {"id":"100", "balance":0}, "destination": {"id":"300", "balance":15}}

#### Transfer from non-existing account
POST /event {"type":"transfer", "origin":"200", "amount":15, "destination":"300"}
404 0

Where:

Durability IS NOT a requirement, that is, you don’t need to use a database or persistence mechanism.
The main goal of this exercise is to create a common ground to conduct the interview process.
The API consists of two endpoints, GET /balance, and POST /event. Using your favorite programming language, build a system that can handle those requests, publish it on the internet, and test it using our automated test suite.
Keep in mind that:

There is no hidden agenda, if you code passes the tests, and you are happy about it: you are done;
Pay attention to the package/directory structure, naming and encapsulation;
Separate your business logic from the HTTP transport layer;
Keep your code simple, do not try to anticipate anything that is not part of the spec;
Keep your code malleable, we may ask for modifications;
AGAIN, Keep your code malleable, we may ask for modifications;
Use version control, we would love to see your step-by-step process;
Take your time, don’t rush it;
