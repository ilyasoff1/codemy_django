from django.db import models


class Venue(models.Model):
    name = models.CharField(max_length=120)
    address = models.CharField(max_length=120)
    zip_code = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    web = models.URLField()
    email = models.EmailField()

    def __str__(self):
        return self.name


class MyClubUser(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Events(models.Model):
    name = models.CharField(max_length=120)
    event_date = models.DateTimeField()
    venue = models.ForeignKey(Venue, blank=True, null=True, on_delete=models.CASCADE)
    manager = models.CharField(max_length=60)
    description = models.TextField(blank=True)
    attendees = models.ManyToManyField(MyClubUser, blank=True, null=True)

    def __str__(self):
        return self.name
