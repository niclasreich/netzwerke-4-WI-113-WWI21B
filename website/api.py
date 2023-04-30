from flask import Blueprint, request, jsonify
from flask_login import login_user
from werkzeug.security import check_password_hash
from .models import User, Note
from . import db

api = Blueprint('api', __name__)
    
@api.route('/api/call/', methods=['GET'])
def api_get_notes():
    """
    Alle Notizen eines Benutzers abrufen.
    Example GET: /api/call/?username=netzwerke%40hwr.berlin&password=netzwerke123
    """
    username = str(request.args.get('username'))
    password = str(request.args.get('password'))
    user = User.query.filter_by(email=username).first()
    if user:
        if check_password_hash(user.password, password):
            notes = Note.query.filter_by(user_id=user.id).all()
            note_list = []
            for note in notes:
                note_dict = {'id': note.id, 'data': note.data, 'date': note.date.strftime('%Y-%m-%d %H:%M:%S')}
                note_list.append(note_dict)
            if len(note_list) < 1:
                data_set = {'Page': 'API Get Notes', 'Status': 204, 'Nachricht': 'No Content (Keine Notizen vorhanden)'}
                return jsonify(data_set)
            else:
                data_set = {'Page': 'API Get Notes', 'Status': 200, 'Nachricht': 'OK', 'Notes': note_list}
                return jsonify(data_set)
        else:
            data_set = {'Page': 'API Get Notes', 'Status': 401, 'Nachricht': 'Unauthorized (Das Passwort ist falsch)'}
            return jsonify(data_set), 401
    else:
        data_set = {'Page': 'API Get Notes', 'Status': 401, 'Nachricht': 'Unauthorized (Benutzer existiert nicht)'}
        return jsonify(data_set), 401

@api.route('/api/create/', methods=['GET', 'POST'])
def api_create():
    """
    Eine neue Notiz erstellen.
    Example POST: /api/create/?username=netzwerke%40hwr.berlin&password=netzwerke123&note=Test%20Notiz
    """
    username = str(request.args.get('username'))
    password = str(request.args.get('password'))
    note = str(request.args.get('note'))
    user = User.query.filter_by(email=username).first()
    if user:  # check if user exists
        if check_password_hash(user.password, password):  # check if password is correct
            if len(note) < 1:  # check if note is empty
                data_set = {'Page': 'API Create Note', 'Status': 400, 'Nachricht': 'Bad Request (Notiz ist leer)'}
                return jsonify(data_set), 400
            else:  # create note if note is not empty
                login_user(user)
                new_note = Note(data=note, user_id=user.id)
                db.session.add(new_note)
                db.session.commit()
                data_set = {'Page': 'API Create Note', 'Status': 201, 'Nachricht': 'Created (Notiz erfolgreich erstellt)'}
                return jsonify(data_set), 401
        else:  # return error if password is incorrect
            data_set = {'Page': 'API Create Note', 'Status': 401, 'Nachricht': 'Unauthorized (Das Passwort ist falsch)'}
            return jsonify(data_set), 401
    else:  # return error if user does not exist
        data_set = {'Page': 'API Create Note', 'Status': 401, 'Nachricht': 'Unauthorized (Benutzer existiert nicht)'}
        return jsonify(data_set), 401
    
@api.route('/api/delete/', methods=['GET', 'POST'])
def api_delete():
    """
    Alle Notizen eines Benutzers löschen.
    Example GET: /api/delete/?username=netzwerke%40hwr.berlin&password=netzwerke123
    """
    username = str(request.args.get('username'))
    password = str(request.args.get('password'))
    user = User.query.filter_by(email=username).first()
    if user:
        if check_password_hash(user.password, password):
            notes = Note.query.filter_by(user_id=user.id).all()
            for note in notes:
                db.session.delete(note)
            db.session.commit()
            data_set = {'Page': 'API Delete Notes', 'Status': 200, 'Nachricht': 'OK (Alle Notizen erfolgreich gelöscht)'}
            return jsonify(data_set)
        else:
            data_set = {'Page': 'API Delete Notes', 'Status': 401, 'Nachricht': 'Unauthorized (Das Passwort ist falsch)'}
            return jsonify(data_set), 401
    else:
        data_set = {'Page': 'API Delete Notes', 'Status': 401, 'Nachricht': 'Unauthorized (Benutzer existiert nicht)'}
        return jsonify(data_set), 401
    
@api.route('/api/delete-recent/', methods=['GET', 'POST'])
def api_delete_recent():
    """
    Löscht die letzte Notiz eines Benutzers.
    Example GET: /api/delete-recent/?username=netzwerke%40hwr.berlin&password=netzwerke123
    """
    username = str(request.args.get('username'))
    password = str(request.args.get('password'))
    user = User.query.filter_by(email=username).first()
    if user:
        if check_password_hash(user.password, password):
            most_recent_note = Note.query.filter_by(user_id=user.id).order_by(Note.date.desc()).first()
            if most_recent_note:
                db.session.delete(most_recent_note)
                db.session.commit()
                data_set = {'Page': 'API Delete Recent Note', 'Status': 200, 'Nachricht': 'OK (Letzte Notiz erfolgreich gelöscht)'}
                return jsonify(data_set)
            else:
                data_set = {'Page': 'API Delete Recent Note', 'Status': 204, 'Nachricht': 'No Content (Keine Notizen vorhanden)'}
                return jsonify(data_set), 204
        else:
            data_set = {'Page': 'API Delete Recent Note', 'Status': 401, 'Nachricht': 'Unauthorized (Das Passwort ist falsch)'}
            return jsonify(data_set), 401
    else:
        data_set = {'Page': 'API Delete Recent Note', 'Status': 401, 'Nachricht': 'Unauthorized (Benutzer existiert nicht)'}
        return jsonify(data_set), 401