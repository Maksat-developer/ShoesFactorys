
from django.db import models


class StatusProduct(models.Model):
    status_pr = models.CharField(
        verbose_name="Статус продукта:",
        max_length=50)

    class Meta:
        verbose_name = " Статус Продукта:"
        verbose_name_plural = "Статуса Продуктов:"

    def __str__(self):
        return self.status_pr


class ProductSale(models.Model):

    articul = models.CharField(max_length=100, verbose_name="articul")
    image = models.ImageField(
        verbose_name="Фотография продукта: ",
        upload_to="media/%Y/%m/%d")
    type_pr = models.CharField(verbose_name="Тип продукта:", max_length=100)
    size = models.PositiveSmallIntegerField(verbose_name="Размер продукта:")
    package = models.PositiveSmallIntegerField(
        verbose_name="Количество упаковок:")
    pair = models.PositiveSmallIntegerField(verbose_name="Количество пар:")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sum_pr = models.CharField(max_length=50,
                              verbose_name="Уточним что это поля должно быть:")
    status = models.ForeignKey(StatusProduct, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Продукт:"
        verbose_name_plural = "Продуктов:"

    def __str__(self):
        return str(self.articul) + ": $" + str(self.price)


class ProductModel(models.Model):
    type_pr = models.CharField(verbose_name="Тип продукта: ", max_length=100)
    date_published = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Модель продукта:"
        verbose_name_plural = "Модели продуктов:"
        ordering = ['id']

    def __str__(self):
        return self.type_pr


# fullname  = models.CharField(verbose_name="ФИО - Сотрудника:", max_length=200)

class Employee(models.Model):
    last_name = models.CharField(verbose_name="Фамилия:", max_length=150)
    first_name = models.CharField(verbose_name="Имя:", max_length=150)
    phone = models.CharField(max_length=50,
                             verbose_name="Контактный номер сотрудника:")
    date_register = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата регистрации:")

    class Meta:
        verbose_name = "Сотрудник:"
        verbose_name_plural = "Сотрудников:"
        ordering = ['id']

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"

    # def get_name(self):
    #     return '{0} {1}'.format(self.first_name, self.last_name)


class CounterpartiesRegion(models.Model):
    region_name = models.CharField(max_length=150, verbose_name="Регион")

    def __str__(self):
        return self.region_name

    class Meta:
        verbose_name = "Регион:"
        verbose_name_plural = "Регионов"
        ordering = ['id']


class Counterparties(models.Model):
    last_name = models.CharField(verbose_name="Фамилия:", max_length=150)
    first_name = models.CharField(verbose_name="Имя:", max_length=150)
    region = models.ForeignKey(CounterpartiesRegion, on_delete=models.CASCADE)
    phone = models.CharField(max_length=50,
                             verbose_name="Контактный номер контрагента:")

    class Meta:
        verbose_name = "Контрагент:"
        verbose_name_plural = "Контрагентов:"

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"
