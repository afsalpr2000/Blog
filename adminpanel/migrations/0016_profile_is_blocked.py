# Generated by Django 5.1 on 2024-10-08 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0015_alter_comment_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_blocked',
            field=models.BooleanField(default=False),
        ),
    ]
