
#Passwort zurücksetzten
#es wird ein generierter code als email geschickt den man dann in die app eingeben muss
#Wichtig man kann nur einer Person eine Email schicken wenn diese Person d
import smtplib
import random

# der empfaenger der Email
empfaenger = input(str("Geben sie den Email-Empfaenger ein: "))
#der Email Sender \ Email Sender passwort
gmail__user = input(str("Geben sie ihre Email ein : "))
gmail__pwd = input(str("Geben sie ihr Passwort ein : "))
#Email Betreff\ Email Inhalt
email_subject = "Verifizierungs Email"

#eindeutige Nummer für die Passwort zurücksetzung wird erstellt.
#im ergebnis steht die eindeutige nummer die als inhalt der email geschickt wird
ergebnis = ""
for x in range(5):
  ergebnis += str(random.randint(1,9))



#Es wird eine Verbindung zu smtpserver hergestellt
smtpserver = smtplib.SMTP("smtp.gmail.com",587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo
smtpserver.login(gmail__user, gmail__pwd)
header = 'To:' + empfaenger + '\n' + 'From: ' + gmail__user + '\n' + "Subject:" + email_subject + "\n"
msg = header + "\n " + ergebnis + " \n\n"
smtpserver.sendmail(gmail__user, empfaenger, msg)
print (header)
print ('done!')
#Die verbindung wird geschlossen
smtpserver.close()
