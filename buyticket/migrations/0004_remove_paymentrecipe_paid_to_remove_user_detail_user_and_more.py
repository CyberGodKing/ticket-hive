# Generated by Django 4.1.5 on 2023-03-14 19:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buyticket', '0003_payment_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paymentrecipe',
            name='paid_to',
        ),
        migrations.RemoveField(
            model_name='user_detail',
            name='user',
        ),
        migrations.DeleteModel(
            name='GenerateReciept',
        ),
        migrations.DeleteModel(
            name='PaymentRecipe',
        ),
        migrations.DeleteModel(
            name='user_detail',
        ),
    ]
