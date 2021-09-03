# Generated by Django 3.2.7 on 2021-09-03 09:00

from django.db import migrations


def capitalize(apps, schema_editor):
    Product = apps.get_model('main', 'Product')
    for product in Product.objects.all():
        product.name = product.name.capitalize()
        product.save()


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_productimage_thumbnail'),
    ]

    operations = [
        migrations.RunPython(
            capitalize,
            migrations.RunPython.noop
        ),
    ]