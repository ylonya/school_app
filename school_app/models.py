from django.db import models
from django.db.models import Model
from django.core.exceptions import ValidationError
import re

def validate_phone_number(value):
    pattern = r'^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$'
    if not re.match(pattern, value):
        raise ValidationError('Неверный формат номера телефона. Введите номер в формате +7XXXXXXXXXX или 8XXXXXXXXXX')

class Employee(models.Model):
    class Meta:
        db_table = "Employee"
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"
    
    last_name_emp = models.CharField(max_length=20)
    middle_name_emp = models.CharField(max_length=20)
    first_name_emp = models.CharField(max_length=20)
    date_birth_emp = models.DateField()
    email_emp = models.CharField(max_length=100)
    number_emp = models.CharField(max_length=15, validators=[validate_phone_number])
    passport_detail_emp = models.CharField(max_length=10)
    post = models.CharField(max_length=100)
    address_emp = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.last_name_emp} {self.middle_name_emp} {self.first_name_emp}"
    
    
class Pupil(models.Model):
    class Meta:
        db_table = "Pupil"
        verbose_name = "Ребёнок"
        verbose_name_plural = "Дети"

    last_name_pupil = models.CharField(max_length=20)
    middle_name_pupil = models.CharField(max_length=20)
    first_name_pupil = models.CharField(max_length=20)
    date_birth_pupil = models.DateField()
    date_reception = models.DateField()

    def __str__(self):
        return f"{self.last_name_pupil} {self.middle_name_pupil} {self.first_name_pupil}"
    
class Group(models.Model):
    class Meta:
        db_table = "Group"
        verbose_name = "Группа"
        verbose_name_plural = "Группы"

    pupil = models.ForeignKey(Pupil, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    bias = models.CharField(max_length=50)
    count = models.IntegerField()

    def __str__(self):
        return f"{"Группа направленности: "} {self.bias}"
    


class Parent(models.Model):
    class Meta:
        db_table = "Parent"
        verbose_name = "Родитель"
        verbose_name_plural = "Родители"

    pupil = models.ForeignKey(Pupil, on_delete=models.CASCADE)
    last_name_parent = models.CharField(max_length=20)
    middle_name_parent = models.CharField(max_length=20)
    first_name_parent = models.CharField(max_length=20)
    date_birth_parent = models.DateField()
    passport_detail_parent = models.CharField(max_length=10)
    address_parent = models.CharField(max_length=200)
    number_parent = models.CharField(max_length=12, validators=[validate_phone_number])

    def __str__(self):
        return f"{self.last_name_parent} {self.middle_name_parent} {self.first_name_parent}"

class Application(models.Model):
    class Meta:
        db_table = "Application"
        verbose_name = "Заявление"
        verbose_name_plural = "Заявления"

    class Status(models.IntegerChoices):
        IN_PROGRESS = 1, 'In progress'
        REFUSED = 2, 'Refused'
        EXECUTED = 3, 'Executed'
    
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
    status = models.IntegerField(choices=Status.choices)
    date = models.DateField()

    def __str__(self):
        return f"{"Заявление от "} {self.date}"
    


class Document(models.Model):
    class Meta:
        db_table = "Document"
        verbose_name = "Документ"
        verbose_name_plural = "Документы"

    class Status(models.IntegerChoices):
        IN_PROGRESS = 1, 'In progress'
        REFUSED = 2, 'Refused'
        EXECUTED = 3, 'Executed'
        SIGNED = 4, 'Signed'

    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
    pupil = models.ForeignKey(Pupil, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    status = models.IntegerField(choices=Status.choices)
    date = models.DateField()

    def __str__(self):
        return f"{"Документ от "} {self.date}"






