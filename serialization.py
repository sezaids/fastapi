from pydantic import BaseModel

class Patient_Address(BaseModel):
    city : str
    state : str
    pin : str

class Patient(BaseModel):
    name : str
    gender : str
    age : int
    address : Patient_Address

address_info = {'city' : 'Gojra', 'state' : 'Punjab', 'pin' : '36120'}
address_1 = Patient_Address(**address_info)

patient_info = {'name' : 'Fatima', 'gender' : 'Female', 'age' : '23', 'address' : address_1}
patient_1 = Patient(**patient_info)

temp = patient_1.model_dump(exclude_unset= True)

print(temp)
print(type(temp))