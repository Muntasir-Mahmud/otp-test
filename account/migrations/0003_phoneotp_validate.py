# Generated by Django 3.1.1 on 2020-11-04 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_phoneotp'),
    ]

    operations = [
        migrations.AddField(
            model_name='phoneotp',
            name='validate',
            field=models.BooleanField(default=False, help_text='If it is true, that means user have validate OTP correctly'),
        ),
    ]
