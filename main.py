import re  # Bibliothek regex wird importiert. Ist für die Überprüfung der Eingaben.
import mysql.connector  # Bibliothek mysql wird importiert. Ist für die Verbindung zur Datenbank.
import datetime  # Bibliothek datetime wird importiert. Ist für die Prüfung vom Geburtsdatum.
import smtplib  # Bibliothek smtplib wird importiert. Ist für den Zugriff und versendung der E-Mails zuständig.
import random  # Bibliothek random wird importiert.Ist für die 5 Stellige Verefezierung für Passwort zurücksetzen.
import base64  # Bibliothek für die Verschlüsselung
from tkinter import *  # Bibliothek für die Obrfläche
from tkinter import messagebox


class GUI:  # Klasse der Oberfläche
    def __init__(self, surface):
        self.backend = Backend()  # zugriff auf die Klasse Backend
        """ GUI Fenster """
        self.surface = surface
        self.title = 'Coronatracking-App'
        self.surface.title(self.title)
        # Hier werden alle Labels, Enterys, etc. erstellt die jemals im Programm verwendet wird, ohne ihre Eigenschaft zu bestimmen also Text, Farbe, usw.
        """ Hauptseit: Listenbox """
        self.listbox = Listbox(self.surface)
        # self.index = None
        # self.inhalt = None
        self.scroll = Scrollbar(self.surface, orient=VERTICAL)

        # regestrierung
        self.benutzername = Label(self.surface)
        self.pswt = Label(self.surface)
        self.pswt_w = Label(self.surface)
        self.vorname = Label(self.surface)
        self.nachname = Label(self.surface)
        self.email_r = Label(self.surface)

        self.e_benutzername = Entry(self.surface)
        self.e_pswt = Entry(self.surface, show="*")
        self.e_pswt_w = Entry(self.surface, show="*")
        self.e_vorname = Entry(self.surface)
        self.e_nachname = Entry(self.surface)
        self.e_email = Entry(self.surface)

        self.b_save = Button(self.surface)

        self.fehler = Label(self.surface)
        # login
        self.userLabel = Label(self.surface)
        self.userEntry = Entry(self.surface)
        self.passLabel = Label(self.surface)
        self.passEntry = Entry(self.surface, show="*")

        self.b_regestrieren = Button(self.surface)
        self.b_login = Button(self.surface)
        self.b_pswt_return = Button(self.surface)
        # startseite
        self.t_verlauf = Label(self.surface)

        self.b_logout = Button(self.surface)

        # Events erstellen (GUI Fenster)
        self.name = Label(self.surface)
        self.datum = Label(self.surface)
        self.zeit = Label(self.surface)

        self.ev_name = Entry(self.surface)
        self.ev_datum = Entry(self.surface)
        self.ev_zeit = Entry(self.surface)

        self.ev_error = Label(self.surface)
        # Event_hinzufügen
        self.ev_title = Label(self.surface)
        self.ev_createbutton = Button(self.surface)
        self.ev_cancelbutton = Button(self.surface)
        # email
        self.b_verdachtsfall = Button(self.surface)
        # event regestrieren
        self.b_regestrieren_event = Button(self.surface)

        self.var_event_auswahl = StringVar(self.surface)
        self.event_l = Label(self.surface)
        self.event_om = Label(self.surface)
        self.event_b = Button(self.surface)

        # passwort zurücksetzen
        self.pvLabel = Label(self.surface)
        self.emailLabel = Label(self.surface)
        self.psLabel = Label(self.surface)
        self.codeLabel = Label(self.surface)

        self.email = Entry(self.surface)

        self.pv_pass = Entry(self.surface, show="*")
        self.pv_passw = Entry(self.surface, show="*")
        self.pv_code = Entry(self.surface)
        self.pv_email = Entry(self.surface)
        self.pv_button = Button(self.surface)
        self.pv_stop = Button(self.surface)

        self.email_adress = None

    def menubar(self):
        menubar = Menu(self.surface)

        menubar.add_command(label="Registrieren", command=self.regestrieren)
        menubar.add_command(label="Login", command=self.login)

        self.surface.config(menu=menubar)

    def menubar2(self):
        menubar = Menu(self.surface)

        menubar.add_command(label="Home", command=self.main)
        menubar.add_command(label="Event Anmeldung", command=self.event_reservieren)

        menubar.add_command(label="Logout", command=self.logout)

        self.surface.config(menu=menubar)


    def menubar3(self):
        menubar = Menu(self.surface)

        menubar.add_command(label="Home", command=self.main)
        menubar.add_command(label="Event Anmeldung", command=self.event_reservieren)

        menubar.add_command(label="Logout", command=self.logout)

        self.surface.config(menu=menubar)
        self.clear_design()

    def clear_design(self):
        # hier werden alle Labels, Enterys, etc. ausgeblendet
        """ Hauptseit: Listenbox """
        self.listbox.grid_forget()
        self.scroll.grid_forget()

        # regestrieren
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
        # login
        self.userLabel.grid_forget()
        self.userEntry.grid_forget()
        self.passLabel.grid_forget()
        self.passEntry.grid_forget()

        self.b_regestrieren.grid_forget()
        self.b_login.grid_forget()
        self.b_pswt_return.grid_forget()

        # startseite
        self.t_verlauf.grid_forget()

        self.b_logout.grid_forget()

        # Events .grid_forget()
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

        # email
        self.b_verdachtsfall.grid_forget()

        # event regestrieren
        self.b_regestrieren_event.grid_forget()

        self.event_l.grid_forget()
        self.event_om.grid_forget()
        self.event_b.grid_forget()

        # passwort zurücksetzen
        self.pvLabel.grid_forget()
        self.emailLabel.grid_forget()
        self.psLabel.grid_forget()
        self.codeLabel.grid_forget()
        self.email.grid_forget()

        self.pv_pass.grid_forget()
        self.pv_passw.grid_forget()
        self.pv_code.grid_forget()
        self.pv_email.grid_forget()
        self.pv_button.grid_forget()
        self.pv_stop.grid_forget()

    def regestrieren(self):


        self.clear_design()  # ganzer Inhalt des Fensters wird ausgeblendet
        # der Text der Labels werden geändert
        self.benutzername.config(text='Benutzername:', bg="#005ca9", fg="white", padx=140)
        self.pswt.config(text='Passwort:', bg="#005ca9", fg="white")
        self.pswt_w.config(text='Passwort wiederholen:', bg="#005ca9", fg="white")
        self.vorname.config(text='Vorname:', bg="#005ca9", fg="white")
        self.nachname.config(text='Nachname:', bg="#005ca9", fg="white")
        self.email_r.config(text='Email:', bg="#005ca9", fg="white")

        # Labels,Enterys, Buttons werden hier positioniert
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

        self.b_save.config(text='Erstellen', command=self.benutzer_erstellen,bg="green",padx=36,pady=6)  # der Text vom Button wird geändert und festgelegt welche Methode aufgerufen wird, wenn der Button geklickt wird
        self.b_save.grid(row=18, column=2, pady=(12))
        self.fehler.grid(row=19, column=2, columnspan=30)


    def benutzer_erstellen(self):
        # Inahlter der Eingabefelder werden rausgehohlt
        benutzername = self.e_benutzername.get()
        pswt = self.e_pswt.get()
        pswt_w = self.e_pswt_w.get()
        vorname = self.e_vorname.get()
        nachname = self.e_nachname.get()
        email = self.e_email.get()
        # Eingaben werden überprüft
        fehler_text = self.backend.neu(benutzername, pswt, pswt_w, vorname, nachname, email)

        if fehler_text != None:  # Gibt es einen Fehler wird die Meldung angezeigt und man kommt nicht weiter
            self.fehler.config(text=fehler_text,bg="red")

            self.regestrieren()
        else:  # Inhalte der Eingabefelder werden entleert, Text vom Lable fehler wird geändert, man kommt auf die login Seite zurück
            self.fehler.config(text='',bg="#005ca9")
            self.e_benutzername.delete(0, 'end')
            self.e_pswt.delete(0, 'end')
            self.e_pswt_w.delete(0, 'end')
            self.e_vorname.delete(0, 'end')
            self.e_nachname.delete(0, 'end')
            self.e_email.delete(0, 'end')
            self.login()

    def fehler_text_leer_regestrieren(self):
        """die Eingabefelder Benutzername/E-Mail und Passwort auf der Login Seite werden geleert und die Fehlermeldung ausgeblendet. Dann wird die regestrier Seite geöffnet/aufgerufen"""
        self.fehler.config(text='',bg="#005ca9")
        self.userEntry.delete(0, 'end')
        self.passEntry.delete(0, 'end')
        self.regestrieren()

    def fehler_text_leer_pswt_r(self):
        """die Eingabefelder Benutzername/E-Mail und Passwort auf der Login Seite werden geleert und die Fehlermeldung ausgeblendet. Dann wird die Passwort zurücksetzen Seite geöffnet/aufgerufen"""
        self.fehler.config(text='',bg="#005ca9")
        self.userEntry.delete(0, 'end')
        self.passEntry.delete(0, 'end')
        self.pswt_r()

    def login(self):


        self.surface.configure(bg="#005ca9")  # hintergrundfrabe des fensters
        self.surface.geometry("800x360")  # größe des fensters
        self.clear_design()  # ganzer Inhalt des Fensters wird ausgeblendet
        self.menubar()  # menübar wird angezeigt
        self.clear_design()
        self.email.delete(0, 'end')  # das meist verwendte Eingabefeld für Passwort zurücksetzen wird hier entleert
        # der Text der Labels werden geändert
        self.userLabel.config(text="Email/Benutzername:", bg="#005ca9", fg="white",)
        self.passLabel.config(text="Passwort:", bg="#005ca9", fg="white")
        self.fehler.config(bg="#005ca9", fg="white")
        # die Labels werden positioniert
        self.userLabel.grid(row=1, column=0,padx=(240,0), pady=(120,0))
        self.userEntry.grid(row=1, column=1,pady=(120,0))
        self.passLabel.grid(row=2, column=0,padx=(240,0))
        self.passEntry.grid(row=2, column=1,pady=6)
        # die Eigenschaften der Buttons werden geändert
        #self.b_regestrieren.config(text='Regestrieren', command=self.fehler_text_leer_regestrieren, bg="green")
        self.b_login.config(text='Login', command=self.login_pr, bg="green",padx=44)
        self.b_pswt_return.config(text='Passwort zurücksetzen', command=self.fehler_text_leer_pswt_r, bg="#33ccff")
        # die Buttons werden positioniert
        #self.b_regestrieren.grid(row=4, column=1)
        self.b_login.grid(row=4, column=1, pady=3, )
        self.b_pswt_return.grid(row=3, column=1, pady= 3)
        self.fehler.grid(row=4, column=2)
        self.surface.mainloop()  # fenster schließt sich nicht automatisch

    def login_pr(self):
        user = self.userEntry.get()  # Inhalt des Eingabefeldes Benutzername/E-Mail auf der Login Seite
        pswt = self.passEntry.get()  # Inhalt des Eingabefeldes Passwort auf der Login Seite
        fehler_text = self.backend.anmelden(user, pswt)  # geprüft ob die Eingaben passen

        if fehler_text != None:  # wenn fehler zurückgegeben wird, dann wird dieser Fehler angezeigt und man kommt auf die Login Seite zurück
            # print(fehler_text)
            self.fehler.config(text=fehler_text,bg='red')

            self.login()
        else:  # kein Fehler zurückgegeben
            self.fehler.config(text='',bg="#005ca9")  # Fehlermeldung ausgeblendet
            self.userEntry.delete(0, 'end')  # Eingabefeld wird geleert
            self.passEntry.delete(0, 'end')  # Eingabefeld wird geleert
            self.main()  # Starseite wird aufgerufen/geöffnet

    def main(self):
        self.clear_design()  # Seite wird geleert
        self.menubar2()  # Menübar wird angezeig
        self.listbox.delete(0, 'end')  # alter Listbox stand wird gelöscht

        """Scrollbar wird zur Listbox hinzugefügt"""
        self.listbox["yscrollcommand"] = self.scroll.set
        self.scroll["command"] = self.listbox.yview

        for i in self.backend.kundenevent():  # die aktueller Verlauf es Kunden wird in der Listbox angezeigt
            text = i[1] + " am " + str(i[2]) + " um " + str(i[3])  # 1 ist Eventname, 2 ist Eventdatum, 3 ist Eventzeit
            self.listbox.insert(END, text)
        # positionierung der Listbox und Scrollbar
        self.listbox.grid(row=1, column=1, columnspan=10, sticky=N + E + S + W,padx=20)
        self.scroll.grid(row=1, column=10, sticky=E + N + S,)
        self.t_verlauf.config(text='Verlauf', font="Helvetica 16 bold italic", bg="#005ca9", fg="white",padx=190,pady=10)  # Überschrift

        self.t_verlauf.grid(row=0, column=1,pady=(0,10))  # Überschrift positionieren
        # self.b_logout.grid(row = 3, column=11)
        # self.b_logout.config(text='Abmelden',command=self.logout)
        self.b_verdachtsfall.config(text='Corona Fall melden', command=self.verdachtsfall, bg='red', fg='white',
                                    pady="24", padx=30)
        self.b_verdachtsfall.grid(row=2, column=12,padx=100)
        # self.b_regestrieren_event.config(text='Event reservieren',command=self.event_reservieren)
        # self.b_regestrieren_event.grid(row = 13, column=3)

    def event_reservieren(self):
        self.clear_design()  # Seite wird geleert
        self.menubar3()  # menübar wird angezeigt
        self.var_event_auswahl.set("Events")  # String wird auf Events gestellt

        self.event_l.config(text='Select One', width=10, bg="#005ca9", fg= "white" )
        self.event_l.grid(row=2, column=1)
        liste = self.backend.event()  # Alle Events mit ihren Informationen
        self.event_om = OptionMenu(self.surface, self.var_event_auswahl, *liste)  # OptionMenu wird erstellt, in self.var_event_auswahl wird die ausgewählte Event(value) eingetragen
        self.event_om.grid(row=2, column=2)

        self.event_b.config(text='Bestätigen', command=self.reservieren, bg="green", pady=10)
        self.event_b.grid(row=3, column=2)

      

    def reservieren(self):
        name = self.var_event_auswahl.get()  # ausgewählter Event, ist ein string
        self.backend.db.connect()  # Verbindung zu DB erstellt
        verlauf = self.backend.db.verlauf(
            self.backend.id)  # alle Events die der Kunde reserviert hat werden in verlauf gespeichert
        self.backend.db.close()  # verbindung zu DB getrennt
        ok = 0
        for i in verlauf:  # jedes einzelne Event wird durchgegangen
            if i[
                1] in name:  # hat der Kunde schon das ausgewählte event reserviert, kommt diese Meldung, 0 = eventid, 1 = eventname
                messagebox.showinfo('Event reservieren', 'Für dieses Event haben sie schon reserviert.')
                ok = 1
                break
        if ok == 0:
            events = self.backend.event()  # in evenst stehen alle Events mit ihren Informationen
            for i in events:  # jedes event wird einzeln durchgegangen
                if i[0] in name:  # das richtige event wird gesucht, 0 = eventname
                    self.backend.event_res(i[0])
            self.main()  # Starseite wird aufgerufen
        else:
            self.event_reservieren()  # Seite reservieren wird aufgerufen

    def verdachtsfall(self):
        MsgBox = messagebox.askquestion('Corona Fall melden','Sind Sie sich sicher, dass Sie einen Corona Fall melden möchten?',icon='warning')
        if MsgBox == 'yes':
            self.backend.mail()  # Email wird versendet
            messagebox.showinfo('Bestätigung', 'Die warn E-Mails wurden versendet')
            self.main()  # Startseite
        else:
            self.main()  # Starseite

    def logout(self):
        self.backend.logout()  # kunden id wird auf none gesetzt
        self.login()  # login Seite wird aufgerufen

    def pswt_r(self):
        self.clear_design()  # Seite wird geleert
        self.emailLabel.config(text="Geben sie bitte ihre Email-Adresse ihres Accounts an:", bg="#005ca9", fg="white",
                               padx=270,)
        # Eigenschaften ändern
        self.pv_button.config(text="Senden", command=self.email_p,bg = "green" ,padx=30, fg="white"  )
        self.pv_stop.config(text="Abbrechen", command=self.login, bg= "red", fg="white",padx=19)
        # positionierungen
        self.emailLabel.grid(row=1, column=1,pady=(100,0))
        self.email.grid(row=2, column=1)
        self.pv_button.grid(row=3, column=1, pady=3 )
        self.pv_stop.grid(row=4, column=1,pady=3)
        self.fehler.grid(row=5, column=1)

    def email_p(self):
        email = self.email.get()  # E-Mail-Adresse
        fehler_text = self.backend.passwort_email(email)
        if fehler_text != None:  # Gibt es einen Fehler wird die Meldung angezeigt und man kommt nicht weiter
            self.fehler.config(text=fehler_textbg="red")
            self.pswt_r()
        else:  # Inhalte der Eingabefelder werden entleert, Text vom Lable fehler wird geändert
            self.fehler.config(text='',bg="#005ca9")
            self.email_adress = self.email.get()  # E-Mail-Adresse, brauche ich für das Passwort update
            self.email.delete(0, 'end')
            self.verifiziercode()

    def verifiziercode(self):
        self.clear_design()
        # Eigenschaften ändern
        self.psLabel.config(text="Geben sie den 5-stellingen Code der ihnen per Email gesendet wurde", bg="#005ca9",padx=220, fg= "white")
        self.pv_button.config(text="Bestätigen", command=self.code_p, padx=23)
        # self.pv_stop.config(text="Abbrechen", command=self.login)
        # positionierung
        self.psLabel.grid(row=1, column=1, pady=(110,0))
        self.email.grid(row=2, column=1)
        self.pv_button.grid(row=3, column=1, pady=3)
        self.pv_stop.grid(row=4, column=1)
        self.fehler.grid(row=5, column=0)

    def code_p(self):
        code = self.email.get()  # Code vom Eingabefeld
        fehler_text = self.backend.code_pr(code)
        if fehler_text != None:  # Gibt es einen Fehler wird die Meldung angezeigt und man kommt nicht weiter
            messagebox.showinfo('Code ist falsch', fehler_text)
            self.email.delete(0, 'end')
            self.login()
        else:  # Inhalte der Eingabefelder werden entleert, Text vom Lable fehler wird geändert
            self.email.delete(0, 'end')
            self.zuruecksetzen()

    def zuruecksetzen(self):
        self.clear_design()
        self.psLabel.config(text="Geben sie das neue Passwort ein:", bg="#005ca9", padx=300)
        # Eigenschaften ändern
        self.pv_button.config(text="Bestätigen", command=self.neu_pswt_p)

        # self.pv_stop.config(text="Abbrechen", command=self.login)
        # positionierung
        self.psLabel.grid(row=0, column=0, pady=(120,0))
        self.pv_pass.grid(row=1, column=0, pady=3)
        self.pv_passw.grid(row=2, column=0)
        self.pv_button.grid(row=3, column=0, pady=3)
        # self.pv_stop.grid(row=3, column=1)

    def neu_pswt_p(self):
        pswt = self.pv_pass.get()  # Passwort
        pswt_w = self.pv_passw.get()  # Password wiederholen
        fehler_text = self.backend.neuse_passwort(pswt, pswt_w, self.email_adress)
        if fehler_text != None:  # Gibt es einen Fehler wird die Meldung angezeigt und man kommt nicht weiter
            self.fehler.config(text=fehler_text,bg="red")
            self.zuruecksetzen()
        else:  # Inhalte der Eingabefelder werden entleert, Text vom Lable fehler wird geändert, man kommt auf die login Seite zurück
            self.fehler.config(text='',bg="#005ca9")
            self.pv_pass.delete(0, 'end')
            self.pv_passw.delete(0, 'end')
            self.login()

    # Fenster zum erstellen von Events
    def event_input(self):
        self.clear_design()
        # Eigenschaften ändern
        self.ev_title.config(text="Geben Sie die Info des Events das sie erstellen wollen an.", bg="#005ca9",
                             font="bold")
        self.name.config(text='Name:', bg="#005ca9")
        self.datum.config(text='Datum:', bg="#005ca9")
        self.zeit.config(text='Zeit:', bg="#005ca9")
        self.ev_createbutton.config(text="Bestätigen", command=self.event_erstellen)
        self.ev_cancelbutton.config(text="Abbrechen", command=self.main)
        self.ev_error.config(text="", bg="#005ca9", fg="red")
        # positionierung
        self.ev_title.grid(row=0, columnspan=20)
        self.name.grid(row=1, column=0)
        self.datum.grid(row=2, column=0)
        self.zeit.grid(row=3, column=0)

        self.ev_name.grid(row=1, column=1)
        self.ev_datum.grid(row=2, column=1)
        self.ev_zeit.grid(row=3, column=1)

        self.ev_createbutton.grid(row=4, column=1)
        self.ev_cancelbutton.grid(row=4, column=3)
        self.ev_error.grid(row=5, column=0, columnspan=5, sticky=N + S + E + W)

    def event_erstellen(self):
        # Input für den Eventnamen
        name = self.ev_name.get()
        # Input für das Eventdatum (YYYY-MM-DD Format, geht auch mit / oder .)
        datum = self.ev_datum.get()
        # Input für die Uhrzeit des Events (24:00 Format)
        zeit = self.ev_zeit.get()

        # Sind alle Felder ausgefüllt, wird das Event angelegt/erstellt.
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


