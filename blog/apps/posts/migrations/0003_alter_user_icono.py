# Generated by Django 5.1.1 on 2024-10-14 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_user_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='icono',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='media/usuarios'),
        ),
    ]
