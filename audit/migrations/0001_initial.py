# Generated by Django 4.2.4 on 2023-08-26 08:27

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="IPAuditLog",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "ip",
                    models.GenericIPAddressField(blank=True, editable=False, null=True),
                ),
            ],
        ),
        migrations.CreateModel(
            name="VarcharAuditLog",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("ip", models.CharField(blank=True, max_length=45)),
            ],
        ),
    ]
