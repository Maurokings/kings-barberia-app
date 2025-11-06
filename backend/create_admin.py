
# Script to create an admin user (run locally)
from sqlmodel import SQLModel, create_engine, Session, select
from app.models import Usuario
from app.crud import get_password_hash
import os, sys

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./kings.db")
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {})

def create_admin(username, password):
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        user = session.exec(select(Usuario).where(Usuario.username == username)).first()
        if user:
            print("Usuario ya existe")
            return
        admin = Usuario(username=username, password_hash=get_password_hash(password), nombre="Administrador", rol="admin")
        session.add(admin)
        session.commit()
        print("Admin creado:", username)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python create_admin.py username password")
    else:
        create_admin(sys.argv[1], sys.argv[2])
