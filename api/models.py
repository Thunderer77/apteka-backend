from django.db import models


class User(models.Model):
    name = models.CharField(max_length=30)
    s_name = models.CharField(max_length=30)
    birth = models.DateField()
    gender = models.CharField(max_length=3)
    login = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    role = models.IntegerField()
    balance = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} {self.s_name}"


class Checks(models.Model):
    pat_id = models.ForeignKey(User, on_delete=models.CASCADE)
    sum = models.DecimalField(max_digits=10, decimal_places=3)

    def __str__(self):
        return f"Check Number: {self.sum} {self.pat_id}"


class Medicine(models.Model):
    med_n = models.CharField(max_length=30)
    dose = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=3)
    until = models.DateField()
    dev = models.CharField(max_length=30)
    effect = models.CharField(max_length=100)
    others = models.CharField(max_length=100)
    amount = models.IntegerField()

    def __str__(self):
        return f'{self.med_n} {self.dose}'

class Recipes(models.Model):
    pat_id = models.ForeignKey(User, on_delete=models.CASCADE)
    m_id = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    r_dose = models.IntegerField()
    since = models.DateField()

    def __str__(self):
        return f"Pacient ID: {self.pat_id}"
