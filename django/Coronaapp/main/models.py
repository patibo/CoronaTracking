from django.db import models

# Create your models here.
class ToDoList(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Item(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    complete = models.BooleanField()

    def __str__(self):
        return self.text

class Kunden(models.Model):
    kunden_id = models.AutoField(primary_key=True)
    benutzername = models.CharField(max_length=16)
    vorname = models.CharField(max_length=20)
    nachname = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    passwort = models.CharField(max_length=32)

    def __str__(self):
        return str(self.kunden_id) + ' ' + self.vorname + ' ' + self.nachname


class EventsEntry(models.Model):
    event_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=70)
    datum = models.DateField()
    zeit = models.TimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.name


class KundenEvents(models.Model):
    kID = models.ForeignKey(Kunden, on_delete=models.CASCADE)
    eID = models.ForeignKey(EventsEntry, on_delete=models.CASCADE)

    def __str__(self):
        return self.kID + ' ' + self.eID
