from django.db import models
from simple_history.models import HistoricalRecords


class Tarifs(models.Model):
    title = models.CharField(verbose_name='Тариф', max_length=100)
    description = models.CharField(verbose_name='Описание', max_length=100)
    price = models.IntegerField(verbose_name='Цена')

    history = HistoricalRecords()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Абонемент'
        verbose_name_plural = 'Абонементы'


class Clubs(models.Model):
    club_name = models.CharField(verbose_name='Имя клуба', max_length=250)
    location = models.CharField(verbose_name='Местонахождение', max_length=250)
    workin_hours = models.CharField(verbose_name='Рабочие часы', max_length=13)
    date = models.DateField(verbose_name='Дата открытия')
    amount = models.IntegerField(verbose_name='Посетителей в день')

    history = HistoricalRecords()

    def __str__(self):
        return self.club_name


    class Meta:
        verbose_name = 'Клуб'
        verbose_name_plural = 'Клубы'


class Personal(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=100)
    surname = models.CharField(verbose_name='Фамилия', max_length=100)
    age = models.IntegerField(verbose_name='Возраст')
    club = models.ManyToManyField(Clubs,verbose_name='Клуб')

    history = HistoricalRecords()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Персонал'
        verbose_name_plural = 'Персонал'


class Training(models.Model):
    training = models.CharField(verbose_name='Груповая тренировка', max_length=250)
    description = models.CharField(verbose_name='Описание тренировки', max_length=250)
    personal = models.ManyToManyField(Personal,verbose_name='Тренер')
    club = models.ManyToManyField(Clubs,verbose_name='Клуб')
    datetime = models.DateTimeField(verbose_name='Время тренировки')

    history = HistoricalRecords()

    def __str__(self):
        return self.training

    class Meta:
        verbose_name = 'Тренировка'
        verbose_name_plural = 'Тренировки'




