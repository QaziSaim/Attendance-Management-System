# Generated by Django 4.1.4 on 2023-04-15 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AMS', '0002_alter_course_limit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='limit',
            field=models.PositiveIntegerField(default=5),
        ),
    ]