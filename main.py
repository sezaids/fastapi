from fastapi import FastAPI, Path, HTTPException, Query
from pydantic import BaseModel, Field
from typing import Annotated, Literal
import json

app = FastAPI()

class Patient(BaseModel):

    id : Annotated[str, Field(..., description="ID of Patient", examples=['P001','P002'])]
    name : Annotated[str, Field(..., description='Patient\'s Name', examples=['Zaid Sohail'])]
    city : Annotated[str, Field(..., description='City Name', examples=['Dhaka', 'Dehli'])]
    age : Annotated[int, Field(..., gt=0, lt=120, description='Your age', examples=[18,22,90])]
    gender : Annotated[Literal['male', 'female', 'other'], Field(..., description='Gender of the patient')]
    height : Annotated[float, Field(..., gt=0, description='Height of the Patient in Meters')]
    weight : Annotated[float, Field(..., gt=0, description='Weight of the Patient in Kilograms')]


def load_data():
    with open("patients.json", 'r') as f:
        data = json.load(f)
    return data

@app.get("/")
def hello():
    return {'message' : 'Hello World'}

@app.get("/zaid")
def hello():
    return {'message' : 'My name is Zaid'}

@app.get("/view")
def view():
    data = load_data()
    return data

@app.get('/patient/{patients_id}')
def patient(patients_id : str = Path(..., description = 'ID of the Patient in the DB', example = 'p001')):
    data = load_data()
    if patients_id in data:
        return data[patients_id]
    raise HTTPException(status_code=404, details = 'Patient not Found')

@app.get('/sort')
def sort_patients(sort_by : str = Query(..., description='Sort by basis of height, weight'), order : str = Query('asc', description='sort in asc order or desc order')):
    valid_fields = ['height', 'weight', 'bmi']
    order_fields = ['asc', 'desc']

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail= f'Invalid field select from {valid_fields}')
    
    if order not in order_fields:
        raise HTTPException(status_code=400, detail=f'invalid order select from {order_fields}')

    data = load_data()
    sort_order = True if order =='desc' else False
    sorted_data = sorted(data.values(), key=lambda x:x.get(sort_by, 0), reverse=sort_order)
    return sorted_data