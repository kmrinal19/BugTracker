# Generated by Django 3.0.5 on 2020-06-14 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BugTracker', '0030_auto_20200613_2323'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='attachment',
            field=models.FileField(blank=True, null=True, upload_to='project_attachment'),
        ),
    ]
