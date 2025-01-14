# Generated by Django 2.2.24 on 2023-12-07 14:36

from django.db import migrations


def fill_owners(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    flats = Flat.objects.all()
    if flats.exists():
        for flat in flats.iterator():
            Owner.objects.get_or_create(
                name=flat.owner,
                defaults={
                    'phone_number': flat.owners_phonenumber,
                    'pure_phone': flat.owner_pure_phone
                }
            )


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0009_auto_20231207_1721'),
    ]

    operations = [
        migrations.RunPython(fill_owners),
    ]
