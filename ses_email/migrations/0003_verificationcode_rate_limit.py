# Generated by Django 3.2.7 on 2021-09-22 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ses_email', '0002_verificationcode_validity'),
    ]

    operations = [
        migrations.AddField(
            model_name='verificationcode',
            name='rate_limit',
            field=models.PositiveSmallIntegerField(default=10),
        ),
    ]
