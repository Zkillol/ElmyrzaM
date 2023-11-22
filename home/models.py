from django.db import models

class CountryModel(models.Model):
    GENRE = (
        ('Европа', 'Европа'),
        ('Азия', 'Азия'),
        ('Америка', 'Америка'),
        ('Африка' , "Африка"),
    )
    title = models.CharField(max_length=100, verbose_name='Напишите название страны' , null=True)
    image = models.ImageField(upload_to='countries/', verbose_name='Добавьте фото')
    president = models.CharField(max_length=100, verbose_name='Укажите президента', null=True)
    continent = models.CharField(max_length=100, choices=GENRE , null=True)
    description = models.TextField(blank=True, verbose_name='Описание страны' , null=True)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

class TableCoutnry(models.Model):
    country = models.CharField(max_length=100, verbose_name='Название страны Афиша' , null=True)
    time = models.TimeField(verbose_name='Вылет рейса' , null= True)


    def __str__(self):
        return self.country

class Slider(models.Model):
    slide= models.URLField()


    def __str__(self):
        return self.slide
