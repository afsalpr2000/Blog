# Generated by Django 5.0.6 on 2024-08-02 17:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0002_alter_blog_blog_image_alter_user_id_proof_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Profile',
        ),
    ]
