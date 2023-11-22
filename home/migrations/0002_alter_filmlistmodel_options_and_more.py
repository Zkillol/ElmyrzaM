# Generated by Django 4.2.7 on 2023-11-22 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='filmlistmodel',
            options={'verbose_name': 'Город', 'verbose_name_plural': 'Города'},
        ),
        migrations.RemoveField(
            model_name='filmlistmodel',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='filmlistmodel',
            name='director',
        ),
        migrations.RemoveField(
            model_name='filmlistmodel',
            name='genre',
        ),
        migrations.AddField(
            model_name='filmlistmodel',
            name='continent',
            field=models.CharField(choices=[('Комедия', 'Комедия'), ('Хоррор', 'Хоррор'), ('Драмма', 'Драмма')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='filmlistmodel',
            name='president',
            field=models.CharField(max_length=100, null=True, verbose_name='Укажите президента'),
        ),
        migrations.AlterField(
            model_name='filmlistmodel',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание страны'),
        ),
        migrations.AlterField(
            model_name='filmlistmodel',
            name='image',
            field=models.ImageField(upload_to='countries/', verbose_name='Добавьте фото'),
        ),
        migrations.AlterField(
            model_name='filmlistmodel',
            name='title',
            field=models.CharField(max_length=100, null=True, verbose_name='Напишите название страны'),
        ),
        migrations.AlterField(
            model_name='filmlistmodel',
            name='year',
            field=models.DateField(null=True, verbose_name='Укажите возраст страны'),
        ),
    ]