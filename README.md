# Programm zur Erstellung einer HTML-Datei

![Generic badge](https://img.shields.io/static/v1?label=Attention&message=This%20needs%20work&color=orange)

Dieses Programm generiert eine HTML-Datei, die eine einfache Webseite darstellt. Die Seite enthält eine Bootstrap-Navigation, die je nach Zustand des Benutzers unterschiedliche Links anzeigt (zum Beispiel "Anmelden" oder "Abmelden"). Darüber hinaus werden auf der Seite eventuelle Fehler- oder Warnmeldungen angezeigt, die dem Benutzer mitgeteilt werden sollen. Die eigentlichen Inhalte der Webseite werden in einem Bereich mit der Klasse "container" angezeigt. Das Programm enthält auch JavaScript-Code, der eine Funktion definiert, um Notizen zu löschen.

## Verwendung

![Generic badge](https://img.shields.io/static/v1?label=Attention&message=This%20needs%20work&color=orange)

Dieses Programm kann als Vorlage für die Erstellung von HTML-Dateien für Webseiten verwendet werden. Der Code kann einfach in einem beliebigen Texteditor eingegeben werden, und die HTML-Datei kann dann in einem Webbrowser geöffnet werden. Die Bootstrap- und Font Awesome-Bibliotheken, die in der HTML-Datei verlinkt sind, müssen jedoch online verfügbar sein, um ordnungsgemäß geladen zu werden.

Das Programm enthält auch Code für die Handhabung von Flash-Nachrichten, die dazu dienen, dem Benutzer nach bestimmten Aktionen auf der Website Rückmeldungen zu geben. Außerdem enthält es JavaScript-Code zum Löschen einer Notiz auf der Website.

Der Code ist für Flask konzipiert, ein in Python geschriebenes Webanwendungs-Framework.

Die folgenden Ressourcen werden in den Code importiert:

- [Bootstrap 4.4.1 CSS](https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css)

- [Font Awesome 4.7.0 CSS](https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css)

- [jQuery 3.2.1 slim](https://code.jquery.com/jquery-3.2.1.slim.min.js)

- [Popper.js 1.12.9](https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js)

- [Bootstrap 4.0.0 JS](https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js)

## Aufgaben

- [x] Webapplikation (z. B. simpler Chat) erstellen, deren Teile mittels Sockets oder HTTP miteinander kommunizieren
- [ ] Applikationsprotokoll
- [ ] OpenAPI Spezifikation Eurer API unter Nutzung von Libraries wie connexion unter Python
- [x] Verteilung von Backend (da wo Logik und API verortet sind) und Speicherungsteil (Datenbank) auf unterschiedlichen Servern
- [x] Applikation enthält eine Authentifizierung

## Voraussetzungen:

- [Flask](https://flask.palletsprojects.com/en/2.2.x/) - Ein Mikro-Web-Framework für Python

- [Flask_SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/) - Eine Erweiterung für Flask, die Unterstützung für SQLAlchemy bietet

- [Flask_Login](https://flask-login.readthedocs.io/en/latest/) - Eine Erweiterung für Flask, die die Verwaltung von Benutzersitzungen ermöglicht

- [SQLAlchemy](https://www.sqlalchemy.org/) - Ein SQL-Toolkit und ORM für Python

- [Werkzeug](https://werkzeug.palletsprojects.com/en/2.3.x/) - Eine Python-Bibliothek für Webanwendungen, die Routing, Anfrage- und Antwortverarbeitung bietet

- [Pyngrok](https://pypi.org/project/pyngrok/) - Ein Python-Wrapper für ngrok, der sein eigenes Binary verwaltet und ngrok über eine komfortable Python-API verfügbar macht.

Installieren:

`pip install flask flask_sqlalchemy flask_login sqlalchemy werkzeug`

## Ausführung der App

`python main.py`

## Anzeigen der App

Gehe zu `http://127.0.0.1:5000`

## Datenbank-Hosting

|            |                                           |
| ---------- | ----------------------------------------- |
| Datenbank  | https://www.freemysqlhosting.net/account/ |
| E-Mail     | owq03838@zslsz.com                        |
| Pasaswort  | owq03838@zslsz.com                        |
| phpmyadmin | https://www.phpmyadmin.co/                |
| Server     | sql7.freemysqlhosting.net                 |
| Name       | sql7615055                                |
| Username   | sql7615055                                |
| Pasaswort  | dHH854eHaL                                |
| Port       | 3306                                      |

## App öffentlich verfügbar machen

```

pip install pyngrok

ngrok config add-authtoken <<YourToken>> # from https://dashboard.ngrok.com/get-started/setup

ngrok http 5000

```

## API Documentation

### api_get_notes

Alle Notizen eines Benutzers abrufen.

**Schnittstelle**

GET `/api/call/`

**Parameter**

- `username` (string, required) - User email.

- `password` (string, required) - User password.

**Beispiel**

`/api/call/?username=LeonKohl%40test123.de&password=7044691640`

**Antwort**

- `Page` (string) - Page name.

- `Status` (int) - HTTP Antwort status code.

- `Nachricht` (string) - Message.

- `Notes` (list) - List of notes.

### api_create

Eine neue Notiz erstellen.

**Schnittstelle**

POST `/api/create/`

**Parameter**

- `username` (string, required) - User email.

- `password` (string, required) - User password.

- `note` (string, required) - Note.

**Beispiel**

`/api/create/?username=LeonKohl%40test123.de&password=7044691640&note=Test%20Notiz`

**Antwort**

- `Page` (string) - Page name.

- `Status` (int) - HTTP Antwort status code.

- `Nachricht` (string) - Message.

### api_delete

Alle Notizen eines Benutzers löschen.

**Schnittstelle**

GET `/api/delete/`

**Parameter**

- `username` (string, required) - User email.

- `password` (string, required) - User password.

**Beispiel**

`/api/delete/?username=LeonKohl%40test123.de&password=7044691640`

**Antwort**

- `Page` (string) - Page name.

- `Status` (int) - HTTP Antwort status code.

- `Nachricht` (string) - Message.

### api_delete_recent

Löscht die letzte Notiz eines Benutzers.

**Schnittstelle**

GET `/api/delete-recent/`

**Parameter**

- `username` (string, required) - User email.

- `password` (string, required) - User password.

**Beispiel**

`/api/delete-recent/?username=LeonKohl%40test123.de&password=7044691640`

**Antwort**

- `Page` (string) - Page name.

- `Status` (int) - HTTP Antwort status code.

- `Nachricht` (string) - Message.
