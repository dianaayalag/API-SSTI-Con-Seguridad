from app import app
import os

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://diana:1234@localhost:5432/postgres'
app.secret_key = b'\xf9\xe4p(\xa9\x12\x1a!\x94\x8d\x1c\x99l\xc7\xb7e\xc7c\x86\x02MJ\xa0'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
