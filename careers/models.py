from django.db import models
from datetime import date

class Customer(models.Model):
    name = models.CharField("Имя", max_length=150)
    phone = models.CharField("Телефон", max_length=12)
    email = models.CharField("Электронная почта", max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Покупатель"
        verbose_name_plural = "Покупатели"

class Owner(models.Model):
    name = models.CharField("Имя", max_length=150)
    phone = models.CharField("Телефон", max_length=12)
    email = models.CharField("Электронная почта", max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Владелец недвижимости"
        verbose_name_plural = "Владелец недвижимости"

class TypeRealty(models.Model):
    type_realty = models.CharField("Тип недвижимости", max_length=150)

    def __str__(self):
        return self.type_realty

    class Meta:
        verbose_name = "Тип недвижимости"
        verbose_name_plural = "Типы недвижимости"

class Realty(models.Model):
    title = models.CharField("Название", max_length=150)
    description = models.CharField("Описание", max_length=150)
    image = models.ImageField("Изображение", upload_to="media/", null=True)
    address = models.CharField("Адрес", max_length=150)
    price = models.PositiveSmallIntegerField("Стоимость", default=0)
    id_owner = models.ForeignKey(Owner, verbose_name="Владелец", on_delete=models.SET_NULL, null=True)
    id_type_realty = models.ForeignKey(TypeRealty, verbose_name="Тип недвижимости", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Недвижимость"
        verbose_name_plural = "Недвижимости"

STATUS_CHOICES = [
    ('rejected', 'Покупка не состоялась'),
    ('success', 'Покупка состоялась'),
    ('consideration', 'На рассмотрении'),
]

class RequestPurchase(models.Model):
    title = models.CharField("Название", max_length=150)
    status = models.CharField("Статус", max_length=150, choices=STATUS_CHOICES)
    id_customer = models.ForeignKey(Customer, verbose_name="Покупатель", on_delete=models.SET_NULL, null=True)
    id_realty = models.ForeignKey(Realty, verbose_name="Недвижимость", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Заявка на покупку"
        verbose_name_plural = "Заявки на покупку"

class ContractPurchase(models.Model):
    title = models.CharField("Название", max_length=150)
    file = models.FileField("Контракт купли-продажи", upload_to="uploads/", null=True)
    id_request = models.ForeignKey(RequestPurchase, verbose_name="Заявка на покупку", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Контракт купли-продажи"
        verbose_name_plural = "Данные о контрактах купли-продаже"

class AgencyRealtors(models.Model):
    name = models.CharField("Название", max_length=150)
    rating = models.CharField("Рейтинг", max_length=150)
    year_of_foundation = models.PositiveSmallIntegerField("Год основания", default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Риэлторское агенство"
        verbose_name_plural = "Риэлторские агенства"

class Realtors(models.Model):
    name = models.CharField("Имя", max_length=150)
    phone = models.CharField("Телефон", max_length=12)
    email = models.CharField("Электронная почта", max_length=150)
    rating = models.CharField("Рейтинг", max_length=150)
    id_agency = models.ForeignKey(AgencyRealtors, verbose_name="Риэлторское агенство", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Риэлтор"
        verbose_name_plural = "Риэлторы"

class RealtorServices(models.Model):
    title = models.CharField("Тип услуги", max_length=150)
    id_realtor = models.ForeignKey(Realtors, verbose_name="Риэлтор", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Риэлторская услуга"
        verbose_name_plural = "Риэлторские услуги"

class ContractServices(models.Model):
    title = models.CharField("Название", max_length=150)
    file = models.FileField("Контракт на оказание услуг", upload_to="uploads/", null=True)
    id_owner = models.ForeignKey(Owner, verbose_name="Владелец недвижимости", on_delete=models.SET_NULL, null=True)
    id_service = models.ForeignKey(RealtorServices, verbose_name="Риэлторская услуга", on_delete=models.SET_NULL, null=True)
    id_realtor = models.ForeignKey(Realtors, verbose_name="Риэлтор", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Контракт на оказание услуги"
        verbose_name_plural = "Данные о контрактах на оказание услуги"
