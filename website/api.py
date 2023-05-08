from flask import Blueprint, request, jsonify
from flask_login import login_user
from werkzeug.security import check_password_hash
from .models import User, Note
from . import db

api = Blueprint('api', __name__)

OK = {'Page': 'API', 'Status': 200, 'Message': 'OK'}
CREATED = {'Page': 'API', 'Status': 201, 'Message': 'Created'}
NO_CONTENT = {'Page': 'API', 'Status': 204, 'Message': 'No Content'}
BAD_REQUEST = {'Page': 'API', 'Status': 400, 'Message': 'Bad Request'}
UNAUTHORIZED = ({'Page': 'API', 'Status': 401, 'Message': 'Unauthorized'}, {'error': 'Username-Passwort-Kombination existiert nicht'})
NOT_ACCEPTABLE = {'Page': 'API', 'Status': 406, 'Message': 'Not Acceptable'}


@api.route('/api/request/', methods=['GET'])
def api_get_notes():
    """
    Alle Notizen eines Benutzers abrufen.
    Example GET: /api/request/?username=netzwerke%40hwr.berlin&password=netzwerke123
    """
    username = request.args.get('username')
    password = request.args.get('password')
    user = User.query.filter_by(email=username).first()
    if user:  # check if user exists
        if check_password_hash(user.password, password):  # check if password is correct
            notes = Note.query.filter(Note.user_id == user.id).all()
            note_list = [{'id': note.id, 'data': note.data, 'date': note.date.strftime('%Y-%m-%d %H:%M:%S')} for note in notes]
            if len(note_list) < 1:  # check if user has notes
                return jsonify(NO_CONTENT, {'error': 'Keine Notizen vorhanden'}), 204
            else:  # return notes if user has notes
                return jsonify(OK, {'Notizen': note_list}), 200
    return jsonify(UNAUTHORIZED), 401  # return error if user does not exist or password is incorrect


@api.route('/api/create/', methods=['GET', 'POST', 'DELETE'])
def api_create():
    """
    Eine neue Notiz erstellen.
    Example POST: /api/create/?username=netzwerke%40hwr.berlin&password=netzwerke123&note=Test%20Notiz
    """
    username = request.args.get('username')
    password = request.args.get('password')
    note = str(request.args.get('note'))
    user = User.query.filter_by(email=username).first()
    if user:  # check if user exists
        if check_password_hash(user.password, password):  # check if password is correct
            if len(note) < 1 or note == 'None':  # check if note is empty
                return jsonify(BAD_REQUEST, {'error': 'Notiz ist leer'}), 400
            else:  # create note if note is not empty
                login_user(user)
                new_note = Note(data=note, user_id=user.id)
                db.session.add(new_note)
                db.session.commit()
                return jsonify(CREATED), 201
    return jsonify(UNAUTHORIZED), 401  # return error if user does not exist or password is incorrect


@api.route('/api/delete/', methods=['GET', 'POST', 'DELETE'])
def api_delete():
    """
    Alle Notizen eines Benutzers löschen.
    Example GET: /api/delete/?username=netzwerke%40hwr.berlin&password=netzwerke123
    """
    username = request.args.get('username')
    password = request.args.get('password')
    user = User.query.filter_by(email=username).first()
    if user:  # check if user exists
        if check_password_hash(user.password, password):  # check if password is correct
            notes = Note.query.filter_by(user_id=user.id).all()
            for note in notes:  # delete all notes of user
                db.session.delete(note)
            db.session.commit()
            return jsonify(OK), 200
    return jsonify(UNAUTHORIZED), 401  # return error if user does not exist or password is incorrect


@api.route('/api/delete-recent/', methods=['GET', 'POST'])
def api_delete_recent():
    """
    Löscht die letzte Notiz eines Benutzers.
    Example GET: /api/delete-recent/?username=netzwerke%40hwr.berlin&password=netzwerke123
    """
    username = request.args.get('username')
    password = request.args.get('password')
    user = User.query.filter_by(email=username).first()
    if user:  # check if user exists
        if check_password_hash(user.password, password):  # check if password is correct
            most_recent_note = Note.query.filter_by(
                user_id=user.id).order_by(Note.date.desc()).first()
            if most_recent_note:  # check if user has notes
                db.session.delete(most_recent_note)
                db.session.commit()
                return jsonify(OK), 200
            else:  # return error if user has no notes
                return jsonify(NOT_ACCEPTABLE, {'error': 'Keine Notizen vorhanden'}), 406
    return jsonify(UNAUTHORIZED), 401  # return error if user does not exist or password is incorrect