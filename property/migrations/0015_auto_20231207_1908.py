# Generated by Django 2.2.24 on 2023-12-07 16:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0014_auto_20231207_1856'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='complaint',
            options={'ordering': ['-created_at'], 'verbose_name': 'Жалоба', 'verbose_name_plural': 'Жалобы'},
        ),
        migrations.AlterModelOptions(
            name='flat',
            options={'verbose_name': 'Квартира', 'verbose_name_plural': 'Квартиры'},
        ),
        migrations.AlterModelOptions(
            name='owner',
            options={'ordering': ['name'], 'verbose_name': 'Владелец', 'verbose_name_plural': 'Владельцы'},
        ),
        migrations.AddField(
            model_name='complaint',
            name='created_at',
            field=models.DateTimeField(db_index=True, default=django.utils.timezone.now, verbose_name='Когда создано жалоба'),
        ),
    ]
