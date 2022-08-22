from typing import Optional
from pydantic import BaseModel
from fastapi import FastAPI
from fastapi import Body

app = FastAPI()

#Models
class Person(BaseModel):
    first_name: str
    last_name: str
    age: int
    hair_color: Optional[str] = None
    is_married: Optional[bool] = None

# Path Parameters
# Query Parameters
# "/tweets/{tweet_id}/details?age=30&height=184"
@app.get('/')
def home():
    message = 'Hola Mundo'
    print(message)
    return {'message': message}


#Request and reponse body
@app.post('/persons')
def create_person(person: Person = Body(...)):

    return person