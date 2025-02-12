# Generated by Django 1.11.4 on 2017-09-24 10:05

import django.core.validators
from django.db import migrations, models
import i18nfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ("event", "0006_auto_20170906_0205"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="email",
            field=models.EmailField(default="event@localhost", max_length=254),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="event",
            name="slug",
            field=models.SlugField(
                validators=[
                    django.core.validators.RegexValidator(
                        message="The slug may only contain letters, numbers, dots and dashes.",
                        regex="^[a-zA-Z0-9.-]+$",
                    )
                ]
            ),
        ),
        migrations.AlterField(
            model_name="event",
            name="subtitle",
            field=i18nfield.fields.I18nCharField(blank=True, max_length=200, null=True),
        ),
    ]
