# Generated by Django 4.2 on 2023-06-16 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_alter_body_part_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='body_part',
            field=models.ManyToManyField(to='myapp.body_part'),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='difficulty',
            field=models.ManyToManyField(to='myapp.difficulty'),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='equipment',
            field=models.ManyToManyField(to='myapp.equipment'),
        ),
    ]