# Generated by Django 5.0.4 on 2024-05-11 06:06

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        (
            "teamboard",
            "0003_rename_description_boardmodel_project_description_and_more",
        ),
    ]

    operations = [
        migrations.RenameField(
            model_name="taskmodel",
            old_name="description",
            new_name="Project_description",
        ),
        migrations.RenameField(
            model_name="taskmodel",
            old_name="title",
            new_name="Project_title",
        ),
        migrations.RenameField(
            model_name="taskmodel",
            old_name="creationtime",
            new_name="created_at",
        ),
        migrations.RenameField(
            model_name="taskmodel",
            old_name="user_id",
            new_name="team",
        ),
    ]
