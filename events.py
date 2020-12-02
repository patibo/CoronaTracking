import re
import datetime
import mysql.connector

class DBcon:
    def __init__(self, user, pswd, host, port, db):
        self.config = {
            'user': user,
            'password': pswd,
            'host': host,
            'port': port,
            'database': db
        }
        self.mydb = None
        self.cursor = None
    
    #Verbindung zur Datenbank herstellen.
    def connect(self):
        self.mydb = mysql.connector.connect(**self.config)
        self.cursor = self.mydb.cursor()

    #Neues Event anlegen
    def eventinsert(self, name, datum, zeit): 
        sql = "INSERT INTO `eventsentry`(`name`, `datum`, `zeit`) VALUES ('{}', '{}', '{}')".format(name, datum, zeit)
        self.cursor.execute(sql)
        self.mydb.commit()
    
    def eventoutput(self, name):
        sql = "SELECT * FROM `eventsentry` WHERE `eventsentry`.`name` = '{}'".format(name)
        self.cursor.execute(sql)
        
        return self.cursor.fetchall()
    
    #Datenbank schließen
    def close(self):
        self.cursor.close()
        self.mydb.close()


class Eventinput:

    def evinput(self):
        #Instanzierung der DBcon Klasse, damit sie hier aufgerufen werden kann.
        #Zurzeit sind nur placeholder Daten drinnen, die müssen dann angepasst werden, sobald es eine Funktion/Weg zur übertragung der DB Daten gibt.
        dbcon = DBcon('root', 'root', 'localhost', '3306', 'coronatracking')

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
            date = re.match('^\d{4}(?P<sep>[\/.-])\d{2}(?P=sep)(\d{2})$', datum)
            
            #Falls alle Daten nicht None sind, wird das Event hinzugefügt.
            if date != None and name != None and zeit != None:
                dbcon.connect()
                dbcon.eventinsert(name, datum, zeit)
                dbcon.close()
                
            else:
                print("Missing Data")


    #Funktion um Events aus der Datenbank zu holen.
    def evoutput(self, name):
        
        dbcon = DBcon('root', 'root', 'localhost', '3306', 'coronatracking')
        
        if name != None:
            self.dbcon.connect()
            out = self.dbcon.eventoutput(name)
            output = []
            for i in out[0]:
                output.append(str(i))
            print(output)
            dbcon.close()

if __name__ == "__main__":
    Ein = Eventinput()
    Ein.evinput()
    #Ein.evoutput('name')