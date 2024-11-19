# Generated by Django 5.1.3 on 2024-11-19 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aksiyalar', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='image',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='price',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='stock_percent',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='title',
        ),
        migrations.AddField(
            model_name='stock',
            name='from_chat_id',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='from chat id'),
        ),
        migrations.AddField(
            model_name='stock',
            name='message_id',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='message id'),
        ),
    ]