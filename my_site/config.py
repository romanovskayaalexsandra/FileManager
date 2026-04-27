import os

class Config:
    SECRET_KEY = 'supersecretkey12345'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = 'static/uploads'
    MAX_CONTENT_LENGTH = 5 * 1024 * 1024
