# Generated by Django 3.0.5 on 2020-05-03 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BugTracker', '0008_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='bug',
            name='media',
            field=models.FileField(null=True, upload_to='bugs_media'),
        ),
    ]
