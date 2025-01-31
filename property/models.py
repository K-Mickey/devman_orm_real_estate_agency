from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from phonenumber_field import modelfields


class Flat(models.Model):
    new_building = models.BooleanField(
        'Новостройка?',
        db_index=True,
        blank=True,
        null=True)
    created_at = models.DateTimeField(
        'Когда создано объявление',
        default=timezone.now,
        db_index=True)

    description = models.TextField('Текст объявления', blank=True)
    price = models.IntegerField('Цена квартиры', db_index=True)

    town = models.CharField(
        'Город, где находится квартира',
        max_length=50,
        db_index=True)
    town_district = models.CharField(
        'Район города, где находится квартира',
        max_length=50,
        blank=True,
        help_text='Чертаново Южное')
    address = models.TextField(
        'Адрес квартиры',
        help_text='ул. Подольских курсантов д.5 кв.4')
    floor = models.CharField(
        'Этаж',
        max_length=3,
        help_text='Первый этаж, последний этаж, пятый этаж')

    rooms_number = models.IntegerField(
        'Количество комнат в квартире',
        db_index=True)
    living_area = models.IntegerField(
        'количество жилых кв.метров',
        null=True,
        blank=True,
        db_index=True)

    has_balcony = models.NullBooleanField('Наличие балкона', db_index=True)
    active = models.BooleanField('Активно-ли объявление', db_index=True)
    construction_year = models.IntegerField(
        'Год постройки здания',
        null=True,
        blank=True,
        db_index=True)

    like = models.ManyToManyField(
        User,
        related_name='liked_flats',
        verbose_name='Кто лайкнул',
        blank=True)

    def __str__(self):
        return f'{self.town}, {self.address} ({self.price}р.)'

    class Meta:
        verbose_name = 'Квартира'
        verbose_name_plural = 'Квартиры'


class Complaint(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='complaints', verbose_name='Автор жалобы')
    flat = models.ForeignKey(
        Flat,
        on_delete=models.CASCADE,
        related_name='complaints',
        verbose_name='Квартира, на которую пожаловались')
    text = models.TextField(verbose_name='Текст жалобы')
    created_at = models.DateTimeField(
        'Когда создано жалоба',
        auto_now_add=True,
        db_index=True)

    def __str__(self):
        return f'{self.author}: {self.text[:20]}'

    class Meta:
        verbose_name = 'Жалоба'
        verbose_name_plural = 'Жалобы'
        ordering = ['-created_at']


class Owner(models.Model):
    name = models.CharField('ФИО владельца', max_length=200, db_index=True)
    phone_number = models.CharField('Номер владельца', max_length=20)
    pure_phone = modelfields.PhoneNumberField('Нормализованный номер владельца', blank=True, null=True)
    flat = models.ManyToManyField(
        Flat,
        verbose_name='Квартиры в собственности',
        related_name='owners',
        blank=True,
        db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Владелец'
        verbose_name_plural = 'Владельцы'
        ordering = ['name']
