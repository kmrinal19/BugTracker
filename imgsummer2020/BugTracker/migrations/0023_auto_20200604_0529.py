# Generated by Django 3.0.5 on 2020-06-03 23:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BugTracker', '0022_project_launched'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bug',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bugs_project', to='BugTracker.Project'),
        ),
    ]
