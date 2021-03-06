# Generated by Django 2.0.2 on 2018-03-17 14:54

import accounts.models
from django.db import migrations, models


def populate_internal_name(apps, schema_editor):
    Group = apps.get_model("accounts", "Group")
    for group in Group.objects.all():
        group.internal_name = group.name.lower().replace(" ", "_")
        group.save()


class Migration(migrations.Migration):

    dependencies = [("accounts", "0006_add_username_insensitive_index")]

    operations = [
        migrations.AddField(
            model_name="group",
            name="internal_name",
            field=models.CharField(
                default="", max_length=20, unique=True, validators=[accounts.models.validate_username]
            ),
        ),
        migrations.RunPython(populate_internal_name),
        migrations.AlterField(
            model_name="group",
            name="internal_name",
            field=models.CharField(max_length=20, unique=True, validators=[accounts.models.validate_username]),
        ),
    ]
