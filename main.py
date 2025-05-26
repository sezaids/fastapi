from fastapi import FastAPI

app = FastAPI()
@app.get("/")
def data1():
    return {"message":"Hello world!"}

@app.get("/api")
def data2():
    return [
        {
            "name" : "adil",
            "age" : 23,
            "class" : "MS AI"
        },
        {
            "name" : "adil2",
            "age" : 23,
            "class" : "MS AI"
        },
        {
            "name" : "adil1",
            "age" : 231,
            "class" : "MS AI"
        }
    ]