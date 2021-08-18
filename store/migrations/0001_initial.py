# Generated by Django 3.2.6 on 2021-08-18 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Urstore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(default=0)),
                ('banner', models.ImageField(upload_to='products/')),
                ('profile_pic', models.ImageField(upload_to='products/')),
                ('store_name', models.CharField(max_length=58)),
                ('address1', models.CharField(max_length=58)),
                ('address2', models.CharField(max_length=58)),
                ('city', models.CharField(max_length=28)),
                ('zipcode', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=28)),
                ('state', models.CharField(max_length=28)),
                ('phone_number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]