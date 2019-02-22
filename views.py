from utils import *
from models import *
from app import app
from flask import session, request, render_template, url_for, redirect
from datetime import datetime
import json

@app.route("/login", methods=['POST'])
def loginAlumno():
        alumno = Alumno.query.filter_by(usuarioAlumno=request.form['uname'], contrasena=request.form['psw']).first()
        if alumno:
                session['USER'] = request.form['uname']
                response = {}
                response['status'] = 'Login Successful'
                response['auth_token'] = encode_auth_token(request.form['uname'], app).decode()
                return json.dumps(response), 201
        else:
                response = {}
                response['status'] = 'Login Failed'
                return response, 403

@app.route("/getInfo", methods=['GET'])
def getInfo():
        token = request.headers.get('Authorization').replace('Bearer ', '')
        print(token)
        auth = decode_auth_token(token, app)
        response = {}
        print(auth)
        if auth == 'exp':
            response['status'] = 'Signature expired.'
            return json.dumps(response), 403
        elif auth == 'inv':
            response['status'] = 'Invalid token. Please log in again.'
            return json.dumps(response), 403
        elif auth == session['USER']:
            alumnos = Alumno.query.all()
            response = {}
            lista = []
            for alumno in alumnos:
                temp = {}
                temp['id'] = alumno.idAlumno
                temp['user'] = alumno.usuarioAlumno
                temp['password'] = alumno.contrasena
                temp['name'] = alumno.nombre
                temp['career'] = alumno.carrera
                lista.append(temp)
            response['students'] = lista
            response['requester'] = session['USER']
            response['time of transaction'] = str(datetime.now())
            return json.dumps(response)
