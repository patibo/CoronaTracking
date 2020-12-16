import re #Bibliothek regex wird importiert. Ist für die Überprüfung der Eingaben.
import mysql.connector#Bibliothek mysql wird importiert. Ist für die Verbindung zur Datenbank.
import datetime#Bibliothek datetime wird importiert. Ist für die Prüfung vom Geburtsdatum.
import smtplib#Bibliothek smtplib wird importiert. Ist für den Zugriff und versendung der E-Mails zuständig.
import random#Bibliothek random wird importiert.Ist für die 5 Stellige Verefezierung für Passwort zurücksetzen.
import base64#Bibliothek für die Verschlüsselung
from tkinter import *#Bibliothek für die Obrfläche
from tkinter import messagebox


class GUI:#Klasse der Oberfläche
    def __init__(self,surface):
        self.backend = Backend()#zugriff auf die Klasse Backend
        """ GUI Fenster """
        self.surface = surface
        self.title = 'Coronatracking-App'
        self.surface.title(self.title)
        #Hier werden alle Labels, Enterys, etc. erstellt die jemals im Programm verwendet wird, ohne ihre Eigenschaft zu bestimmen also Text, Farbe, usw.
        """ Hauptseit: Listenbox """
        self.listbox = Listbox(self.surface)
        self.index = None
        self.inhalt = None
        self.scroll = Scrollbar(self.surface,orient=VERTICAL)

        #regestrierung
        self.benutzername = Label(self.surface)
        self.pswt = Label(self.surface)
        self.pswt_w = Label(self.surface)
        self.vorname = Label(self.surface)
        self.nachname = Label(self.surface)
        self.email_r = Label(self.surface)

        self.e_benutzername = Entry(self.surface)
        self.e_pswt = Entry(self.surface,show="*")
        self.e_pswt_w = Entry(self.surface,show="*")
        self.e_vorname = Entry(self.surface)
        self.e_nachname = Entry(self.surface)
        self.e_email = Entry(self.surface)

        self.b_save = Button(self.surface)

        self.fehler = Label(self.surface)
        #login
        self.userLabel = Label(self.surface)
        self.userEntry = Entry(self.surface)
        self.passLabel = Label(self.surface)
        self.passEntry = Entry(self.surface,show="*")

        self.b_regestrieren = Button(self.surface)
        self.b_login = Button(self.surface)
        self.b_pswt_return = Button(self.surface)
        #startseite
        self.t_verlauf = Label(self.surface)

        self.b_logout = Button(self.surface)

        #Events erstellen (GUI Fenster)
        self.name = Label(self.surface)
        self.datum = Label(self.surface)
        self.zeit = Label(self.surface)

        self.ev_name = Entry(self.surface)
        self.ev_datum = Entry(self.surface)
        self.ev_zeit = Entry(self.surface)
        
        self.ev_error = Label(self.surface)
        #Event_hinzufügen
        self.ev_title = Label(self.surface)
        self.ev_createbutton = Button(self.surface)
        self.ev_cancelbutton = Button(self.surface)
        #email
        self.b_verdachtsfall = Button(self.surface)
        #event regestrieren
        self.b_regestrieren_event = Button(self.surface)

        self.var_event_auswahl = StringVar(self.surface)
        self.event_l = Label(self.surface)
        self.event_om = Label(self.surface)
        self.event_b = Button(self.surface)

        #passwort zurücksetzen
        self.pvLabel = Label(self.surface)
        self.emailLabel = Label(self.surface)
        self.psLabel = Label(self.surface)
        self.codeLabel = Label(self.surface)
        
        self.email = Entry(self.surface)

        self.pv_pass = Entry(self.surface)
        self.pv_passw = Entry(self.surface)
        self.pv_code = Entry(self.surface)
        self.pv_email = Entry(self.surface)
        self.pv_button = Button(self.surface)
        self.pv_stop = Button(self.surface)

        self.email_adress = None

    def menubar(self):
        menubar = Menu(self.surface)
        filemenu = Menu(self.surface, tearoff=0)
        filemenu.add_command(label="Registrieren", command=self.regestrieren())
        filemenu.add_command(label="Login", command=self.login)

        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.surface.destroy)
        menubar.add_cascade(label="File", menu=filemenu)

        self.surface.config(menu=menubar)


    def clear_design(self):
        #hier werden alle Labels, Enterys, etc. ausgeblendet
        """ Hauptseit: Listenbox """
        self.listbox.grid_forget()
        self.scroll.grid_forget()

        #regestrieren
        self.benutzername.grid_forget()
        self.pswt.grid_forget()
        self.pswt_w.grid_forget()
        self.vorname.grid_forget()
        self.nachname.grid_forget()
        self.email_r.grid_forget()

        self.e_benutzername.grid_forget()
        self.e_pswt.grid_forget()
        self.e_pswt_w.grid_forget()
        self.e_vorname.grid_forget()
        self.e_nachname.grid_forget()
        self.e_email.grid_forget()

        self.b_save.grid_forget()

        self.fehler.grid_forget()
        #login
        self.userLabel.grid_forget()
        self.userEntry.grid_forget()
        self.passLabel.grid_forget()
        self.passEntry.grid_forget()

        self.b_regestrieren.grid_forget()
        self.b_login.grid_forget()
        self.b_pswt_return.grid_forget()

        #startseite
        self.t_verlauf.grid_forget()
        
        self.b_logout.grid_forget()

        #Events .grid_forget()
        self.name.grid_forget()
        self.datum.grid_forget()
        self.zeit.grid_forget()

        self.ev_name.grid_forget()
        self.ev_datum.grid_forget()
        self.ev_zeit.grid_forget()
        self.ev_error.grid_forget()

        self.ev_title.grid_forget()
        self.ev_createbutton.grid_forget()
        self.ev_cancelbutton.grid_forget()

        #email
        self.b_verdachtsfall.grid_forget()

        #event regestrieren
        self.b_regestrieren_event.grid_forget()

  
        self.event_l.grid_forget()
        self.event_om.grid_forget()
        self.event_b.grid_forget()

        #passwort zurücksetzen
        self.pvLabel.grid_forget()
        self.emailLabel.grid_forget()
        self.psLabel.grid_forget()
        self.codeLabel.grid_forget()
        

        self.pv_pass.grid_forget()
        self.pv_passw.grid_forget()
        self.pv_code.grid_forget()
        self.pv_email.grid_forget()
        self.pv_button.grid_forget()
        self.pv_stop.grid_forget()


    def regestrieren(self):
        self.clear_design()#ganzer Inhalt des Fensters wird ausgeblendet
        #der Text der Labels werden geändert
        self.benutzername.config(text='Benutzername:',bg="#005ca9", fg="white",padx=140)
        self.pswt.config(text='Passwort:',bg="#005ca9", fg="white")
        self.pswt_w.config(text='Passwort wiederholen:',bg="#005ca9", fg="white")
        self.vorname.config(text='Vorname:',bg="#005ca9", fg="white")
        self.nachname.config(text='Nachname:',bg="#005ca9", fg="white")
        self.email_r.config(text='Email:',bg="#005ca9", fg="white")
        
        #Labels,Enterys, Buttons werden hier positioniert
        self.benutzername.grid(row=2, column=1)
        self.pswt.grid(row=4, column=1, pady=(0, 10))
        self.pswt_w.grid(row=6, column=1, pady=(0, 10))
        self.vorname.grid(row=8, column=1, pady=(0, 10))
        self.nachname.grid(row=10, column=1, pady=(0, 10))
        self.email_r.grid(row=14, column=1, pady=(0, 10))

        self.e_benutzername.grid(row=2, column=2, pady=(20, 10))
        self.e_pswt.grid(row=4, column=2, pady=(0, 10))
        self.e_pswt_w.grid(row=6, column=2, pady=(0, 10))
        self.e_vorname.grid(row=8, column=2, pady=(0, 10))
        self.e_nachname.grid(row=10, column=2, pady=(0, 10))
        self.e_email.grid(row=14, column=2, pady=(0, 10))

        self.b_save.config(text='Erstellen', command=self.benutzer_erstellen,bg="green")#der Text vom Button wird geändert und festgelegt welche Methode aufgerufen wird, wenn der Button geklickt wird
        self.b_save.grid(row=18, column=2, pady = (12))
        self.fehler.grid(row=19, column=2, columnspan=30)



        
    def benutzer_erstellen(self):
        #Inahlter der Eingabefelder werden rausgehohlt
        benutzername = self.e_benutzername.get()
        pswt = self.e_pswt.get()
        pswt_w = self.e_pswt_w.get()
        vorname = self.e_vorname.get()
        nachname = self.e_nachname.get()
        email = self.e_email.get()
        #Eingaben werden überprüft
        fehler_text = self.backend.neu(benutzername,pswt,pswt_w,vorname,nachname,email)
        
        if fehler_text != None:#Gibt es einen Fehler wird die Meldung angezeigt und man kommt nicht weiter
            self.fehler.config(text=fehler_text)
            
            self.regestrieren()
        else:#Inhalte der Eingabefelder werden entleert, Text vom Lable fehler wird geändert, man kommt auf die login Seite zurück
            self.fehler.config(text='')
            self.e_benutzername.delete(0,'end')
            self.e_pswt.delete(0,'end')
            self.e_pswt_w.delete(0,'end')
            self.e_vorname.delete(0,'end')
            self.e_nachname.delete(0,'end')
            self.e_email.delete(0,'end')
            self.login()

    def login(self):
        self.surface.configure(bg="#005ca9")
        self.surface.geometry("800x400")
        self.clear_design()#ganzer Inhalt des Fensters wird ausgeblendet
        #der Text der Labels werden geändert
        self.userLabel.config(text="Email/Benutzername:",bg="#005ca9", fg="white", padx=130)
        self.passLabel.config(text="Passwort:",bg="#005ca9", fg="white")
        self.fehler.config(bg="#005ca9", fg="red")
        #die Labels werden positioniert
        self.userLabel.grid(row=1, column=0,)
        self.userEntry.grid(row=1, column=1,pady = (10,4))
        self.passLabel.grid(row=2, column=0)
        self.passEntry.grid(row=2, column=1,pady = (5))
        #die Eigenschaften der Buttons werden geändert
        self.b_regestrieren.config(text='Regestrieren',command=self.menubar,bg="green")
        self.b_login.config(text='Login',command=self.login_pr,bg="green")
        self.b_pswt_return.config(text='Passwort zurücksetzen',command=self.pswt_r,bg="#33ccff")
        #die Buttons werden positioniert
        self.b_regestrieren.grid(row=4, column=1)
        self.b_login.grid(row=4, column=0)
        self.b_pswt_return.grid(row=3, column=1)
        self.fehler.grid(row=5, column=1)
        self.surface.mainloop()#fenster schließt sich nicht automatisch
    def login_pr(self):
        user = self.userEntry.get()
        pswt = self.passEntry.get()
        fehler_text = self.backend.anmelden(user, pswt)
        
        if fehler_text != None:
            #print(fehler_text)
            self.fehler.config(text=fehler_text)
            
            self.login()
        else:
            self.fehler.config(text='')
            self.userEntry.delete(0,'end')
            self.passEntry.delete(0,'end')
            self.main()
    def main(self):
        self.clear_design()
        self.listbox.delete(0,'end')#alter Listbox stand wird gelöscht

        """Scrollbar wird zur Listbox hinzugefügt"""
        self.listbox["yscrollcommand"]=self.scroll.set
        self.scroll["command"]=self.listbox.yview
        
        for i in self.backend.kundenevent():#die aktuelle Liste wird in der Listbox angezeigt
            text = i[1]+" am "+str(i[2])+" um "+str(i[3])
            self.listbox.insert(END, text)
        #positionierung der Listbox und Scrollbar
        self.listbox.grid(row=1,column=1,columnspan=10,sticky=N+E+S+W)
        self.scroll.grid(row=1,column=10, sticky=E+N+S)

        self.t_verlauf.config(text='Verlauf',font = "Helvetica 16 bold italic")
 
        self.t_verlauf.grid(row = 0, column=1)
        self.b_logout.grid(row = 3, column=11)
        self.b_logout.config(text='Abmelden',command=self.logout)
        self.b_verdachtsfall.config(text='Corona Fall melden', command=self.verdachtsfall, bg='red', fg='black')
        self.b_verdachtsfall.grid(row = 12, column=1)
        self.b_regestrieren_event.config(text='Event reservieren',command=self.event_reservieren)
        self.b_regestrieren_event.grid(row = 13, column=3)
    def event_reservieren(self):
        self.clear_design()
        self.var_event_auswahl.set("Events")  # default value

        self.event_l.config(text='Select One', width=10)
        self.event_l.grid(row=2, column=1)
        liste = self.backend.event()
        self.event_om = OptionMenu(self.surface,self.var_event_auswahl, *liste)
        self.event_om.grid(row=2, column=2)

        self.event_b.config(text='Reservieren', command=self.reservieren)
        self.event_b.grid(row=2, column=3)
        self.pv_stop.config(text="Abbrechen", command=self.main)
        self.pv_stop.grid(row=2, column=1)
    def reservieren(self):
        name = self.var_event_auswahl.get()
        self.backend.db.connect()
        verlauf = self.backend.db.verlauf(self.backend.id)
        self.backend.db.close()
        ok = 0
        for i in verlauf:
            if i[1] in name:
                messagebox.showinfo('Event reservieren', 'Für dieses Event haben sie schon reserviert.')
                ok = 1
                break
        if ok == 0:        
            events = self.backend.event()
            for i in events:
                if i[0] in name:
                    self.backend.event_res(i[0])
            self.main()
        else:
            self.event_reservieren()
        

    def verdachtsfall(self):
        MsgBox = messagebox.askquestion('Corona Fall melden', 'Sind Sie sich sicher, dass Sie einen Corona Fall melden möchten?',icon='warning')
        if MsgBox == 'yes':
            self.backend.mail()
            messagebox.showinfo('Bestätigung', 'Die warn E-Mails wurden versendet')
            self.main()
        else:
            self.main()
            

    def logout(self):
        self.backend.logout()
        self.login()
    def pswt_r(self):
        self.clear_design()
        self.emailLabel.config(text="Geben sie bitte ihre Email-Adresse ihres Accounts an:", bg="#005ca9")
        
        self.pv_button.config(text="Senden", command=self.email_p)
        self.pv_stop.config(text="Abbrechen", command=self.login)

        self.emailLabel.grid(row=1, column=1)
        self.email.grid(row=2, column=1)
        self.pv_button.grid(row=3, column=0)
        self.pv_stop.grid(row=3, column=1)
        self.fehler.grid(row=4, column=1)
    def email_p(self):
        email = self.email.get()
        fehler_text = self.backend.passwort_email(email)
        if fehler_text != None:#Gibt es einen Fehler wird die Meldung angezeigt und man kommt nicht weiter
            self.fehler.config(text=fehler_text)
            self.pswt_r()
        else:#Inhalte der Eingabefelder werden entleert, Text vom Lable fehler wird geändert, man kommt auf die login Seite zurück
            self.fehler.config(text='')
            self.email_adress = self.email.get()
            self.email.delete(0,'end')
            self.verifiziercode()

    def verifiziercode(self):
        self.clear_design()
        self.psLabel.config(text="Geben sie den 5-stellingen Code der ihnen per Email gesendet wurde", bg="#005ca9")

        self.psLabel.grid(row=1, column=1)
        self.email.grid(row=2, column=1)
        self.pv_button.config(text="Bestätigen", command=self.code_p)
        self.pv_stop.config(text="Abbrechen", command=self.login)
        self.pv_button.grid(row=3, column=0)
        self.pv_stop.grid(row=3, column=1)
        self.fehler.grid(row=4, column=0)
    def code_p(self):
        code = self.email.get()
        fehler_text = self.backend.code_pr(code)
        if fehler_text != None:#Gibt es einen Fehler wird die Meldung angezeigt und man kommt nicht weiter
            messagebox.showinfo('Code ist falsch', fehler_text)
            self.email.delete(0,'end')
            self.login()
        else:#Inhalte der Eingabefelder werden entleert, Text vom Lable fehler wird geändert, man kommt auf die login Seite zurück
            self.email.delete(0,'end')
            self.zuruecksetzen()
        
    def zuruecksetzen(self):
        self.clear_design()
        self.psLabel = Label(text="Geben sie das neue Passwort ein:", bg="#005ca9")
       
        self.pv_button.config(text="Bestätigen", command=self.neu_pswt_p)
        self.pv_stop.config(text="Abbrechen", command=self.login)

        self.psLabel.grid(row=0, column=0)
        self.pv_pass.grid(row=1, column=0)
        self.pv_passw.grid(row=2, column=0)
        self.pv_button.grid(row=3, column=0)
        self.pv_stop.grid(row=3, column=1)
    def neu_pswt_p(self):
        pswt = self.pv_pass.get()
        pswt_w = self.pv_passw.get()
        fehler_text = self.backend.neuse_passwort(pswt,pswt_w,self.email_adress)
        if fehler_text != None:#Gibt es einen Fehler wird die Meldung angezeigt und man kommt nicht weiter
            self.fehler.config(text=fehler_text)
            self.zuruecksetzen()
        else:#Inhalte der Eingabefelder werden entleert, Text vom Lable fehler wird geändert, man kommt auf die login Seite zurück
            self.fehler.config(text='')
            self.pv_pass.delete(0,'end')
            self.pv_passw.delete(0,'end')
            self.login()
    #Fenster zum erstellen von Events
    def event_input(self):
        self.clear_design()
        self.ev_title.config(text="Geben Sie die Info des Events das sie erstellen wollen an.", bg="#005ca9", font="bold")
        self.name.config(text='Name:', bg="#005ca9")
        self.datum.config(text='Datum:', bg="#005ca9")
        self.zeit.config(text='Zeit:', bg="#005ca9")
        self.ev_createbutton.config(text="Bestätigen", command=self.event_erstellen)
        self.ev_cancelbutton.config(text="Abbrechen", command=self.main)
        self.ev_error.config(text="", bg="#005ca9", fg="red")
        self.ev_title.grid(row=0, columnspan=20)
        self.name.grid(row=1, column=0)
        self.datum.grid(row=2, column=0)
        self.zeit.grid(row=3, column=0)

        self.ev_name.grid(row=1, column=1)
        self.ev_datum.grid(row=2, column=1)
        self.ev_zeit.grid(row=3, column=1)

        self.ev_createbutton.grid(row=4, column=1)
        self.ev_cancelbutton.grid(row=4, column=3)
        self.ev_error.grid(row=5, column=0, columnspan=5, sticky=N+S+E+W)
    def event_erstellen(self):
       #Input für den Eventnamen
        name = self.ev_name.get()
        #Input für das Eventdatum (YYYY-MM-DD Format, geht auch mit / oder .)
        datum = self.ev_datum.get()
        #Input für die Uhrzeit des Events (24:00 Format)
        zeit = self.ev_zeit.get()

        #Sind alle Felder ausgefüllt, wird das Event angelegt/erstellt.
        if name != '' and datum != '' and zeit != '':
            fehler = self.backend.evinput(name, datum, zeit)
            if fehler != None:
                self.ev_error.config(text=fehler, fg="red")
                self.event_input()
            else:
                self.main()

        else:
            fehler = "Die Eingabe ist unvollständig!"
            self.ev_error.config(text=fehler)
            self.event_input()

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
    def insert_kunde(self,benutzername,pswt,vorname,nachname,email):#ein Neuer Kunde wird erstellt
        sql = "INSERT INTO `kunden`(`benutzername`, `passwort`, `vorname`, `nachname`, `email`) VALUES ('{}','{}','{}','{}','{}')".format(benutzername,pswt,vorname,nachname,email)
        self.cur.execute(sql)
        self.mydb.commit()
    def insert_kundenevent(self,kunden_id,event_id):
        sql="INSERT INTO `kundenevents` (`kID`, `eID`) VALUES ('{}', '{}');".format(kunden_id[0][0],event_id[0][0])
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
    def select_email(self,email):
        sql = "SELECT COUNT(*) FROM kunden WHERE email = '{}' ".format(email)
        self.cur.execute(sql)
        return self.cur.fetchall()
    def select_mail(self,kunden_id,date):
        sql = "SELECT kunden.`email` FROM kunden JOIN kundenevents ON kunden.id=kundenevents.kID JOIN eventsentry on eventsentry.id = kundenevents.eID WHERE kunden.id != {} and eventsentry.datum >='{}'and eventsentry.id IN(SELECT eventsentry.id FROM eventsentry JOIN kundenevents ON eventsentry.id=kundenevents.eID JOIN kunden on kunden.id = kundenevents.kID WHERE kunden.id = {} and eventsentry.datum >='{}')".format(kunden_id[0][0],date,kunden_id[0][0],date)  
        self.cur.execute(sql)
        return self.cur.fetchall() 
    def select_event_mail(self,kunden_id,date):
        sql = "SELECT eventsentry.name,eventsentry.datum,eventsentry.zeit FROM eventsentry JOIN kundenevents ON eventsentry.id=kundenevents.eID JOIN kunden on kunden.id = kundenevents.kID WHERE kunden.id = {} and eventsentry.datum >= '{}'".format(kunden_id[0][0],date,kunden_id[0][0],date)  
        self.cur.execute(sql)
        return self.cur.fetchall()  
    def select_user_email(self, kunden_id):
        sql = "SELECT `email` FROM kunden WHERE id = {}".format(kunden_id)
        self.cur.execute(sql)
        return self.cur.fetchall() 
    def update_pswd(self, pswd,email):
        
        sql = "UPDATE `kunden` SET `passwort`='{}' WHERE `email` = '{}'".format(pswd,email)
        self.cur.execute(sql)
        self.mydb.commit()
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
    def event_id(self, name):
        sql = "SELECT id FROM `eventsentry` WHERE `eventsentry`.`name` = '{}'".format(name)
        self.cur.execute(sql)
        return self.cur.fetchall()
    def eventout(self):
        sql = "SELECT `name`,`datum`,`zeit` FROM `eventsentry`"
        self.cur.execute(sql)
        return self.cur.fetchall()
    def verlauf(self,kunden_id):

        sql = "SELECT * FROM eventsentry WHERE id IN (SELECT eID FROM kundenevents WHERE kID = {})".format(kunden_id[0][0])
        self.cur.execute(sql)
        return self.cur.fetchall()

