from django.db import models

# This is a student class and each student should only have one of these
# The student class has major, name, email, major
class Student(models.Model):
    MAJOR = (
        ("CSCI-BS", "BS in Computer Science"),
        ("CPEN-BS", "BS in Computer Engineering"),
        ("BIGD-BI", "BI in Game Design and Development"),
        ("BICS-BI", "BI in Computer Science"),
        ("BISC-BI", "BI in Computer Security"),
        ("CSCI-BA", "BA in Computer Science"),
        ("DASE-BS", "BS in Data Analytics and Systems Engineering"),
    )

    name = models.CharField(max_length=200)
    email = models.EmailField("MSU Email")
    major = models.CharField(max_length=200, choices=MAJOR, blank=True)

    # What is shown when the class is printed
    def __str__(self):
        return self.name


# This is the portfolio class
# It has student, title, contact_email, is_active, and about
class Portfolio(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    contact_email = models.EmailField()
    is_active = models.BooleanField(default=True)
    about = models.TextField(blank=True)

    # What is shown when the class is printed
    def __str__(self):
        return self.title


