# Kursplaner der Skischule

## Diese Anwendung wurde Entwickelt um die Planung der Kurse zu automatisieren

Es werden Anhand der gepflegten Verfügbarkeiten automatisch neue Kurse erstellt oder bestehende Kurse aufgefüllt.

### Todo


post_save der Classes -> wenn ein Kurs mit lehrer Created wurde, dann muss der timeslot für den Leherer geblockt werden.

es muss eine Verfügbarkeits-eingabe-view erstellt werden

es muss ein Interface für die Counter geschaffen werden.
    - Neue Kunden anlegen oder alte Kunden finden
    - Kurse für die Kunden anlegen


1. Find / Create Customer
2. Select Time and Class Type
3a. Get Variety of alvailable teachers to select from
3b. Get Shown which course was created for the selection


es muss das Skillevel der Kunden automatisch erhöht werden, wenn sie einen Kurs absolvieren.
    - Beginner Kurs belegt in der Vergangenheit -> Skill auf dem Sportgerät wird auf Level_1 gesetzt

es muss für die Skileherer ersichtlich sein, welche Kurse für sie an Tag X geplant wurden.

Wer hat die Kunden angenommen/gebucht mit speichern.

beim buchen der Kurse wird bereits gezeigt wie die verfügbarkeit ist.
    - grün = save Lehrer vorhanden um den Kurs zu geben
    - gelb = unklar ob die Anzahl der Lehrer da ist
    - rot = keine Lehrer / nur Notfall als Verfügbarkeit



### Feature Creep

Auswertung der gegebenen Stunden für Skilehrer

### Development

Install dependencies
`pip3 install --upgrade pip pip-tools && pip-compile --upgrade && pip3 install -r requirements.txt`

Setup DB
if you have a local mysql container running create a schema named `kursplaner`

else change the DB-Setup in `kursplaner/settings.py`
```py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'mydatabase', # This is where you put the name of the db file. 
                 # If one doesn't exist, it will be created at migration time.
    }
}
```

`python3 manage.py migrate`


Run Development Server
`python3 manage.py runserver`