# Generated by Django 3.2.3 on 2022-09-26 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20220926_0832'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery_image',
            name='image',
            field=models.ImageField(null=True, upload_to='home/gallery'),
        ),
    ]
