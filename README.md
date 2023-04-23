# Programm zur Erstellung einer HTML-Datei

Dieses Programm generiert eine HTML-Datei, die eine einfache Webseite darstellt. Die Seite enthält eine Bootstrap-Navigation, die je nach Zustand des Benutzers unterschiedliche Links anzeigt (zum Beispiel "Anmelden" oder "Abmelden"). Darüber hinaus werden auf der Seite eventuelle Fehler- oder Warnmeldungen angezeigt, die dem Benutzer mitgeteilt werden sollen. Die eigentlichen Inhalte der Webseite werden in einem Bereich mit der Klasse "container" angezeigt. Das Programm enthält auch JavaScript-Code, der eine Funktion definiert, um Notizen zu löschen.

## Verwendung

Dieses Programm kann als Vorlage für die Erstellung von HTML-Dateien für Webseiten verwendet werden. Der Code kann einfach in einem beliebigen Texteditor eingegeben werden, und die HTML-Datei kann dann in einem Webbrowser geöffnet werden. Die Bootstrap- und Font Awesome-Bibliotheken, die in der HTML-Datei verlinkt sind, müssen jedoch online verfügbar sein, um ordnungsgemäß geladen zu werden.

Das Programm enthält auch Code für die Handhabung von Flash-Nachrichten, die dazu dienen, dem Benutzer nach bestimmten Aktionen auf der Website Rückmeldungen zu geben. Außerdem enthält es JavaScript-Code zum Löschen einer Notiz auf der Website.

Der Code ist für Flask konzipiert, ein in Python geschriebenes Webanwendungs-Framework.

Die folgenden Ressourcen werden in den Code importiert:
-   [Bootstrap 4.4.1 CSS](https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css)
-   [Font Awesome 4.7.0 CSS](https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css)
-   [jQuery 3.2.1 slim](https://code.jquery.com/jquery-3.2.1.slim.min.js)
-   [Popper.js 1.12.9](https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js)
-   [Bootstrap 4.0.0 JS](https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js)

## Voraussetzungen:
-   [flask](https://flask.palletsprojects.com/en/2.2.x/)
-   [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/)
-   [flask-login](https://flask-login.readthedocs.io/en/latest/)

## Ausführung der App

```bash
python main.py
```

## Anzeigen der App

Gehe zu `http://127.0.0.1:5000`
