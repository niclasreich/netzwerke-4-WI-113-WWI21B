# Programm zur Verwaltung von Notizen

Das vorliegende Programm ist eine Flask-Webanwendung, die es Benutzern ermöglicht, Notizen zu erstellen und zu speichern. Das Programm ist in Python geschrieben und verwendet Flask- und SQLAlchemy-Bibliotheken sowie Flask-Login zur Benutzerverwaltung. Die Webanwendung wird in einer HTML-Datei angezeigt, die mit Bootstrap und Font Awesome gestaltet ist und wird auf einem öffentlich zugänglichen Server gehostet, der mit ngrok bereitgestellt wird. 


## Inhaltsverzeichnis

- [Demo](#demo)

	- [Einleitung](#einleitung)

		- [Oracle Cloud](#oracle-cloud)

		- [Canonical-Ubuntu](#canonical-ubuntu)

		- [Python](#python)

		- [Tmux](#tmux)

		- [Ngrok](#ngrok)

	- [Demo-Logindaten](#demo-logindaten)

	- [Fazit](#fazit)

- [Verwendung](#verwendung)

- [Aufgaben](#aufgaben)

- [Voraussetzungen](#voraussetzungen)

	- [Installieren](#installieren)

- [Ausführung der App](#ausführung-der-app)

	- [Development](#development)

	- [Latest Release](#latest-release)

- [Anzeigen der App](#anzeigen-der-app)

- [Datenbank-Hosting](#datenbank-hosting)

- [App öffentlich verfügbar machen](#app-öffentlich-verfügbar-machen)

- [Applikationsprotokoll](#applikationsprotokoll)

- [API Documentation](#api-documentation)

	- [api_get_notes](#api_get_-_notes)

	- [api_create](#api_create)

	- [api_delete](#api_delete)

	- [api_delete recent](#api_delete-recent)

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

| Zugangsdaten |                                             |
| ------------ | ------------------------------------------- |
| URL          | https://netzwerke.hwr.niclasreich.de/       |
| Benutzername | netzwerke@hwr.berlin                        |
| Passwort     | netzwerke123                                |

Die URL ist die öffentlich zugängliche Adresse der Demo-Webanwendung, während der Benutzername und das Passwort verwendet werden, um sich bei der Anwendung anzumelden.

### Fazit

Insgesamt bietet die Demo-Entwicklungsumgebung eine vollständige Entwicklungs- und Bereitstellungsumgebung, die es uns ermöglicht, leistungsfähige Webanwendungen zu erstellen und auf einem öffentlich zugänglichen Server bereitzustellen. Mit der Verwendung von Oracle Cloud, Canonical-Ubuntu-22.04-aarch64-2023.02.15-0, Python 3.10.6, tmux und ngrok wird die Bereitstellung der Demo-Webanwendung einfach und schnell.

## Verwendung

Die vorliegende Prüfungsaufgabe beschäftigt sich mit der Erstellung einer Flask-Webanwendung, die eine Benutzerverwaltung und die Speicherung von Notizen ermöglicht. Die Anwendung verfügt zudem über eine API, die nach der OpenAPI-Spezifikation beschrieben wurde und auf einer MySQL-Datenbank mit Python und Bootstrap basiert.

Ziel dieser Prüfungsaufgabe / dieses Konstruktionsentwurfs ist es, eine Webapplikation zu erstellen, bei der verschiedene Teile mittels Sockets oder HTTP in einer bestimmten Pro-grammiersprache miteinander kommunizieren. Zudem soll eine API erstellt und durch eine OpenAPI-Spezifikation beschrieben werden. Die Applikation sollte über mindestens einen Backend- und einen Speicherungsteil verfügen, die auf verschiedenen Servern eingesetzt werden. Die Applikation sollte zudem eine einfache Authentifizierungsfunktion bereitstel-len.

## Aufgaben

- [x] Webapplikation (z. B. simpler Chat) erstellen, deren Teile HTTP miteinander kommunizieren
- [x] Applikationsprotokoll
- [x] OpenAPI Spezifikation der API
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

### Installieren

`pip install flask flask_sqlalchemy flask_login flask_swagger_ui sqlalchemy werkzeug pymysql`

## Ausführung der App

### Development

```
git clone https://github.com/niclasreich/netzwerke-4-WI-113-WWI21B.git

cd netzwerke-4-WI-113-WWI21B

python3 main.py
```

### Latest Release

```
git clone --depth 1 --branch $(git ls-remote --tags --refs --sort="v:refname" https://github.com/niclasreich/netzwerke-4-WI-113-WWI21B.git | tail -n1 | awk '{print $2}' | sed 's/refs\/tags\///g') https://github.com/niclasreich/netzwerke-4-WI-113-WWI21B.git

cd netzwerke-4-WI-113-WWI21B

python3 main.py
```

## Anzeigen der App

Gehe zu `http://127.0.0.1:5000`

## Datenbank-Hosting

| Zugangsdaten |                                           |
| ------------ | ----------------------------------------- |
| Server       | mysql2ec5.netcup.net:3306                 |
| Datenbank    | k97841_netzwerke                          |
| Username     | k97841_netzwerke                          |
| Pasaswort    | p32M7aAcvep2jeE                           |

## App öffentlich verfügbar machen

```

pip install pyngrok

ngrok config add-authtoken <<YourToken>> # from https://dashboard.ngrok.com/get-started/setup

ngrok http 5000

```

## Applikationsprotokoll


In der Datei `__init__.py` wird die App-Factory-Funktion `create_app()` definiert, die die Flask-App erstellt und konfiguriert. Es wird eine Geheimhaltungsschlüssel festgelegt, um die Anwendung vor Angriffen zu schützen. Außerdem wird eine MySQL-Datenbank festgelegt und eine Verbindung zur Datenbank hergestellt. Die Flask-Blueprints für die verschiedenen Teile der Anwendung werden registriert und die Datenbank wird initialisiert. Ein Login-Manager wird ebenfalls initialisiert und die Login-View wird festgelegt.

In der Datei `views.py` werden die Routen für die verschiedenen Seiten der Anwendung definiert. Die Route `'/'` stellt die Hauptseite der Anwendung dar, auf der Benutzer ihre Notizen anzeigen und neue Notizen erstellen können. Wenn ein Benutzer eine neue Notiz erstellt, wird sie in der Datenbank gespeichert. Die Route '/delete-note' wird verwendet, um eine vorhandene Notiz zu löschen.

In der Datei `models.py` werden die Datenbankmodelle für Benutzer und Notizen definiert. Das Notiz-Modell hat eine ID, den Inhalt der Notiz, das Erstellungsdatum und eine Fremdschlüsselbeziehung zum Benutzer, dem die Notiz gehört. Das Benutzermodell hat eine ID, eine E-Mail-Adresse, ein Passwort und den Vornamen des Benutzers sowie eine Beziehung zu den Notizen des Benutzers.

In der Datei `auth.py` definiert der Code Routen für die Benutzerauthentifizierung. Der Code verwendet die Blueprint-Klasse von Flask, um ein separates Modul zu definieren, das in die Flask-App importiert und registriert werden kann. Die Route `/login` nimmt eine GET- oder POST-Anfrage entgegen. Bei einer POST-Anfrage prüft der Code, ob die E-Mail und das Passwort des Benutzers mit einem Datensatz in der Datenbank übereinstimmen. Wenn die E-Mail-Adresse und das Passwort des Benutzers übereinstimmen, meldet der Code den Benutzer an und speichert ein Cookie in seinem Browser. Wenn sie nicht übereinstimmen, wird der Benutzer über den Fehler informiert. Bei einer GET-Anfrage wird dem Benutzer die Anmeldeseite angezeigt. Die `/logout`-Route meldet den Benutzer ab, indem sie sein Cookie entfernt. Die `/sign-up`-Route nimmt eine GET- oder POST-Anfrage entgegen. Bei einer POST-Anfrage prüft der Code, ob die E-Mail, der Vorname und das Passwort des Benutzers bestimmte Kriterien erfüllen. Wenn die E-Mail bereits verwendet wurde oder die Mindestlänge nicht erfüllt, oder wenn der Vorname nicht der Mindestlänge entspricht, oder wenn die Passwörter nicht übereinstimmen oder nicht der Mindestlänge entsprechen, wird dem Benutzer eine Fehlermeldung angezeigt. Andernfalls wird ein neuer Benutzer angelegt und eingeloggt. Bei einer GET-Anfrage wird dem Benutzer die Anmeldeseite angezeigt.

In der Datei `api.py` definiert der Code Routen zum Erstellen und Abrufen von Notizen über eine API. Die Routen werden ebenfalls mithilfe der Blueprint-Klasse von Flask definiert. Die Route `/api/request/` nimmt eine GET-Anfrage mit Parametern für den Benutzernamen und das Passwort entgegen. Der Code prüft, ob der Benutzername und das Passwort mit einem Datensatz in der Datenbank übereinstimmen. Wenn sie übereinstimmen, ruft der Code alle mit diesem Benutzer verbundenen Notizen ab und gibt eine JSON-Antwort mit den Notizdaten zurück. Wenn sie nicht übereinstimmen, wird eine Fehlermeldung zurückgegeben. Die `/api/create/`-Route nimmt eine GET- oder POST-Anfrage mit Parametern für den Benutzernamen, das Passwort und die Notiz entgegen. Der Code prüft, ob der Benutzername und das Kennwort mit einem Datensatz in der Datenbank übereinstimmen. Wenn sie übereinstimmen und die Notiz nicht leer ist, wird eine neue Notiz erstellt und mit dem Benutzer verknüpft. Wenn der Benutzername oder das Kennwort falsch sind oder die Notiz leer ist, wird eine Fehlermeldung zurückgegeben.

Insgesamt bietet die Anwendung eine einfache Möglichkeit für Benutzer, Notizen zu erstellen und zu verwalten. Durch die Verwendung von Flask-Login und SQLAlchemy ist es sicher und robust, und es bietet eine gute Grundlage für die Erweiterung der Funktionalität in der Zukunft.

## API Documentation

Diese API unterstützt [OpenAPI](https://www.openapis.org/). Die Dokumentation kann unter `/api/docs/` aufgerufen werden. Die zugehörige Datei kann auch unter `/api/openapi.json` als JSON-Datei heruntergeladen bzw. im Ordner `/website/static` angesehen werden.

### api_get_notes

Alle Notizen eines Benutzers abrufen.

**Schnittstelle**

GET `/api/request/`

**Parameter**

- `username` (string, required) - User email.

- `password` (string, required) - User password.

**Beispiel**

`/api/request/?username=netzwerke%40hwr.berlin&password=netzwerke123`

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
