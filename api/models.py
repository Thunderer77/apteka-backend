from django.db import models


class User(models.Model):
    name = models.CharField(max_length=30, verbose_name="Имя")
    s_name = models.CharField(max_length=30, verbose_name="Фамилия")
    birth = models.DateField(verbose_name="Дата рождения")
    gender = models.CharField(max_length=3, verbose_name="Пол")
    login = models.CharField(max_length=30, verbose_name="Логин")
    password = models.CharField(max_length=30, verbose_name="Пароль")
    role = models.IntegerField(verbose_name="Роль")
    balance = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Баланс")

    def __str__(self):
        return f"{self.name} {self.s_name}"

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Checks(models.Model):
    pat_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    sum = models.DecimalField(max_digits=10, decimal_places=3, verbose_name="Сумма чека")

    def __str__(self):
        return f"Чек: {self.sum}"

    class Meta:
        verbose_name = "Чек"
        verbose_name_plural = "Чеки"


class Medicine(models.Model):
    med_n = models.CharField(max_length=30, verbose_name="Название")
    dose = models.IntegerField(verbose_name="Дозировка", )
    price = models.DecimalField(max_digits=10, decimal_places=3, verbose_name="Цена")
    until = models.DateField(verbose_name="Действительно до")
    dev = models.CharField(max_length=30, verbose_name="Производитель")
    effect = models.CharField(max_length=100, verbose_name="Эффект")
    others = models.CharField(max_length=100, verbose_name="Другие аспекты")
    amount = models.IntegerField(verbose_name="Количество")

    def __str__(self):
        return f"{self.med_n} {self.dose}"

    class Meta:
        verbose_name = "Лекарство"
        verbose_name_plural = "Лекарства"


class Recipes(models.Model):
    pat_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    m_id = models.ForeignKey(Medicine, on_delete=models.CASCADE, verbose_name="Лекарство")
    r_dose = models.IntegerField(verbose_name="Дозировка рецепта")
    since = models.DateField(verbose_name="Начиная с")
    until = models.DateField(verbose_name="Действительно до")

    def __str__(self):
        return f"Рецепт для: {self.pat_id}"

    class Meta:
        verbose_name = "Рецепт"
        verbose_name_plural = "Рецепты"
