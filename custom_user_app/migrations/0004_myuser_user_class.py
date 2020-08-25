# Generated by Django 3.1 on 2020-08-25 23:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('custom_user_app', '0003_auto_20200825_2207'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='user_class',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
