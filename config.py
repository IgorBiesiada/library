import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'DATABASE_URL',
        'postgresql://postgres:1234@localhost:5432/library'
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False