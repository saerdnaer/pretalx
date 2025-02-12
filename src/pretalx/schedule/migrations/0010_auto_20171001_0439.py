# Generated by Django 1.11.5 on 2017-10-01 09:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("schedule", "0010_auto_20171001_1358"),
    ]

    operations = [
        migrations.AlterField(
            model_name="availability",
            name="person",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="availabilities",
                to="person.SpeakerProfile",
            ),
        ),
    ]
