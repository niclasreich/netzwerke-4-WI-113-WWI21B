# Programm zur Erstellung einer HTML-Datei

![Generic badge](https://img.shields.io/static/v1?label=Attention&message=This%20needs%20work&color=orange)

Dieses Programm generiert eine HTML-Datei, die eine einfache Webseite darstellt. Die Seite enthält eine Bootstrap-Navigation, die je nach Zustand des Benutzers unterschiedliche Links anzeigt (zum Beispiel "Anmelden" oder "Abmelden"). Darüber hinaus werden auf der Seite eventuelle Fehler- oder Warnmeldungen angezeigt, die dem Benutzer mitgeteilt werden sollen. Die eigentlichen Inhalte der Webseite werden in einem Bereich mit der Klasse "container" angezeigt. Das Programm enthält auch JavaScript-Code, der eine Funktion definiert, um Notizen zu löschen.

## Demo

### Einleitung

Die vorliegende Dokumentation bietet eine Übersicht über die verwendete Software und deren Konfiguration für die Demo. Die Demo-Entwicklungsumgebung basiert auf Oracle Cloud, Canonical-Ubuntu-22.04-aarch64-2023.02.15-0 als Image, Python 3.10.6 als Programmiersprache, tmux als Terminal-Multiplexer und ngrok als Reverse-Proxy.

#### Oracle Cloud

Oracle Cloud ist eine Cloud Computing-Plattform, die eine umfassende Palette von Cloud-Diensten für Unternehmen bietet. In der Demo wird Oracle Cloud verwendet, um die Server-Infrastruktur bereitzustellen.

#### Canonical-Ubuntu

Canonical-Ubuntu-22.04-aarch64-2023.02.15-0 ist das verwendete Betriebssystem-Image für die Demo-IDE. Es basiert auf Ubuntu 22.04 und ist für die ARM-Architektur optimiert.

#### Python

Python 3.10.6 ist die Programmiersprache, die für die Entwicklung der Demo-Software verwendet wurde. Python ist eine leistungsstarke, flexible und einfach zu erlernende Sprache, die für eine Vielzahl von Anwendungen geeignet ist.

#### Tmux

Tmux ist ein Terminal-Multiplexer, der es Benutzern ermöglicht, mehrere virtuelle Konsolen in einem einzigen Terminal-Fenster zu erstellen. Dies ist besonders nützlich für Entwickler, die mehrere Prozesse gleichzeitig ausführen müssen.

#### Ngrok

Ngrok ist ein Reverse-Proxy, der es Benutzern ermöglicht, lokale Webanwendungen über das Internet zugänglich zu machen. Dies ist besonders nützlich für Demos, da Entwickler ihre Anwendungen ohne Aufwand auf einem öffentlich zugänglichen Server bereitstellen können.

### Demo-Logindaten

Die Demo-Logindaten sind wie folgt:

| Zugangsdaten |                                             |
| ------------ | ------------------------------------------- |
| URL          | https://9a27-130-61-149-222.ngrok-free.app/ |
| Benutzername | netzwerke@hwr.berlin                        |
| Passwort     | netzwerke123                                |

URL: [https://9a27-130-61-149-222.ngrok-free.app/](https://9a27-130-61-149-222.ngrok-free.app/)
Benutzername: 
Passwort: netzwerke123

Die URL ist die öffentlich zugängliche Adresse der Demo-Webanwendung, während der Benutzername und das Passwort verwendet werden, um sich bei der Anwendung anzumelden.

### Fazit

Insgesamt bietet die Demo-Entwicklungsumgebung eine vollständige Entwicklungs- und Bereitstellungsumgebung, die es uns ermöglicht, leistungsfähige Webanwendungen zu erstellen und auf einem öffentlich zugänglichen Server bereitzustellen. Mit der Verwendung von Oracle Cloud, Canonical-Ubuntu-22.04-aarch64-2023.02.15-0, Python 3.10.6, tmux und ngrok wird die Bereitstellung der Demo-Webanwendung einfach und schnell.

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

- [pymsql](https://pypi.org/project/pymysql/) - Dieses Paket enthält eine reine Python-MySQL-Client-Bibliothek, die auf PEP 249 basiert.

Installieren:

`pip install flask flask_sqlalchemy flask_login sqlalchemy werkzeug pymysql`

## Ausführung der App

`python main.py`

## Anzeigen der App

Gehe zu `http://127.0.0.1:5000`

## Datenbank-Hosting

| Zugangsdaten |                                           |
| ------------ | ----------------------------------------- |
| Datenbank    | https://www.freemysqlhosting.net/account/ |
| E-Mail       | owq03838@zslsz.com                        |
| Pasaswort    | owq03838@zslsz.com                        |
| phpmyadmin   | https://www.phpmyadmin.co/                |
| Server       | sql7.freemysqlhosting.net                 |
| Name         | sql7615055                                |
| Username     | sql7615055                                |
| Pasaswort    | dHH854eHaL                                |
| Port         | 3306                                      |

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

`/api/call/?username=netzwerke%40hwr.berlin&password=netzwerke123`

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

`/api/create/?username=netzwerke%40hwr.berlin&password=netzwerke123&note=Test%20Notiz`

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

`/api/delete/?username=netzwerke%40hwr.berlin&password=netzwerke123`

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

`/api/delete-recent/?username=netzwerke%40hwr.berlin&password=netzwerke123`

**Antwort**

- `Page` (string) - Page name.

- `Status` (int) - HTTP Antwort status code.

- `Nachricht` (string) - Message.
