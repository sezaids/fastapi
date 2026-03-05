from pydantic import BaseModel, EmailStr, computed_field
from typing import List, Dict

class Patient(BaseModel):
    name            : str
    email           : EmailStr
    age             : int
    weight          : float
    height          : float
    married         : bool
    allergies       : List[str]
    contact_details : Dict[str , str]

    @computed_field
    @property
    def calc_bmi(self) -> float:
        bmi = round(self.weight/(self.height ** 2),2)
        return bmi


patient1_info = {
    'name'            : 'Zaid',
    'email'           : 'zaid@vu.edu.pk',
    'age'             : 6,
    'weight'          : 75.2,
    'height'          : 1.72,
    'married'         : 0,
    'allergies'       : ['flou', 'headache'],
    'contact_details' : {'number' : '3062468', 'emergency' : '03124567890'}
    }

patient1 = Patient(**patient1_info)

def insert_patient(patient : Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print("BMI : " , patient.calc_bmi)
    print("Patient Inserted")
insert_patient(patient1)