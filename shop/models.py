from django.db import models

# Create your models here.
class Product(models.Model):
        name = models.CharField('название', max_length=200)
        price = models.CharField('Цена', max_length=200)

        class Meta:
            verbose_name = 'Не заполнять'
            verbose_name_plural = 'Не заполнять'

class Purchase(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    person = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)


class Systemunit(models.Model):
    name = models.CharField('название системного блока', max_length=200)
    price = models.CharField('Цена', max_length=200)
    image = models.ImageField('Изоображение', upload_to="image/")
    description = models.TextField('Описание', max_length=5000)

    class Meta:
        verbose_name = 'Системник'
        verbose_name_plural = 'Системники'

class Accessories(models.Model):
    name = models.CharField('название комлпетующих', max_length=200)
    price = models.CharField('Цена', max_length=200)
    image = models.TextField('URL изоображения', max_length=5000)
    description = models.TextField('Описание', max_length=5000)


    class Meta:
        verbose_name = 'Комлпектующие'
        verbose_name_plural = 'Комлпетующие'

class Noteboo(models.Model):
    name = models.CharField('название ноутбука', max_length=200)
    price = models.CharField('Цена', max_length=200)
    image = models.TextField('URL изоображения', max_length=5000)
    description = models.TextField('Описание', max_length=5000)
    haracteristick = models.TextField('Характеристики', max_length=5000)
    sale5 = models.CharField('скидка 5', max_length=200)
    sale10 = models.CharField('скидка 10', max_length=200)


    class Meta:
        verbose_name = 'Ноутбук'
        verbose_name_plural = 'Ноутбуки'

class Open(models.Model):
    year = models.CharField('Год выпуска', max_length=200)
    name = models.CharField('название ноутбука', max_length=200)
    price = models.CharField('Цена', max_length=200)
    image = models.TextField('URL изоображения', max_length=5000)
    description = models.TextField('Описание', max_length=5000)
    haracteristick = models.TextField('Характеристики', max_length=5000)

    class Meta:
       verbose_name = 'Open'
       verbose_name_plural = 'Open'

class Promocod(models.Model):
    promo = models.CharField('Промокод', max_length=200)
    number = models.TextField('Номер', max_length=11)


    class Meta:
       verbose_name = 'Promocod'
       verbose_name_plural = 'Promocod'

class Notepr(models.Model):
    promo = models.CharField('Скдка 5%', max_length=200)

    class Meta:
       verbose_name = 'Скдка 5%'
       verbose_name_plural = 'Скдка 5%'
