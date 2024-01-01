from fastapi import FastAPI  
# app FastAPI()
app : FastAPI = FastAPI()

# method /hi
@app.get("/hi")
def greet()-> str:
    return "Hello World?"