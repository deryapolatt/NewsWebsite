# Generated by Django 3.2.4 on 2021-06-04 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Haberler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baslik', models.CharField(max_length=200)),
                ('kullanici_adi', models.CharField(max_length=200)),
                ('metin', models.TextField()),
                ('gorsel', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
