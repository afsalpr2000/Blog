# Generated by Django 5.0.6 on 2024-08-02 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blog_image',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='id_proof',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
