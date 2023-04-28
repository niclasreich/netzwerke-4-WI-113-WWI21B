from flask import *
from flask_login import login_user
from werkzeug.security import check_password_hash
from .models import User, Note
from . import db
import json

api = Blueprint('api', __name__)

@api.route('/api/', methods=['GET'])
# example URL: /api/
def api_home():
    """
    Does just load a basic homepage.
    """
    data_set = {'Page': 'Home', 'Status': 200, 'Nachricht': 'Die Homepage wurde erfolgreich geladen!'}
    json_dump = json.dumps(data_set)
    return json_dump, 200

@api.route('/api/request/', methods=['GET'])
# example URL: /api/request/
# api does not check for username and password, simply puts given username and password into the json response
def api_request():
    """
    Simply puts given username and password into the json response.
    """
    username = str(request.args.get('username'))
    password = str(request.args.get('password'))
    data_set = {'Page': 'API Request', 'Status': 200, 'Nachricht': 'Die Homepage wurde erfolgreich geladen!', 'Username': username, 'Password': password}
    json_dump = json.dumps(data_set)
    return json_dump, 200

@api.route('/api/create/', methods=['GET', 'POST'])
# example URL: /api/create/?username=LeonKohl%40test123.de&password=7044691640&note=Test%20Notiz
def api_create():
    """
    Create a new note.
    """
    username = str(request.args.get('username'))
    password = str(request.args.get('password'))
    note = str(request.args.get('note'))
    user = User.query.filter_by(email=username).first()
    if user:  # check if user exists
        if check_password_hash(user.password, password):  # check if password is correct
            if len(note) < 1:  # check if note is empty
                data_set = {'Page': 'API Create Note', 'Status': 400, 'Nachricht': 'Bad Request (Notiz ist leer)'}
                json_dump = json.dumps(data_set)
                return json_dump, 400
            else:  # create note if note is not empty
                login_user(user)
                new_note = Note(data=note, user_id=user.id)
                db.session.add(new_note)
                db.session.commit()
                data_set = {'Page': 'API Create Note', 'Status': 201, 'Nachricht': 'Created (Notiz erfolgreich erstellt)'}
                json_dump = json.dumps(data_set)
                return json_dump, 201
        else:  # return error if password is incorrect
            data_set = {'Page': 'API Create Note', 'Status': 401, 'Nachricht': 'Unauthorized (Das Passwort ist falsch)'}
            json_dump = json.dumps(data_set)
            return json_dump, 401
    else:  # return error if user does not exist
        data_set = {'Page': 'API Create Note', 'Status': 401, 'Nachricht': 'Unauthorized (Benutzer existiert nicht)'}
        json_dump = json.dumps(data_set)
        return json_dump, 401
    
@api.route('/api/call/', methods=['GET'])
# example URL: /api/call/?username=LeonKohl%40test123.de&password=7044691640
def api_get_notes():
    """
    Get all notes from a user.
    """
    username = str(request.args.get('username'))
    password = str(request.args.get('password'))
    user = User.query.filter_by(email=username).first()
    if user:  # check if user exists
        if check_password_hash(user.password, password):  # check if password is correct
            notes = Note.query.filter_by(user_id=user.id).all()  # retrieve all notes for the user
            note_list = []  # create a list of dictionaries representing the notes
            for note in notes:
                note_dict = {'id': note.id, 'data': note.data, 'date': note.date.strftime('%Y-%m-%d %H:%M:%S')}
                note_list.append(note_dict)
            if len(note_list) < 1:  # check if note list is empty
                data_set = {'Page': 'API Get Notes', 'Status': 204, 'Nachricht': 'No Content (Keine Notizen vorhanden)'}
                json_dump = json.dumps(data_set)
                return json_dump  # , 204 --> 204 does not work with json.dumps
            else:  # return note list if note list is not empty
                data_set = {'Page': 'API Get Notes', 'Status': 200, 'Message': 'OK', 'Notes': note_list}
                json_dump = json.dumps(data_set)
                return json_dump
        else:  # return error if password is incorrect
            data_set = {'Page': 'API Get Notes', 'Status': 401, 'Nachricht': 'Unauthorized (Das Passwort ist falsch)'}
            json_dump = json.dumps(data_set)
            return json_dump, 401
    else:  # return error if user does not exist
        data_set = {'Page': 'API Get Notes', 'Status': 401, 'Nachricht': 'Unauthorized (Benutzer existiert nicht)'}
        json_dump = json.dumps(data_set)
        return json_dump, 401