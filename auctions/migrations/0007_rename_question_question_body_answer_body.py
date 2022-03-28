# Generated by Django 4.0.2 on 2022-03-27 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_alter_bid_value'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='question',
            new_name='body',
        ),
        migrations.AddField(
            model_name='answer',
            name='body',
            field=models.TextField(default='Not a valid answer.', max_length=250),
            preserve_default=False,
        ),
    ]
