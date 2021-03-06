# Generated by Django 3.0.5 on 2020-06-13 17:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BugTracker', '0029_auto_20200612_1900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bug',
            name='tag',
            field=models.ManyToManyField(null=True, to='BugTracker.Tag'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='bug',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bugcomments', to='BugTracker.Bug'),
        ),
    ]
