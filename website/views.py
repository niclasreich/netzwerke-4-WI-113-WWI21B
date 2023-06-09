from flask import Blueprint, render_template, request, flash, jsonify, send_from_directory
from flask_login import login_required, current_user
from .models import Note
from . import db
import json


views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required # Nur angemeldete Benutzer können auf diese Route zugreifen
def home():
    if request.method == 'POST':
        note = request.form.get('note')
        if len(note) < 1:
            flash("Notiz ist leer!", category='warning')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash("Notiz hinzugefügt!", category='success')

    return render_template("home.html", user=current_user)

@views.route('delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
            flash('Notiz gelöscht.', category='success')

    return jsonify({})

@views.route('/api/openapi.json')
def openapi():
    return send_from_directory('static', 'openapi.json')