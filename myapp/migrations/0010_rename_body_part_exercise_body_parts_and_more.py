# Generated by Django 4.2 on 2023-06-16 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_alter_exercise_body_part_alter_exercise_difficulty_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exercise',
            old_name='body_part',
            new_name='body_parts',
        ),
        migrations.RenameField(
            model_name='exercise',
            old_name='difficulty',
            new_name='difficulties',
        ),
        migrations.RenameField(
            model_name='exercise',
            old_name='equipment',
            new_name='equipments',
        ),
    ]
