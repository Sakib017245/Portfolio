# Generated by Django 3.1.7 on 2021-05-02 10:08

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('pfapp', '0004_auto_20210502_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['top', 'left'], force_format='JPEG', keep_meta=True, null=True, quality=75, size=[500, 300], upload_to='img'),
        ),
    ]