# Generated by Django 3.0.5 on 2020-05-06 21:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BugTracker', '0011_auto_20200503_2250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bug',
            name='assign_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assign_by_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='bug',
            name='assign_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assign_to_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='bug',
            name='media',
            field=models.FileField(blank=True, null=True, upload_to='bugs_media'),
        ),
    ]
