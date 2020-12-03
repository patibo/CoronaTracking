import re #Bibliothek regex wird importiert. Ist für die Überprüfung der Eingaben.
import mysql.connector#Bibliothek mysql wird importiert. Ist für die Verbindung zur Datenbank.
import datetime#Bibliothek datetime wird importiert. Ist für die Prüfung vom Geburtsdatum.
import smtplib#Bibliothek smtplib wird importiert. Ist für den Zugriff und versendung der E-Mails zuständig.
import random#Bibliothek random wird importiert.Ist für die 5 Stellige Verefezierung für Passwort zurücksetzen.

class DB:#Hier passiert alles was mit der DB zutun hat
    def __init__(self,user,pswd,host,port,db):#Hier werden die Informationen übergeben die ich für eine DB verbindung brauche
        self.config = {
            'user': user,
            'password': pswd,
            'host': host,
            'port': port,
            'database': db
        }
        self.mydb = None
        self.cur = None
    def connect(self):#eine Verbindung zur DB wird erstellt
        self.mydb = mysql.connector.connect(**self.config)
        self.cur = self.mydb.cursor()
    def insert_kunde(self,benutzername,pswt,vorname,nachname,email,geburtsdatum,telefon):#ein Neuer Kunde wird erstellt
        sql = "INSERT INTO `kunden`(`benutzername`, `passwort`, `vorname`, `nachname`, `email`, `geburtsdatum`, `telefon`) VALUES ('{}','{}','{}','{}','{}','{}','{}')".format(benutzername,pswt,vorname,nachname,email,geburtsdatum,telefon)
        self.cur.execute(sql)
        self.mydb.commit()
    def insert_kundenevent(self,kunden_id,event_id):
        sql="INSERT INTO `kundenevents` (`kID`, `eID`) VALUES ('{}', '{}');".format(kunden_id,event_id)
        self.cur.execute(sql)
        self.mydb.commit()
    def select_pswd(self,benutzername_email):#Hier wird das Passwort zurückgegeben was ich für die Anmeldung brauche
        sql = "SELECT passwort FROM `kunden` WHERE benutzername = '{}' or email = '{}'".format(benutzername_email, benutzername_email)
        self.cur.execute(sql)
        return self.cur.fetchall()
    def select_id(self,benutzername_email,pswd):
        sql = "SELECT id FROM kunden WHERE (`benutzername`='{}' or `email`='{}') and `passwort` = '{}' ".format(benutzername_email,benutzername_email,pswd)
        self.cur.execute(sql)
        return self.cur.fetchall()
    def select_benutzername(self,benutzername):
        sql = "SELECT COUNT(*) FROM kunden WHERE benutzername = '{}' ".format(benutzername)
        self.cur.execute(sql)
        return self.cur.fetchall()
    def select_mail(self,kunden_id,date):
        sql = "SELECT kunden.`email` FROM kunden JOIN kundenevents ON kunden.id=kundenevents.kID JOIN eventsentry on eventsentry.id = kundenevents.eID WHERE kunden.id != {} and eventsentry.datum >='{}'and eventsentry.id IN(SELECT eventsentry.id FROM eventsentry JOIN kundenevents ON eventsentry.id=kundenevents.eID JOIN kunden on kunden.id = kundenevents.kID WHERE kunden.id = {} and eventsentry.datum >='{}')".format(kunden_id,date,kunden_id,date)  
        self.cur.execute(sql)
        return self.cur.fetchall()  
    def select_user_email(self, kunden_id):
        sql = "SELECT `email` FROM kunden WHERE id = {}".format(kunden_id)
        self.cur.execute(sql)
        return self.cur.fetchall() 
    def close(self):#die Verbindung zur DB wird getrennt
        self.cur.close()
        self.mydb.close()
    def eventinsert(self, name, datum, zeit):#Neues Event anlegen
        sql = "INSERT INTO `eventsentry`(`name`, `datum`, `zeit`) VALUES ('{}', '{}', '{}')".format(name, datum, zeit)
        self.cur.execute(sql)
        self.mydb.commit()
    
    def eventoutput(self, name):
        sql = "SELECT * FROM `eventsentry` WHERE `eventsentry`.`name` = '{}'".format(name)
        self.cur.execute(sql)
        return self.cur.fetchall()

