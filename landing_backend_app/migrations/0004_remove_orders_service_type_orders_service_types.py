# Generated by Django 5.1 on 2024-08-29 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing_backend_app', '0003_alter_orders_message_alter_orders_messenger_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='service_type',
        ),
        migrations.AddField(
            model_name='orders',
            name='service_types',
            field=models.ManyToManyField(to='landing_backend_app.servicetypes'),
        ),
    ]
