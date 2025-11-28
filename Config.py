from pathlib import Path

BASE = Path(__file__).resolve().parent

class Config:
    SECRET_KEY = "cambia_esta_clave"
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{BASE/'db.sqlite3'}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
