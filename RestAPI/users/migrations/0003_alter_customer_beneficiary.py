# Generated by Django 4.1.1 on 2022-09-16 01:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("recipients", "0002_initial"),
        ("users", "0002_alter_customer_beneficiary"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customer",
            name="beneficiary",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="beneficiary",
                to="recipients.recipient",
            ),
        ),
    ]
