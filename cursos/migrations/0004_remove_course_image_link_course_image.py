# Generated by Django 5.1.2 on 2024-10-15 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0003_course_image_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='image_link',
        ),
        migrations.AddField(
            model_name='course',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='cursos/'),
        ),
    ]
