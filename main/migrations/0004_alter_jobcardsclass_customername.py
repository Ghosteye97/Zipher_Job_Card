# Generated by Django 3.2 on 2021-11-18 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20211117_0807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobcardsclass',
            name='customerName',
            field=models.CharField(choices=[('Juan Jansen van Rensburg', 'Juan Jansen van Rensburg')], default=1, max_length=100),
        ),
    ]
