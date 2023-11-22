# Generated by Django 4.2.7 on 2023-11-22 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Afisha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('film', models.CharField(max_length=100, verbose_name='Название фильма Афиша')),
                ('time', models.TimeField(verbose_name='Начало фильма')),
                ('area', models.PositiveIntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='FilmListModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Напишите название фильма')),
                ('image', models.ImageField(upload_to='films/', verbose_name='Добавьте фото')),
                ('year', models.DateField(verbose_name='Укажите год выпуска')),
                ('director', models.CharField(max_length=100, verbose_name='Укажите режисера')),
                ('genre', models.CharField(choices=[('Комедия', 'Комедия'), ('Хоррор', 'Хоррор'), ('Драмма', 'Драмма')], max_length=100)),
                ('description', models.TextField(blank=True, verbose_name='Описание фильма')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Фильм',
                'verbose_name_plural': 'Фильмы',
            },
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slide', models.URLField()),
            ],
        ),
    ]