from django.db import models

class Emplpoyee(models.Model):

    name=models.CharField(max_length=200, null=True)

    designation=models.CharField(max_length=200 ,null=True)

    department=models.CharField(max_length=200 ,null=True)

    salary=models.PositiveIntegerField(null=True)

    contact=models.CharField(max_length=200, null=True)

    address=models.CharField(max_length=200, null=True)
