from django.db import models


# Create your models here.
class Categori(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Project(models.Model):
    category = models.ForeignKey(Categori, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255)
    company = models.CharField(max_length=255, null=True, blank=True)
    url = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True)
    pic = models.ImageField(upload_to='images/projects', null=True, blank=True)

    def __str__(self):
        return f"{self.name} for {self.company}"


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return f"{self.name} by {self.subject}"


class Testimonial(models.Model):
    name = models.CharField(max_length=255)
    occupation = models.CharField(max_length=255, null=True, blank=True)
    message = models.TextField()
    image = models.ImageField(upload_to='images/testimonial', null=True, blank=True)

    def __str__(self):
        return f"{self.name}"