class DB:  # Hier passiert alles was mit der DB zutun hat
    def __init__(self, user, pswd, host, port,
                 db):  # Hier werden die Informationen übergeben die ich für eine DB verbindung brauche
        self.config = {
            'user': user,
            'password': pswd,
            'host': host,
            'port': port,
            'database': db
        }
        self.mydb = None
        self.cur = None

    def connect(self):  # eine Verbindung zur DB wird erstellt
        self.mydb = mysql.connector.connect(**self.config)
        self.cur = self.mydb.cursor()

    def insert_kunde(self, benutzername, pswt, vorname, nachname, email):  # ein Neuer Kunde wird erstellt
        sql = "INSERT INTO `kunden`(`benutzername`, `passwort`, `vorname`, `nachname`, `email`) VALUES ('{}','{}','{}','{}','{}')".format(
            benutzername, pswt, vorname, nachname, email)
        self.cur.execute(sql)
        self.mydb.commit()

    def insert_kundenevent(self, kunden_id, event_id):  # Eintrag welcher Kunde zu welchen Event geht
        sql = "INSERT INTO `kundenevents` (`kID`, `eID`) VALUES ('{}', '{}');".format(kunden_id[0][0], event_id[0][0])
        self.cur.execute(sql)
        self.mydb.commit()

    def select_pswd(self, benutzername_email):  # Hier wird das Passwort zurückgegeben was ich für die Anmeldung brauche
        sql = "SELECT passwort FROM `kunden` WHERE benutzername = '{}' or email = '{}'".format(benutzername_email,
                                                                                               benutzername_email)
        self.cur.execute(sql)
        return self.cur.fetchall()

    def select_id(self, benutzername_email, pswd):  # die ID vom Kunden wird ausgegeben
        sql = "SELECT id FROM kunden WHERE (`benutzername`='{}' or `email`='{}') and `passwort` = '{}' ".format(
            benutzername_email, benutzername_email, pswd)
        self.cur.execute(sql)
        return self.cur.fetchall()

    def select_benutzername(self,
                            benutzername):  # hier wird geschaut ob es Informationen zum Benutzer gibt bzw. ob dieser Benutzername schon exestiert
        sql = "SELECT COUNT(*) FROM kunden WHERE benutzername = '{}' ".format(benutzername)
        self.cur.execute(sql)
        return self.cur.fetchall()

    def select_email(self,
                     email):  # hier wird geschaut ob es Informationen zur Email gibt bzw. ob diese Email schon exestiert
        sql = "SELECT COUNT(*) FROM kunden WHERE email = '{}' ".format(email)
        self.cur.execute(sql)
        return self.cur.fetchall()

    def select_mail(self, kunden_id,
                    date):  # alle Emails von Kunden die bei den gleichen Events waren ab einem gewissen Datum wie auch der User war werden ausgegeben
        sql = "SELECT kunden.`email` FROM kunden JOIN kundenevents ON kunden.id=kundenevents.kID JOIN eventsentry on eventsentry.id = kundenevents.eID WHERE kunden.id != {} and eventsentry.datum >='{}'and eventsentry.id IN(SELECT eventsentry.id FROM eventsentry JOIN kundenevents ON eventsentry.id=kundenevents.eID JOIN kunden on kunden.id = kundenevents.kID WHERE kunden.id = {} and eventsentry.datum >='{}')".format(
            kunden_id[0][0], date, kunden_id[0][0], date)
        self.cur.execute(sql)
        return self.cur.fetchall()

    def select_event_mail(self, kunden_id,
                          date):  # alle Events die der User ab einen gewissen Datum reserviert hat, werden ausgegeben
        sql = "SELECT eventsentry.name,eventsentry.datum,eventsentry.zeit FROM eventsentry JOIN kundenevents ON eventsentry.id=kundenevents.eID JOIN kunden on kunden.id = kundenevents.kID WHERE kunden.id = {} and eventsentry.datum >= '{}'".format(
            kunden_id[0][0], date)
        self.cur.execute(sql)
        return self.cur.fetchall()

    def select_user_email(self, kunden_id):  # email von user wid ausgegeben
        sql = "SELECT `email` FROM kunden WHERE id = {}".format(kunden_id)
        self.cur.execute(sql)
        return self.cur.fetchall()

    def update_pswd(self, pswd, email):  # passwort wird geändert
        sql = "UPDATE `kunden` SET `passwort`='{}' WHERE `email` = '{}'".format(pswd, email)
        self.cur.execute(sql)
        self.mydb.commit()

    def close(self):  # die Verbindung zur DB wird getrennt
        self.cur.close()
        self.mydb.close()

    def eventinsert(self, name, datum, zeit):  # Neues Event anlegen
        sql = "INSERT INTO `eventsentry`(`name`, `datum`, `zeit`) VALUES ('{}', '{}', '{}')".format(name, datum, zeit)
        self.cur.execute(sql)
        self.mydb.commit()

    def eventoutput(self, name):  # alle Informatione zu einem gewissen Event werden ausgegeben
        sql = "SELECT * FROM `eventsentry` WHERE `eventsentry`.`name` = '{}'".format(name)
        self.cur.execute(sql)
        return self.cur.fetchall()

    def event_id(self, name):  # die ID zu einem gewissen Event wird ausgegeben
        sql = "SELECT id FROM `eventsentry` WHERE `eventsentry`.`name` = '{}'".format(name)
        self.cur.execute(sql)
        return self.cur.fetchall()

    def eventout(self):  # alle Informatione von allen Events werden ausgegeben
        sql = "SELECT `name`,`datum`,`zeit` FROM `eventsentry`"
        self.cur.execute(sql)
        return self.cur.fetchall()

    def verlauf(self, kunden_id):  # alle Informationen von allen reservierten Evenst vom Kunden werden ausgegeben
        sql = "SELECT * FROM eventsentry WHERE id IN (SELECT eID FROM kundenevents WHERE kID = {})".format(
            kunden_id[0][0])
        self.cur.execute(sql)
        return self.cur.fetchall()