class Backend:#Hier passiert alles was im hintergrund der Webseite
    def __init__(self):
        #ilirjan: 'root','15071998','localhost','3306','coronatracking'
        #alisa: 'root','root','localhost','8889','coronatracking'
        self.db = DB('root','15071998','localhost','3306','coronatracking')#hier kann ich die Klasse DB verwenden bzw. hier wird sie aufgerufen
        self.id = None
        self.mail_text = ""
    def anmelden(self,benutzername_email,pswt):#anmelde funktion

        fehlerfrei = "ok"
        
        benutzername_email = benutzername_email.strip()#Leerzeichen werden am Anfang und am Ende entfernt
        self.db.connect()#Verbindung zur DB wird erstellt
        pswd_sql = self.db.select_pswd(benutzername_email)#das Passwort was zum Benutzername/E-Mail passt was in der DB gespeichert wurde wird hier zurückgegeben

        if len(pswd_sql) != 0:
            encoded_pswd = pswd_sql[0][0].encode('ascii')
            encoded_byte = base64.b64decode(encoded_pswd)
            pswd = encoded_byte.decode('ascii')
            if pswt != pswd:#hier wird geschaut ob das Passwort im Eingabefeld das gleiche Passwort ist wie in der DB. Stimmt es nicht kommt eine Fehlermeldung.
                fehler_medlung = "Fehler! Benutzername/E-Mail oder Passwort stimmt nicht."
                fehlerfrei = ""
                return fehler_medlung
                
            
            if fehlerfrei == 'ok':
                #print('benutz:',benutzername_email)
                #print(pswd)
                self.id = self.db.select_id(benutzername_email,pswd_sql[0][0])
                #print('anmelden',self.id)
                self.db.close()#Verbindung zur DB wird getrennt
        else:
            fehler_medlung = "Fehler! Benutzername/E-Mail oder Passwort stimmt nicht."
            fehlerfrei = ""
            return fehler_medlung
            
       

    def neu(self, benutzername,pswt,pswt_w,vorname,nachname,email):

        fehlerfrei = "ok"
       


        benutzername = benutzername.strip()#Leerzeichen werden am Anfang und am Ende entfernt
        vorname = vorname.strip()#Leerzeichen werden am Anfang und am Ende entfernt
        nachname = nachname.strip()#Leerzeichen werden am Anfang und am Ende entfernt

        p_email = "^([a-zA-Z0-9]+([-_\.]?[a-zA-Z0-9])+@[a-zA-Z0-9]+([-_\.]?[a-zA-Z0-9])+\.[a-z]{2,4}){0,}$"
        p_name = "^[a-zA-ZäüöÄÜÖ]{,20}$"
        p_pswd = "^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,32}$"
        p_benutzername = "^[0-9A-Za-z]{,16}$"

        self.db.connect()#verbindung zur DB wird erstellt
        exist_benutzername = self.db.select_benutzername(benutzername)
        exist_benutzername = exist_benutzername[0][0]
        if exist_benutzername !=0:
            #print('Dieser Benutzername exestiert schon')
            fehlerfrei = ""
            return "Dieser Benutzername exestiert schon"
        if not re.search(p_benutzername,benutzername):  
            fehlerfrei = ""
            #print('Keine gültiges Passwort! min. 6 Zeichen lang,min. 1 Großbuchstaben, min. 1 Kleinbuchstaben und min. 1 Ziffer enthalten.')
            return 'Keine gültiger Benutzername! max. 16 Zeichen lang, nur Buchstaben und Zahlen erlaubt.'

        if pswt != pswt_w:#Hier wird geschaut ob in den Passwortfelder das gleiche drinnen steht, wenn nicht kommt eine Fehlermeldung
            fehler_medlung = "Fehler! Passwortfelder stimmen nicht überein."
            fehlerfrei = ""
            #print(fehler_medlung)
            return fehler_medlung
        if not re.search(p_pswd,pswt):  
            fehlerfrei = ""
            #print('Keine gültiges Passwort! min. 6 Zeichen lang,min. 1 Großbuchstaben, min. 1 Kleinbuchstaben und min. 1 Ziffer enthalten.')
            return 'Keine gültiges Passwort! min. 8 und max. 32 Zeichen lang,min. 1 Großbuchstaben, min. 1 Kleinbuchstaben und min. 1 Ziffer enthalten.'
            
        # geburtsdatum = datetime.datetime.strptime(geburtsdatum, '%Y-%m-%d')#wird zum type datetime conventiert
        # if geburtsdatum > datetime.datetime.today():#schaut ob du schon geboren wurdest, wenn nicht fehler meldung
        #     print('Geburtsdatum stimmt nicht!')
        if not re.search(p_name,vorname):  
           
            fehlerfrei = ""
            #print('Kein gültiger Vorname. Es sind nur Buchstaben erlaubt.')
            return 'Kein gültiger Vorname. Es sind nur Buchstaben erlaubt und darf nicht länger als 20 Zeichen lang sein.'
        if not re.search(p_name,nachname):  
            
            fehlerfrei = ""
            #print('Kein gültiger Nachname. Es sind nur Buchstaben erlaubt.')
            return 'Kein gültiger Nachname. Es sind nur Buchstaben erlaubt und darf nicht länger als 20 Zeichen lang sein.'
        if not re.search(p_email,email):  
           
            fehlerfrei = ""
            #print('Keine gültige Email Adresse')
            return 'Keine gültige Email Adresse'
        exist_email = self.db.select_email(email)
        exist_email = exist_email[0][0]
        if exist_email != 0:
            fehlerfrei = ""
            return "Diese E-Mail exestiert schon"

       
        
        if fehlerfrei == 'ok':

            pswd_byte = pswt.encode('ascii')
            encoded_byte = base64.b64encode(pswd_byte)
            encoded_pswd = encoded_byte.decode('ascii')


            self.db.insert_kunde(benutzername,encoded_pswd,vorname,nachname,email)#neues Konot wird erstellt

            self.db.close()#Verbindung zur DB wird getrentt


        
    def kunde_id(self,benutzername_email,pswt):
        self.db.connect()#Verbindung zur DB wird erstellt
        self.id = self.db.select_id(benutzername_email,pswt)
        self.id = self.id[0][0]
        self.db.close()#Verbindung zur DB wird getrent
    def event_res(self, name):
        self.db.connect()#Verbindung zur DB wird erstellt
        
        #SQL-State wo ich die ID vom Event bekomme was ich auswähle
        e_id = self.db.event_id(name)
        self.db.insert_kundenevent(self.id,e_id)
        self.db.close()
    def kundenevent(self):#Verlauf erstellen
        self.db.connect()#Verbindung zur DB wird erstellt

        
        
        events = self.db.verlauf(self.id)

        self.db.close()#Verbindung zur DB wird getrent
        return events
    def mail(self):
        user = 'alisa6rieger@gmail.com'
        pwd = 'spuzunwyyivbpnbe'
        mail_text = 'Es gab einen Coronafall bei diesen Events:'
        subject = 'Warnung!'

        #emails sind alle Emails von den Usern, ausgenommen der die Meldung sendete, die auch bei den Events waren wo auch der erkrankte User 3 Tage vor dem 1 Syntom tag war
        heute = datetime.date.today()
        tage = datetime.timedelta(days=3)

        date = heute-tage
        self.db.connect()
        
        for i in self.db.select_event_mail(self.id,date):
            for e in i:
                mail_text = mail_text+' '+str(e)
            mail_text = mail_text+','
        mail_text = mail_text[:-1]
        emails = []
        for i in self.db.select_mail(self.id,date):
            for e in i:
                emails.append(e)
        self.db.close()

        FROM = user
        # to  = ", ".join(emails)
        # print('to: ',to)
        # DATA = 'From:{}\nTo:{}\nSubject:{}\n\n{}'.format(FROM, to, subject, mail_text)
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(user, pwd)
        # server.sendmail(FROM, to, DATA)
        


        header = 'To:' + ", ".join(emails) + '\n' + 'From: ' + FROM + '\n' + 'Subject: ' + subject + '\n'
        msg = header + '\n' + mail_text + '\n\n'
        server.sendmail(FROM, emails, msg)
        server.quit()
        server.close()

        #Die verbindung wird geschlossen
        server.close()
    def passwort_email(self,email):
        user = 'alisa6rieger@gmail.com'
        pwd = 'spuzunwyyivbpnbe'
        subject = 'Verifizierungs Email'

        p_email = "^([a-zA-Z0-9]+([-_\.]?[a-zA-Z0-9])+@[a-zA-Z0-9]+([-_\.]?[a-zA-Z0-9])+\.[a-z]{2,4}){0,}$"
        if not re.search(p_email,email):  
            #print('Keine gültige Email Adresse')
            return 'Keine gültige Email Adresse'
        self.db.connect()
        exist_email = self.db.select_email(email)
        self.db.close()
        exist_email = exist_email[0][0]
        if exist_email != 0:
            #eindeutige Nummer für die Passwort zurücksetzung wird erstellt.
            #im ergebnis steht die eindeutige nummer die als inhalt der email geschickt wird
            self.mail_text = ""
            for x in range(5):
                self.mail_text += str(random.randint(1,9))

            MAIL_FROM = user
            self.db.connect()
            #email = self.db.select_user_email(self.id)
            self.db.close()
            RCPT_TO  = email#[0][0]#email ist die Email vom User der das Passwort ändern möchte. Diese Information bekomme ich aus der DB
            DATA = 'From:%s\nTo:%s\nSubject:%s\n\n%s' % (MAIL_FROM, RCPT_TO, subject, self.mail_text)
            server = smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()
            server.login(user, pwd)
            server.sendmail(MAIL_FROM, RCPT_TO, DATA)
            server.quit()
            #Die verbindung wird geschlossen
            server.close()
        else:
            return "Diese E-Mail exestiert bei keinem Account"
    def code_pr(self, code):
        code = code.strip()#Leerzeichen werden am Anfang und am Ende entfernt
        if code == self.mail_text:
            return None
        else:
            return 'Code ist falsch und kann man jetzt nicht mehr verwenden'
    def neuse_passwort(self, pswt,pswt_w,email):
        fehlerfrei = "ok"
        #ein SQL-State wo das Passwort geändert wird
            
        p_pswd = "^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{6,}$"

        if pswt != pswt_w:#Hier wird geschaut ob in den Passwortfelder das gleiche drinnen steht, wenn nicht kommt eine Fehlermeldung
            fehler_medlung = "Fehler! Passwortfelder stimmen nicht überein."
            fehlerfrei = ""
            return fehler_medlung
                    #print(fehler_medlung)
        if not re.search(p_pswd,pswt):  
            #print('Keine gültiges Passwort! min. 6 Zeichen lang,min. 1 Großbuchstaben, min. 1 Kleinbuchstaben und min. 1 Ziffer enthalten.')
            fehlerfrei = ""
            return 'Keine gültiges Passwort! min. 6 Zeichen lang,min. 1 Großbuchstaben, min. 1 Kleinbuchstaben und min. 1 Ziffer enthalten.'
        if fehlerfrei == 'ok':
            self.db.connect()

            pswd_byte = pswt.encode('ascii')
            encoded_byte = base64.b64encode(pswd_byte)
            encoded_pswd = encoded_byte.decode('ascii')
            
            self.db.update_pswd(encoded_pswd,email)
            self.db.close()
                #print('Passwort wurde zurückgesetzt')
    
            

    def evinput(self, name, datum, zeit):
        #Checkt ob das Datum richtig formatiert ist, falls nicht, wird es korregiert. (YYYY-MM-DD)
        fehler = None
        for i in datum:
            if i == "/" or i == ".":
                datum = datum.replace(i, "-")

        #Checkt, ob das Datum im "date"-Format der MySQL Datenbank geschrieben wurde.
        date_p = "^\d{4}(?P<sep>[\/.-])\d{2}(?P=sep)(\d{2})$"
        date = re.match(date_p, datum)
                
        #Falls alle Daten nicht None sind, wird das Event hinzugefügt.
        if date != None and name != None and zeit != None:
            self.db.connect()
            self.db.eventinsert(name, datum, zeit)
            self.db.close()
            return fehler
                
        else:
            fehler = "Die Eingabe ist Fehlerhaft!"
            return fehler


    #Funktion um Events aus der Datenbank zu holen.
    def evoutput(self, name):
        
        if name != None:
            self.db.connect()
            out = self.db.eventoutput(name)
            output = []
            for i in out[0]:
                output.append(str(i))
            #print(output)
            self.db.close()
    def event(self):
        self.db.connect()
        out = self.db.eventout()
        output = []
        for i in out:
            output.append(i)
        self.db.close()
        return output
    def logout(self):
        self.id = None




surface = Tk()
Website = GUI(surface)
Website.login()



#es hat gepusht