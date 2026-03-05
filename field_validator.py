from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name            : str
    email           : EmailStr
    age             : int
    weight          : float
    married         : bool
    allergies       : List[str]
    contact_details : Dict[str , str]

    @field_validator('email')
    @classmethod
    def email_validater(cls, value):
        valid_domain = ['vu.edu.pk', 'riphahfsd.edu.pk']
        domain_name = value.split('@')[-1]

        if domain_name not in valid_domain:
            raise ValueError("Not a Valid Domian")
        return value

patient1_info = {
    'name'            : 'Zaid',
    'email'           : 'zaid@vu.edu.pk',
    'age'             : 23,
    'weight'          : 42.1,
    'married'         : 0,
    'allergies'       : ['flou', 'headache'],
    'contact_details' : {'number' : '3062078'}
    }

patient1 = Patient(**patient1_info)

def insert_patient(patient : Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print("Patient Inserted")
insert_patient(patient1)