class Backend:  # Hier passiert alles was im hintergrund der Webseite
    def __init__(self):
        # ilirjan: 'root','15071998','localhost','3306','coronatracking'
        # alisa: 'root','root','localhost','8889','coronatracking'
        self.db = DB('root','root','localhost','8889','coronatracking')  # hier kann ich die Klasse DB verwenden bzw. hier wird sie aufgerufen
        self.id = None
        self.mail_text = ""

    def anmelden(self, benutzername_email, pswt):  # anmelde funktion

        fehlerfrei = "ok"

        benutzername_email = benutzername_email.strip()  # Leerzeichen werden am Anfang und am Ende entfernt
        self.db.connect()  # Verbindung zur DB wird erstellt
        pswd_sql = self.db.select_pswd(
            benutzername_email)  # das Passwort was zum Benutzername/E-Mail passt was in der DB gespeichert wurde wird hier zurückgegeben

        if len(pswd_sql) != 0:  # wenn Benutzername/Email exestiert
            # passwort wird entschlüsselt
            encoded_pswd = pswd_sql[0][0].encode('ascii')  # b'fdskjfsfj
            encoded_byte = base64.b64decode(encoded_pswd)  # b'hallo
            pswd = encoded_byte.decode('ascii')  # hallo

            if pswt != pswd:  # hier wird geschaut ob das Passwort im Eingabefeld das gleiche Passwort ist wie in der DB. Stimmt es nicht kommt eine Fehlermeldung.
                fehler_medlung = "Fehler! Benutzername/E-Mail oder Passwort stimmt nicht."
                fehlerfrei = ""
                return fehler_medlung

            if fehlerfrei == 'ok':  # ist kein fehler aufgetreten kommt man hier rein
                # print('benutz:',benutzername_email)
                # print(pswd)
                self.id = self.db.select_id(benutzername_email, pswd_sql[0][0])  # kunden id wird gespeichert
                # print('anmelden',self.id)
                self.db.close()  # Verbindung zur DB wird getrennt
        else:
            fehler_medlung = "Fehler! Benutzername/E-Mail oder Passwort stimmt nicht."
            fehlerfrei = ""
            return fehler_medlung

    def neu(self, benutzername, pswt, pswt_w, vorname, nachname, email):

        fehlerfrei = "ok"

        benutzername = benutzername.strip()  # Leerzeichen werden am Anfang und am Ende entfernt
        vorname = vorname.strip()  # Leerzeichen werden am Anfang und am Ende entfernt
        nachname = nachname.strip()  # Leerzeichen werden am Anfang und am Ende entfernt
        # regex prüfungen
        p_email = "^([a-zA-Z0-9]+([-_\.]?[a-zA-Z0-9])+@[a-zA-Z0-9]+([-_\.]?[a-zA-Z0-9])+\.[a-z]{2,4}){0,}$"
        p_name = "^[a-zA-ZäüöÄÜÖ]{,20}$"
        p_pswd = "^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,32}$"
        p_benutzername = "^[0-9A-Za-z]{,16}$"

        self.db.connect()  # verbindung zur DB wird erstellt
        exist_benutzername = self.db.select_benutzername(benutzername)
        exist_benutzername = exist_benutzername[0][0]
        if exist_benutzername != 0:
            # print('Dieser Benutzername exestiert schon')
            fehlerfrei = ""
            return "Dieser Benutzername exestiert schon"
        if not re.search(p_benutzername, benutzername):
            fehlerfrei = ""
            # print('Keine gültiges Passwort! min. 6 Zeichen lang,min. 1 Großbuchstaben, min. 1 Kleinbuchstaben und min. 1 Ziffer enthalten.')
            return 'Keine gültiger Benutzername! max. 16 Zeichen lang, nur Buchstaben und Zahlen erlaubt.'

        if pswt != pswt_w:  # Hier wird geschaut ob in den Passwortfelder das gleiche drinnen steht, wenn nicht kommt eine Fehlermeldung
            fehler_medlung = "Fehler! Passwortfelder stimmen nicht überein."
            fehlerfrei = ""
            # print(fehler_medlung)
            return fehler_medlung
        if not re.search(p_pswd, pswt):
            fehlerfrei = ""
            # print('Keine gültiges Passwort! min. 6 Zeichen lang,min. 1 Großbuchstaben, min. 1 Kleinbuchstaben und min. 1 Ziffer enthalten.')
            return 'Keine gültiges Passwort! min. 8 und max. 32 Zeichen lang,min.\n 1 Großbuchstaben, min. 1 Kleinbuchstaben und min. 1 Ziffer enthalten.'

        if not re.search(p_name, vorname):
            fehlerfrei = ""
            # print('Kein gültiger Vorname. Es sind nur Buchstaben erlaubt.')
            return 'Kein gültiger Vorname. Es sind nur Buchstaben erlaubt und darf nicht länger als 20 Zeichen lang sein.'
        if not re.search(p_name, nachname):
            fehlerfrei = ""
            # print('Kein gültiger Nachname. Es sind nur Buchstaben erlaubt.')
            return 'Kein gültiger Nachname. Es sind nur Buchstaben erlaubt und darf nicht länger als 20 Zeichen lang sein.'
        if not re.search(p_email, email):
            fehlerfrei = ""
            # print('Keine gültige Email Adresse')
            return 'Keine gültige Email Adresse'
        exist_email = self.db.select_email(email)
        exist_email = exist_email[0][0]
        if exist_email != 0:
            fehlerfrei = ""
            return "Diese E-Mail exestiert schon"

        if fehlerfrei == 'ok':
            # passwort wird verschlüsselt
            pswd_byte = pswt.encode('ascii')  # hallo
            encoded_byte = base64.b64encode(pswd_byte)  # b'hallo
            encoded_pswd = encoded_byte.decode('ascii')  # b'sdjkfsf

            self.db.insert_kunde(benutzername, encoded_pswd, vorname, nachname, email)  # neues Konot wird erstellt

            self.db.close()  # Verbindung zur DB wird getrentt

    def kunde_id(self, benutzername_email, pswt):  # kunden id wird rausgefunden und gespeichert
        self.db.connect()  # Verbindung zur DB wird erstellt
        self.id = self.db.select_id(benutzername_email, pswt)
        self.id = self.id[0][0]
        self.db.close()  # Verbindung zur DB wird getrent

    def event_res(self, name):  # eintrag welcher Kunde welches event reserviert hat
        self.db.connect()  # Verbindung zur DB wird erstellt

        # SQL-State wo ich die ID vom Event bekomme was ich auswähle
        e_id = self.db.event_id(name)
        self.db.insert_kundenevent(self.id, e_id)
        self.db.close()

    def kundenevent(self):  # Verlauf erstellen
        self.db.connect()  # Verbindung zur DB wird erstellt

        events = self.db.verlauf(self.id)  # alle reservierten Events vom user

        self.db.close()  # Verbindung zur DB wird getrent
        return events

    def mail(self):
        user = 'alisa6rieger@gmail.com'
        pwd = 'spuzunwyyivbpnbe'
        mail_text = 'Es gab einen Coronafall bei diesen Events:'
        subject = 'Warnung!'

        # emails sind alle Emails von den Usern, ausgenommen der die Meldung sendete, die auch bei den Events waren wo auch der erkrankte User 3 Tage vor dem 1 Syntom tag war
        heute = datetime.date.today()
        tage = datetime.timedelta(days=3)

        date = heute - tage
        self.db.connect()

        for i in self.db.select_event_mail(self.id,
                                           date):  # alle events die der user ab einem gewissen Datum reserviert hat
            for e in i:
                mail_text = mail_text + ' ' + str(e)  # event wird zum mail text hinzugefügt
            mail_text = mail_text + ','  # ein beistrich wird zum Text hinzugefügt
        mail_text = mail_text[:-1]  # der Letzte beistrich vom Text wird gelöscht
        emails = []
        for i in self.db.select_mail(self.id,
                                     date):  ##alle Emails von Kunden die bei den gleichen Events waren ab einem gewissen Datum wie auch der User war werden ausgegeben
            for e in i:
                emails.append(e)
        self.db.close()  # verbindung zur DB wird getrennt

        FROM = user
        # verbidnung zu meinen gmail konto zum email versenden
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(user, pwd)

        header = 'To:' + ", ".join(emails) + '\n' + 'From: ' + FROM + '\n' + 'Subject: ' + subject + '\n'
        msg = header + '\n' + mail_text + '\n\n'
        server.sendmail(FROM, emails, msg)
        server.quit()
        server.close()

        # Die verbindung wird geschlossen
        server.close()

    def passwort_email(self, email):
        user = 'alisa6rieger@gmail.com'
        pwd = 'spuzunwyyivbpnbe'
        subject = 'Verifizierungs Email'

        p_email = "^([a-zA-Z0-9]+([-_\.]?[a-zA-Z0-9])+@[a-zA-Z0-9]+([-_\.]?[a-zA-Z0-9])+\.[a-z]{2,4}){0,}$"  # regex überprüfung
        if not re.search(p_email, email):
            # print('Keine gültige Email Adresse')
            return 'Keine gültige Email Adresse'
        self.db.connect()
        exist_email = self.db.select_email(email)
        self.db.close()
        exist_email = exist_email[0][0]
        if exist_email != 0:
            # eindeutige Nummer für die Passwort zurücksetzung wird erstellt.
            # im ergebnis steht die eindeutige nummer die als inhalt der email geschickt wird
            self.mail_text = ""
            for x in range(5):
                self.mail_text += str(random.randint(1, 9))

            MAIL_FROM = user
            self.db.connect()
            # email = self.db.select_user_email(self.id)
            self.db.close()
            RCPT_TO = email  # [0][0]#email ist die Email vom User der das Passwort ändern möchte. Diese Information bekomme ich aus der DB
            DATA = 'From:%s\nTo:%s\nSubject:%s\n\n%s' % (MAIL_FROM, RCPT_TO, subject, self.mail_text)
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(user, pwd)
            server.sendmail(MAIL_FROM, RCPT_TO, DATA)
            server.quit()
            # Die verbindung wird geschlossen
            server.close()
        else:
            return "Diese E-Mail exestiert bei keinem Account"

    def code_pr(self, code):
        code = code.strip()  # Leerzeichen werden am Anfang und am Ende entfernt
        if code == self.mail_text:
            return None
        else:
            return 'Code ist falsch und kann man jetzt nicht mehr verwenden'

    def neuse_passwort(self, pswt, pswt_w, email):
        fehlerfrei = "ok"

        # regex überprüfung
        p_pswd = "^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{6,}$"

        if pswt != pswt_w:  # Hier wird geschaut ob in den Passwortfelder das gleiche drinnen steht, wenn nicht kommt eine Fehlermeldung
            fehler_medlung = "Fehler! Passwortfelder stimmen nicht überein."
            fehlerfrei = ""
            return fehler_medlung
            # print(fehler_medlung)
        if not re.search(p_pswd, pswt):
            # print('Keine gültiges Passwort! min. 6 Zeichen lang,min. 1 Großbuchstaben, min. 1 Kleinbuchstaben und min. 1 Ziffer enthalten.')
            fehlerfrei = ""
            return 'Keine gültiges Passwort! min. 6 Zeichen lang,min. 1 Großbuchstaben, min. 1 Kleinbuchstaben und min. 1 Ziffer enthalten.'
        if fehlerfrei == 'ok':
            self.db.connect()
            # passwort wird verschlüsselt
            pswd_byte = pswt.encode('ascii')
            encoded_byte = base64.b64encode(pswd_byte)
            encoded_pswd = encoded_byte.decode('ascii')

            self.db.update_pswd(encoded_pswd, email)  # passwort wird geändert
            self.db.close()
            # print('Passwort wurde zurückgesetzt')

    def evinput(self, name, datum, zeit):
        # Checkt ob das Datum richtig formatiert ist, falls nicht, wird es korregiert. (YYYY-MM-DD)
        fehler = None
        for i in datum:
            if i == "/" or i == ".":
                datum = datum.replace(i, "-")

        # Checkt, ob das Datum im "date"-Format der MySQL Datenbank geschrieben wurde.
        date_p = "^\d{4}(?P<sep>[\/.-])\d{2}(?P=sep)(\d{2})$"
        date = re.match(date_p, datum)

        # Falls alle Daten nicht None sind, wird das Event hinzugefügt.
        if date != None and name != None and zeit != None:
            self.db.connect()
            self.db.eventinsert(name, datum, zeit)
            self.db.close()
            return fehler

        else:
            fehler = "Die Eingabe ist Fehlerhaft!"
            return fehler

    def evoutput(self, name):  # Funktion um Events aus der Datenbank zu holen.

        if name != None:
            self.db.connect()
            out = self.db.eventoutput(name)
            output = []
            for i in out[0]:
                output.append(str(i))
            # print(output)
            self.db.close()

    def event(self):  # Funktion um Events aus der Datenbank zu holen.
        self.db.connect()
        out = self.db.eventout()  # alle Events mit deren Informationen
        output = []
        for i in out:
            output.append(i)
        self.db.close()
        return output

    def logout(self):
        self.id = None


surface = Tk()  # Fenster erstellt
Website = GUI(surface)  # Obejkt von der Klasse GUI erstellt
Website.login()  # Login Seite aufrufen/öffnen