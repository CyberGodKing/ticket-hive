# Generated by Django 4.1.5 on 2023-03-12 20:10

import buyticket.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('bank', models.CharField(max_length=50)),
                ('whatsaap', models.URLField()),
                ('account', models.CharField(max_length=15, validators=[buyticket.models.limit_value])),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
            ],
        ),
        migrations.CreateModel(
            name='party',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.PositiveBigIntegerField()),
                ('event', models.CharField(choices=[('ANKARA', 'ANKARA'), ('FRESHER PARTY', 'FRESHER PARTY'), ('NADESTU PARTY', 'NADESTU PARTY'), ('OSTEGA PARTY', 'OSTEGA PARTY')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='user_detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.PositiveBigIntegerField(default=0)),
                ('email', models.EmailField(max_length=254)),
                ('contact', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('quantity', models.PositiveBigIntegerField(default=1)),
                ('user', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentRecipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('imageuploader', models.CharField(max_length=50)),
                ('recipe', models.ImageField(upload_to='images/')),
                ('paid_to', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='buyticket.agent')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', phonenumber_field.modelfields.PhoneNumberField(default=1, max_length=128, region=None)),
                ('amount', models.PositiveIntegerField()),
                ('ref', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('verified', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('name', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-date_created',),
            },
        ),
        migrations.CreateModel(
            name='GenerateReciept',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('party_name', models.CharField(max_length=50)),
                ('dateValidated', models.DateField()),
                ('Reciept_Owner', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('validatedby', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='buyticket.agent')),
            ],
        ),
    ]
