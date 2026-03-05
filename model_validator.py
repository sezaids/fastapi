from pydantic import BaseModel, EmailStr, AnyUrl, Field, model_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name            : str
    email           : EmailStr
    age             : int
    weight          : float
    married         : bool
    allergies       : List[str]
    contact_details : Dict[str , str]

    @model_validator(mode='after')
    def validate_emergency_number(cls, model):
        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError("Patient is 60+ age so emergency number is important.")
        return model

patient1_info = {
    'name'            : 'Zaid',
    'email'           : 'zaid@vu.edu.pk',
    'age'             : 6,
    'weight'          : 42.1,
    'married'         : 0,
    'allergies'       : ['flou', 'headache'],
    'contact_details' : {'number' : '3062468', 'emergency' : '03124567890'}
    }

patient1 = Patient(**patient1_info)

def insert_patient(patient : Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print("Patient Inserted")
insert_patient(patient1)