# Generated by Django 3.2.7 on 2021-09-21 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ses_email', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='verificationcode',
            name='validity',
            field=models.BooleanField(default=True),
        ),
    ]
