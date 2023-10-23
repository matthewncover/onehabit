from .main import app
from .models import LoginSchema

from fastapi import HTTPException

def successful_login(username, password):
    if username == 'admin' and password == 'pass':
        return True
    else:
        return False

@app.get("/")
def read_root():
    return {"message": True}

@app.post("/login")
def login(user: LoginSchema):
    username = user.username
    password = user.password
    if successful_login(username, password):
        return {"message": "Login successful"}
    else:
        raise HTTPException(status_code=401, detail="Invalid credentials")
