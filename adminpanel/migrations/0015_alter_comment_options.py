# Generated by Django 5.1 on 2024-09-04 15:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0014_alter_comment_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-created_at']},
        ),
    ]
