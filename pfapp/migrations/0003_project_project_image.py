# Generated by Django 3.1.7 on 2021-05-02 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pfapp', '0002_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_image',
            field=models.ImageField(blank=True, null=True, upload_to='img'),
        ),
    ]
