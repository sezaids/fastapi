from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name : Annotated[str, Field(max_length=50, title="Enter patient name", description='name should be less than 51 char', examples=['Zaid','Fatima'])]
    email : EmailStr
    url : AnyUrl
    age : int = Field(gt = 0, lt = 120)
    weight : Annotated[float, Field(strict=True, gt = 0)]
    married : bool
    allergies : Optional[List[str]] = None
    contact_details : Dict[str , str]

patient1_info = {'name' : 'Zaid', 'email' : 'zaid@gmail.com', 'url' : 'https://linkedin.com/in/', 'age' : 23, 'weight' : 42.1, 'married' : 0, 'contact_details' : {'number' : '3062078'}}
patient1 = Patient(**patient1_info)

def insert_patient(patient : Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print("Patient Inserted")
insert_patient(patient1)