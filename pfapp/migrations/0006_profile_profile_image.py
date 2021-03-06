# Generated by Django 3.1.7 on 2021-05-02 10:19

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('pfapp', '0005_auto_20210502_1608'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['top', 'left'], force_format='JPEG', keep_meta=True, null=True, quality=75, size=[500, 300], upload_to='img'),
        ),
    ]