class Login:#Hier passiert alles was im hintergrund der Webseite
    def __init__(self):
        self.db = DB('root','root','localhost','8889','coronatracking')#hier kann ich die Klasse DB verwenden bzw. hier wird sie aufgerufen
        self.id = None
    def anmelden(self):#anmelde funktion
        benutzername_email = 'ar'#Eingabefeld für Benutzername bzw. E-Mail
        pswt = 'a'#Eingabefeld für das Passwort
        
        benutzername_email = benutzername_email.strip()#Leerzeichen werden am Anfang und am Ende entfernt
        self.db.connect()#Verbindung zur DB wird erstellt
        pswd = self.db.select_pswd(benutzername_email)#das Passwort was zum Benutzername/E-Mail passt was in der DB gespeichert wurde wird hier zurückgegeben

        if pswt != pswd[0][0]:#hier wird geschaut ob das Passwort im Eingabefeld das gleiche Passwort ist wie in der DB. Stimmt es nicht kommt eine Fehlermeldung.
            fehler_medlung = "Fehler! Benutzername/E-Mail oder Passwort stimmt nicht."
            print(fehler_medlung)
        self.db.close()#Verbindung zur DB wird getrennt

    def neu(self):
        benutzername = 'ud'#Eingabefeld vom Benutzernamen
        pswt = 'u'#Eingabefeld vom Passwort
        pswt_w = 'u'#Eingabefeld vom Passwort wiederholen
        vorname = 'ulli'#Eingabefeld vom Vornamen
        nachname = 'doujak'#Eingabefeld vom Nachname
        email = 'ud@gmail.com'#Eingabefeld vom E-Mail
        geburtsdatum = '2020-11-10'#Eingabefeld vom Geburtsdatum
        telefon = ''#Eingabefeld von der Telefonnummer
       
       


        benutzername = benutzername.strip()#Leerzeichen werden am Anfang und am Ende entfernt
        vorname = vorname.strip()#Leerzeichen werden am Anfang und am Ende entfernt
        nachname = nachname.strip()#Leerzeichen werden am Anfang und am Ende entfernt

        p_email = "^([a-zA-Z0-9]+([-_\.]?[a-zA-Z0-9])+@[a-zA-Z0-9]+([-_\.]?[a-zA-Z0-9])+\.[a-z]{2,4}){0,}$"
        p_name = "^[a-zA-Z]+$"
        p_pswd = "^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{6,}$"

        if pswt != pswt_w:#Hier wird geschaut ob in den Passwortfelder das gleiche drinnen steht, wenn nicht kommt eine Fehlermeldung
                fehler_medlung = "Fehler! Passwortfelder stimmen nicht überein."
                print(fehler_medlung)
        if not re.search(p_pswd,pswt):  
            print('Keine gültiges Passwort! min. 6 Zeichen lang,min. 1 Großbuchstaben, min. 1 Kleinbuchstaben und min. 1 Ziffer enthalten.')
        geburtsdatum = datetime.datetime.strptime(geburtsdatum, '%Y-%m-%d')#wird zum type datetime conventiert
        if geburtsdatum > datetime.datetime.today():#schaut ob du schon geboren wurdest, wenn nicht fehler meldung
            print('Geburtsdatum stimmt nicht!')
        
        if not re.search(p_email,email):  
            print('Keine gültige Email Adresse')

        if not re.search(p_name,vorname):  
            print('Kein gültiger Vorname. Es sind nur Buchstaben erlaubt.') 
        if not re.search(p_name,nachname):  
            print('Kein gültiger Vorname. Es sind nur Buchstaben erlaubt.') 

        exist_benutzername = self.db.select_benutzername(benutzername)
        exist_benutzername = exist_benutzername[0][0]
        if exist_benutzername !=0:
            print("Dieser Benutzername exestiert schon")






        self.db.connect()#verbindung zur DB wird erstellt
        self.db.insert_kunde(benutzername,pswt,vorname,nachname,email,geburtsdatum,telefon)#neues Konot wird erstellt
        self.db.close()#Verbindung zur DB wird getrentt
    def kunde_id(self,benutzername_email,pswt):
        self.db.connect()#Verbindung zur DB wird erstellt
        self.id = self.db.select_id(benutzername_email,pswt)
        self.id = self.id[0][0]
        self.db.close()#Verbindung zur DB wird getrent
    
    def kundenevent(self):#Verlauf erstellen
        self.db.connect()#Verbindung zur DB wird erstellt

        #SQL-State wo ich die ID vom Event bekomme was ich auswähle
        event_id = '1'


        self.db.insert_kundenevent(self.id,event_id)
        self.db.close()#Verbindung zur DB wird getrent
    def mail(self):
        user = 'alisa6rieger@gmail.com'
        pwd = 'spuzunwyyivbpnbe'
        mail_text = 'Es gab einen Coronafall!'
        subject = 'Warnung!'

        #emails sind alle Emails von den Usern, ausgenommen der die Meldung sendete, die auch bei den Events waren wo auch der erkrankte User 3 Tage vor dem 1 Syntom tag war
        heute = datetime.date.today()
        tage = datetime.timedelta(days=3)

        date = heute-tage
        self.db.connect()
        emails = []
        for i in self.db.select_mail(self.id,date):
            for e in i:
                emails.append(e)
        self.db.close()

        MAIL_FROM = user
        RCPT_TO  = ", ".join(emails)
        DATA = 'From:%s\nTo:%s\nSubject:%s\n\n%s' % (MAIL_FROM, RCPT_TO, subject, mail_text)
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(user, pwd)
        server.sendmail(MAIL_FROM, RCPT_TO, DATA)
        server.quit()
        #Die verbindung wird geschlossen
        server.close()
    def passwort_email(self):
        user = 'alisa6rieger@gmail.com'
        pwd = 'spuzunwyyivbpnbe'
        subject = 'Verifizierungs Email'

        #eindeutige Nummer für die Passwort zurücksetzung wird erstellt.
        #im ergebnis steht die eindeutige nummer die als inhalt der email geschickt wird
        mail_text = ""
        for x in range(5):
            mail_text += str(random.randint(1,9))

        MAIL_FROM = user
        self.db.connect()
        email = self.db.select_user_email(self.id)
        self.db.close()
        RCPT_TO  = email[0][0]#email ist die Email vom User der das Passwort ändern möchte. Diese Information bekomme ich aus der DB
        DATA = 'From:%s\nTo:%s\nSubject:%s\n\n%s' % (MAIL_FROM, RCPT_TO, subject, mail_text)
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(user, pwd)
        server.sendmail(MAIL_FROM, RCPT_TO, DATA)
        server.quit()
        #Die verbindung wird geschlossen
        server.close()

        #ein SQL-State wo das Passwort geändert wird
    def evinput(self):
        #Zurzeit sind nur placeholder Daten drinnen, die müssen dann angepasst werden, sobald es eine Funktion/Weg zur übertragung der DB Daten gibt.

        #Input für den Eventnamen
        name = ''
        #Input für das Eventdatum (YYYY-MM-DD Format, geht auch mit / oder .)
        datum = ''
        #Input für die Uhrzeit des Events (24:00 Format)
        zeit = ''

        if datum != None:
            #Checkt ob das Datum richtig formatiert ist, falls nicht, wird es korregiert.
            for i in datum:
                if i == "/" or i == ".":
                    datum = datum.replace(i, "-")

            #Checkt, ob das Datum im "date"-Format der MySQL Datenbank geschrieben wurde.
            date_p = "^\d{4}(?P<sep>[\/.-])\d{2}(?P=sep)(\d{2})$"
            date = re.match(date_p, datum)
                
            #Falls alle Daten nicht None sind, wird das Event hinzugefügt.
            if date != None and name != None and zeit != None:
                self.db.connect()#Verbindung zur DB wird erstellt
                self.db.eventinsert(name, datum, zeit)
                self.db.close()
                
            else:
                print("Missing Data")


    #Funktion um Events aus der Datenbank zu holen.
    def evoutput(self, name):
        
        if name != None:
            self.db.connect()
            out = self.db.eventoutput(name)
            output = []
            for i in out[0]:
                output.append(str(i))
            print(output)
            self.db.close()
#Website = Login()
#Website.neu()
# Website.anmelden()

