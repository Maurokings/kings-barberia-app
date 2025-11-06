
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlmodel import Session, select
from .models import Usuario
from .main import engine
from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import JWTError, jwt
import os

router = APIRouter()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
SECRET_KEY = os.getenv("SECRET_KEY", "secret_kings_dev_change")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "10080"))

class Token(BaseModel):
    access_token: str
    token_type: str

class LoginIn(BaseModel):
    username: str
    password: str

def verify_password(plain_password, hashed):
    return pwd_context.verify(plain_password, hashed)

@router.post("/login", response_model=Token)
def login(data: LoginIn):
    with Session(engine) as session:
        user = session.exec(select(Usuario).where(Usuario.username == data.username)).first()
        if not user or not verify_password(data.password, user.password_hash):
            raise HTTPException(status_code=401, detail="Usuario o contraseña inválidos")
        to_encode = {"sub": user.username, "rol": user.rol}
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expire})
        token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return {"access_token": token, "token_type": "bearer"}

@router.get("/me")
def me(token: str = Depends(lambda: None)):
    return {"msg":"use client-side token"}
