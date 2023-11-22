# Generated by Django 4.2.7 on 2023-11-22 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_remove_filmlistmodel_year'),
    ]

    operations = [
        migrations.CreateModel(
            name='CountryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True, verbose_name='Напишите название страны')),
                ('image', models.ImageField(upload_to='countries/', verbose_name='Добавьте фото')),
                ('president', models.CharField(max_length=100, null=True, verbose_name='Укажите президента')),
                ('continent', models.CharField(choices=[('Европа', 'Европа'), ('Азия', 'Азия'), ('Америка', 'Америка'), ('Африка', 'Африка')], max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание страны')),
            ],
            options={
                'verbose_name': 'Город',
                'verbose_name_plural': 'Города',
            },
        ),
        migrations.RenameModel(
            old_name='Afisha',
            new_name='TableCoutnry',
        ),
        migrations.DeleteModel(
            name='FilmListModel',
        ),
    ]